---
url: "https://antondevtips.com/blog/how-to-implement-multitenancy-in-asp-net-core-with-ef-core?utm_source=email&utm_medium=email&utm_campaign=website"
captured_at: "2025-08-11T15:25:57+01:00"
title: "How to Implement Multitenancy in ASP.NET Core with EF Core"
domain: "antondevtips-com"
---

---
**Multitenancy** is a software architecture that allows a single instance of a software application to serve multiple customers, called **tenants**. Each tenant's data is isolated and remains invisible to other tenants for security reasons. This architecture is commonly used in Software as a Service (SaaS) applications, where multiple organizations or users share the same application infrastructure while keeping their data secure and separate.

In this blog post, I will share with you my own experience on how to implement multitenancy in ASP.NET Core using Entity Framework Core (EF Core).

## Introduction to Multitenancy

Multitenancy offers several advantages, including:

-   **Cost Efficiency:** shared infrastructure reduces the overall cost of hosting, infrastructure and maintenance.
-   **Simplified Deployment:** centralized updates simplify maintenance and support.
-   **Scalability:** it allows easy scaling of resources for individual tenants based on their needs.
-   **Isolation and Security:** each tenant's data is isolated, ensuring security and privacy.

There are several approaches to separate data for each tenant in multi-tenant applications:

-   **Database-per-Tenant:** each tenant has its own database. This model offers strong data isolation but may increase costs with many tenants.
-   **Schema-per-Tenant:** a single database with separate schemas for each tenant. It provides a balance between isolation and resource sharing.
-   **Table-per-Tenant:** a single database and schema, with tenant-specific tables. This model is efficient but may complicate data management.
-   **Discriminator Column:** a single database, schema, and tables, with a column indicating the tenant. This is the simplest but least isolated model.

**Discriminator column** is one of the most popular approaches to implementing multitenancy. It is cheap in terms of development, deployment and management compared to other options. With modern technologies like ASP.NET Core and EF Core, you can implement discriminator columns in your application without negatively affecting performance and security.

In this blog post I will show you how to implement multitenancy with discriminator column. Let's explore an application that needs to be multi-tenant.

## Multitenant Application Example

Today we will implement multitenancy for the "Books" application that has the following entities:

-   Books
-   Authors
-   Users
-   Tenants

The `Tenant` entity holds information about each customer:

```
<p><code id="code-lang-csharp"><span ne="0.23863679012881822">public</span><span> </span><span ne="0.7098458642759843">class</span><span> </span><span ne="0.8998333732379764">Tenant</span><span> </span><span ne="0.900092065417373">:</span><span> </span><span ne="0.5279009958312543">IAuditableEntity</span><span>
</span><span></span><span ne="0.09356628886071738">{</span><span>
</span><span>    </span><span ne="0.9130769008819388">public</span><span> required </span><span ne="0.5678467920378478">Guid</span><span> Id </span><span ne="0.33262498896700754">{</span><span> </span><span ne="0.21644907520438494">get</span><span ne="0.6930471601639568">;</span><span> </span><span ne="0.7770955042306266">set</span><span ne="0.10429704142398566">;</span><span> </span><span ne="0.6567478198417828">}</span><span>
</span><span>    </span><span ne="0.1292640595751544">public</span><span> required </span><span ne="0.5532431385396565">string</span><span> Name </span><span ne="0.582245845169132">{</span><span> </span><span ne="0.8260806071111814">get</span><span ne="0.5622677443869407">;</span><span> </span><span ne="0.37542757338832977">set</span><span ne="0.19432320224939392">;</span><span> </span><span ne="0.8501973636034196">}</span><span>
</span>    
<span>    </span><span ne="0.4480015351762602">public</span><span> </span><span ne="0.5605261785118851">DateTime</span><span> CreatedAtUtc </span><span ne="0.20517955563163848">{</span><span> </span><span ne="0.352976244087868">get</span><span ne="0.8496282345757287">;</span><span> </span><span ne="0.45096855322468343">set</span><span ne="0.4071543837138337">;</span><span> </span><span ne="0.25445830105681655">}</span><span>
</span><span>    </span><span ne="0.04512862989128974">public</span><span> </span><span ne="0.8446311951688369">DateTime</span><span ne="0.3061448816460961">?</span><span> UpdatedAtUtc </span><span ne="0.13746704733536919">{</span><span> </span><span ne="0.5827828381321428">get</span><span ne="0.865074716557894">;</span><span> </span><span ne="0.32595586717560865">set</span><span ne="0.026871916208505264">;</span><span> </span><span ne="0.33070916647133874">}</span><span>
</span><span></span><span ne="0.023353498287402186">}</span></code></p>
```

Every `Book`, `Author` and `User` entities in our database belong to a specific tenant. You need to create a `ITenantEntity` interface that should be inherited by all entities that need to be multi-tenant:

```
<p><code id="code-lang-csharp"><span ne="0.6485895657913496">public</span><span> </span><span ne="0.8114920083722137">interface</span><span> </span><span ne="0.49570370806443476">ITenantEntity</span><span>
</span><span></span><span ne="0.7068493724927782">{</span><span>
</span><span>    </span><span ne="0.9059212875602627">public</span><span> </span><span ne="0.5107551157994712">Guid</span><span ne="0.3294599718862241">?</span><span> TenantId </span><span ne="0.13159844329395476">{</span><span> </span><span ne="0.6287699013733574">get</span><span ne="0.13930694307548763">;</span><span> </span><span ne="0.39096837883087765">set</span><span ne="0.9228864826067845">;</span><span> </span><span ne="0.11232762605051938">}</span><span>
</span><span></span><span ne="0.137372423615284">}</span></code></p>
```

Let's explore, for example, User and Book entities:

```
<p><code id="code-lang-csharp"><span ne="0.7758700400642334">public</span><span> </span><span ne="0.33286523934748025">class</span><span> </span><span ne="0.7053882066354105">User</span><span> </span><span ne="0.6014786642907817">:</span><span> </span><span ne="0.8385778634934024">IAuditableEntity</span><span ne="0.26508751973045674">,</span><span> </span><span ne="0.20870690865202568">ITenantEntity</span><span>
</span><span></span><span ne="0.13547598967971264">{</span><span>
</span><span>    </span><span ne="0.17281288252812088">public</span><span> </span><span ne="0.7571331802067972">Guid</span><span> Id </span><span ne="0.28765573018192114">{</span><span> </span><span ne="0.9847437664782364">get</span><span ne="0.3353700930450023">;</span><span> </span><span ne="0.41292998364083433">set</span><span ne="0.26008753428329157">;</span><span> </span><span ne="0.7248165229144672">}</span><span>
</span><span>    </span><span ne="0.7005855133804227">public</span><span> required </span><span ne="0.48393328746998">string</span><span> Email </span><span ne="0.9304587939595479">{</span><span> </span><span ne="0.2325477421678771">get</span><span ne="0.5214450148675894">;</span><span> </span><span ne="0.4255724128328431">set</span><span ne="0.33714440325418904">;</span><span> </span><span ne="0.7381244226264879">}</span><span>
</span>    
<span>    </span><span ne="0.520455374584428">public</span><span> </span><span ne="0.3071153491123728">DateTime</span><span> CreatedAtUtc </span><span ne="0.033168779117503266">{</span><span> </span><span ne="0.3349346522457617">get</span><span ne="0.18608410431517375">;</span><span> </span><span ne="0.21116475277971958">set</span><span ne="0.17415190269026226">;</span><span> </span><span ne="0.45203106876262433">}</span><span>
</span><span>    </span><span ne="0.716732346176352">public</span><span> </span><span ne="0.022771957472066062">DateTime</span><span ne="0.12109258855836902">?</span><span> UpdatedAtUtc </span><span ne="0.7826566272919674">{</span><span> </span><span ne="0.7285613341602339">get</span><span ne="0.01677761362248764">;</span><span> </span><span ne="0.5667990190117171">set</span><span ne="0.7804194744063788">;</span><span> </span><span ne="0.41125746573801136">}</span><span>
</span>    
<span>    </span><span ne="0.5695556732439522">public</span><span> </span><span ne="0.2324911422956062">Guid</span><span ne="0.9568051520923339">?</span><span> TenantId </span><span ne="0.2136535248877488">{</span><span> </span><span ne="0.02591827428397453">get</span><span ne="0.80257082693783">;</span><span> </span><span ne="0.7319399895994235">set</span><span ne="0.36368616245138574">;</span><span> </span><span ne="0.33392331240695916">}</span><span>
</span><span></span><span ne="0.34874347650874604">}</span><span>
</span>
<span></span><span ne="0.7382066132160985">public</span><span> </span><span ne="0.6498348288187396">class</span><span> </span><span ne="0.8977750537234215">Book</span><span> </span><span ne="0.7800997251327196">:</span><span> </span><span ne="0.9756545283763909">IAuditableEntity</span><span ne="0.6781468630808412">,</span><span> </span><span ne="0.3895425136576891">ITenantEntity</span><span>
</span><span></span><span ne="0.4469306581989726">{</span><span>
</span><span>    </span><span ne="0.1213796616039653">public</span><span> required </span><span ne="0.7332085065794761">Guid</span><span> Id </span><span ne="0.9699621385627494">{</span><span> </span><span ne="0.811760998942196">get</span><span ne="0.7816078971123789">;</span><span> </span><span ne="0.6836649369638103">set</span><span ne="0.6484118204794952">;</span><span> </span><span ne="0.5364802948894771">}</span><span>
</span><span>    </span><span ne="0.2034703561059723">public</span><span> required </span><span ne="0.3916026350275208">string</span><span> Title </span><span ne="0.1100180374972336">{</span><span> </span><span ne="0.9090016984583523">get</span><span ne="0.3438050511744033">;</span><span> </span><span ne="0.9424200914532543">set</span><span ne="0.09677927053254542">;</span><span> </span><span ne="0.6130003762239865">}</span><span>
</span><span>    </span><span ne="0.6104302678803902">public</span><span> required </span><span ne="0.34313952917028057">int</span><span> Year </span><span ne="0.8517129859584397">{</span><span> </span><span ne="0.10281743331567572">get</span><span ne="0.005644235566356293">;</span><span> </span><span ne="0.34638661323309106">set</span><span ne="0.21620618371729228">;</span><span> </span><span ne="0.10983075676888698">}</span><span>
</span><span>    </span><span ne="0.6227986968942487">public</span><span> </span><span ne="0.0015136232705421637">Guid</span><span> AuthorId </span><span ne="0.8185734724584525">{</span><span> </span><span ne="0.2021961937667781">get</span><span ne="0.46751448243725346">;</span><span> </span><span ne="0.8827330548449419">set</span><span ne="0.4711750590936261">;</span><span> </span><span ne="0.5199340033205455">}</span><span>
</span><span>    </span><span ne="0.1301724547552312">public</span><span> </span><span ne="0.3302960621545137">Author</span><span> Author </span><span ne="0.9935587662569695">{</span><span> </span><span ne="0.41176037640310736">get</span><span ne="0.38278187566624466">;</span><span> </span><span ne="0.8107975886517501">set</span><span ne="0.9209822958238267">;</span><span> </span><span ne="0.1593054099666399">}</span><span> </span><span ne="0.05197044681864793">=</span><span> </span><span ne="0.628013099696358">null</span><span ne="0.10864778903596684">!</span><span ne="0.8780901598650416">;</span><span>
</span>
<span>    </span><span ne="0.45127606122770336">public</span><span> </span><span ne="0.25925441259178705">DateTime</span><span> CreatedAtUtc </span><span ne="0.10868630735786133">{</span><span> </span><span ne="0.8685562126604168">get</span><span ne="0.1892320864893121">;</span><span> </span><span ne="0.018466960246632746">set</span><span ne="0.8035302041524526">;</span><span> </span><span ne="0.2714533473921248">}</span><span>
</span><span>    </span><span ne="0.749220820313416">public</span><span> </span><span ne="0.04384685808191813">DateTime</span><span ne="0.43647538472814784">?</span><span> UpdatedAtUtc </span><span ne="0.7160559434238037">{</span><span> </span><span ne="0.5527615849699823">get</span><span ne="0.9879299230529939">;</span><span> </span><span ne="0.03724663535686956">set</span><span ne="0.20490943374404913">;</span><span> </span><span ne="0.43329222800151557">}</span><span>
</span>
<span>    </span><span ne="0.35683473209847816">public</span><span> </span><span ne="0.6060812798627868">Guid</span><span ne="0.8305557435518041">?</span><span> TenantId </span><span ne="0.5668324434241401">{</span><span> </span><span ne="0.5183268401433009">get</span><span ne="0.004020245985835946">;</span><span> </span><span ne="0.699314785422803">set</span><span ne="0.34669110591563346">;</span><span> </span><span ne="0.7966861213580272">}</span><span>
</span><span></span><span ne="0.9749837418419374">}</span></code></p>
```

Every entity has a foreign key relationship with `Tenant` entity, for example, User:

```
<p><code id="code-lang-csharp"><span ne="0.030996244379246085">public</span><span> </span><span ne="0.7880629831144929">class</span><span> </span><span ne="0.6354321748857042">UserConfiguration</span><span> </span><span ne="0.746856504853727">:</span><span> </span><span ne="0.24407666104851733">IEntityTypeConfiguration</span><span ne="0.8399643183749161">&lt;</span><span ne="0.47459513822279664">User</span><span ne="0.7913884682025216">&gt;</span><span>
</span><span></span><span ne="0.21191038732698875">{</span><span>
</span><span>    </span><span ne="0.352590178813309">public</span><span> </span><span ne="0.02270562617024996">void</span><span> </span><span ne="0.9665226531168986">Configure</span><span ne="0.7551229288372895">(</span><span ne="0.7008255568947171">EntityTypeBuilder</span><span ne="0.4392729434261231">&lt;</span><span ne="0.2697199411159559">User</span><span ne="0.06477673430140884">&gt;</span><span> builder</span><span ne="0.1079602815488897">)</span><span>
</span><span>    </span><span ne="0.6793407978825555">{</span><span>
</span><span>        builder</span><span ne="0.8754207297784411">.</span><span ne="0.844187542361862">ToTable</span><span ne="0.2710599939287248">(</span><span ne="0.5567138984196901">"users"</span><span ne="0.3607249228071501">)</span><span ne="0.9414613136319809">;</span><span>
</span>
<span>        builder</span><span ne="0.5685988947880729">.</span><span ne="0.29043669403774897">HasKey</span><span ne="0.9288333120132166">(</span><span>x </span><span ne="0.8579216870202611">=&gt;</span><span> x</span><span ne="0.9352418869594484">.</span><span>Id</span><span ne="0.48746901677580223">)</span><span ne="0.9491593098984256">;</span><span>
</span><span>        builder</span><span ne="0.13862296067658697">.</span><span ne="0.8313319496402036">HasIndex</span><span ne="0.5765525410393751">(</span><span>x </span><span ne="0.6992828268751584">=&gt;</span><span> x</span><span ne="0.5978052811363301">.</span><span>Email</span><span ne="0.697861399600191">)</span><span ne="0.46718697073682147">;</span><span>
</span>
<span>        builder</span><span ne="0.42309828541841976">.</span><span ne="0.6212251641435953">Property</span><span ne="0.21850862178252084">(</span><span>x </span><span ne="0.19253889701217775">=&gt;</span><span> x</span><span ne="0.09374347905346025">.</span><span>Id</span><span ne="0.20785213505292366">)</span><span ne="0.04169620964755105">.</span><span ne="0.9483403881641305">ValueGeneratedOnAdd</span><span ne="0.4038507160649588">(</span><span ne="0.953329992369626">)</span><span ne="0.37731182015049514">;</span><span>
</span><span>        builder</span><span ne="0.5462923195508774">.</span><span ne="0.22083396597099736">Property</span><span ne="0.9877295603909917">(</span><span>x </span><span ne="0.36035553450518565">=&gt;</span><span> x</span><span ne="0.7047221378499569">.</span><span>Email</span><span ne="0.6052142169137829">)</span><span ne="0.35554557550294186">.</span><span ne="0.99496821234716">IsRequired</span><span ne="0.9981890015249761">(</span><span ne="0.18195480578400214">)</span><span ne="0.9507247370186012">;</span><span>
</span><span>        builder</span><span ne="0.9916300923454445">.</span><span ne="0.8859147305939221">Property</span><span ne="0.8775914823929207">(</span><span>x </span><span ne="0.9103984523825756">=&gt;</span><span> x</span><span ne="0.8446649039566877">.</span><span>CreatedAtUtc</span><span ne="0.3394626893372884">)</span><span ne="0.4680778947936791">.</span><span ne="0.24462558027934633">IsRequired</span><span ne="0.44361571252404297">(</span><span ne="0.27058890602788854">)</span><span ne="0.469932472611566">;</span><span>
</span><span>        builder</span><span ne="0.1499811538617073">.</span><span ne="0.8994325989126386">Property</span><span ne="0.3380899469583172">(</span><span>x </span><span ne="0.8676237869569615">=&gt;</span><span> x</span><span ne="0.5904629611714276">.</span><span>UpdatedAtUtc</span><span ne="0.2685546321001808">)</span><span ne="0.10983679421998682">;</span><span>
</span>
<span>        builder</span><span ne="0.8822488456401036">.</span><span ne="0.18852125491625715">HasOne</span><span ne="0.8689766096366784">&lt;</span><span ne="0.8540834858893386">Tenant</span><span ne="0.09942438028099754">&gt;</span><span ne="0.548841392399688">(</span><span ne="0.7226563901412415">)</span><span>
</span><span>            </span><span ne="0.7258628068136888">.</span><span ne="0.3082780438811211">WithMany</span><span ne="0.6488909306054913">(</span><span ne="0.4420890132371601">)</span><span>
</span><span>            </span><span ne="0.13409065705970125">.</span><span ne="0.8025273140960075">HasForeignKey</span><span ne="0.461224454188786">(</span><span>e </span><span ne="0.9170395851558045">=&gt;</span><span> e</span><span ne="0.26967061370673473">.</span><span>TenantId</span><span ne="0.8106300815098141">)</span><span>
</span><span>            </span><span ne="0.9524928896471917">.</span><span ne="0.3868333363463261">IsRequired</span><span ne="0.3940760310248782">(</span><span ne="0.1940052664469899">false</span><span ne="0.21523793049918893">)</span><span>
</span><span>            </span><span ne="0.6970271922392168">.</span><span ne="0.9459936389543426">OnDelete</span><span ne="0.6994272723757323">(</span><span>DeleteBehavior</span><span ne="0.37294225302469997">.</span><span>SetNull</span><span ne="0.556256339918322">)</span><span ne="0.8923498640917183">;</span><span>
</span><span>    </span><span ne="0.7621664595985237">}</span><span>
</span><span></span><span ne="0.9375556518496855">}</span></code></p>
```

Depending on your application needs, you may have this foreign key or have a plain `TenantId` column without a reference.

## How To Implement Multitenancy in EF Core

To implement multitenancy, we need to do the following:

1.  After a user logs in, we need to add a tenant identifier in the user claims.
2.  From every request from the frontend (or another application) whether we need to retrieve or modify data, we need to get the user tenant identifier from the user claims.
3.  Whenever a user requests data from the backend - we can use EF Core [Global Query Filters](https://antondevtips.com/blog/global-query-filters-in-ef-core) to automatically filter only those records from the database that a user has access to.
4.  Whenever a user creates, updates or deletes data - we can automatically assign a "TenantId" column in the [Change Tracker](https://antondevtips.com/blog/understanding-change-tracking-for-better-performance-in-ef-core) with a user tenant identifier.

By utilizing EF Core capabilities (Global Query Filters and Change Tracker) we no longer need to write custom filters in each query or provide a tenant id in every create, update or delete action. EF Core helps us to implement multitenancy once that will be applied to all entities that need to be multi-tenant.

This approach secures your code from the critical bugs where you may forget to add a check for a tenant in one of the queries and expose another customer's data.

## Implementing Multitenancy for Read Operations in EF Core

We can implement multitenancy in EF Core DbContext that will automatically be applied to all entities that inherit from `ITenantEntity`.

Let's define a `TenantProvider` that will retrieve user and tenant identifiers from the current HttpRequest:

```
<p><code id="code-lang-csharp"><span ne="0.7655914836386543">public</span><span> </span><span ne="0.05357280283636512">interface</span><span> </span><span ne="0.8911600310389697">ITenantProvider</span><span>
</span><span></span><span ne="0.14713233660667657">{</span><span>
</span><span>    </span><span ne="0.457710946008548">TenantInfo</span><span> </span><span ne="0.5948749522112947">GetCurrentTenantInfo</span><span ne="0.4076550648661771">(</span><span ne="0.32516314033206006">)</span><span ne="0.9372979200328269">;</span><span>
</span><span></span><span ne="0.331262458121089">}</span><span>
</span>
<span></span><span ne="0.3662332814342881">public</span><span> </span><span ne="0.8303104528270193">class</span><span> </span><span ne="0.3954876570217484">TenantProvider</span><span> </span><span ne="0.4379199497134635">:</span><span> </span><span ne="0.26337287252570674">ITenantProvider</span><span>
</span><span></span><span ne="0.44685105546317494">{</span><span>
</span><span>    </span><span ne="0.7353276326870068">private</span><span> </span><span ne="0.423766901734399">readonly</span><span> </span><span ne="0.6490970209392979">TenantInfo</span><span> _tenantInfo</span><span ne="0.23412456808869142">;</span><span>
</span>
<span>    </span><span ne="0.8264445629059778">public</span><span> </span><span ne="0.634744106100959">TenantProvider</span><span ne="0.9929128548336583">(</span><span ne="0.5341812153808448">IHttpContextAccessor</span><span> accessor</span><span ne="0.25703174064375944">)</span><span>
</span><span>    </span><span ne="0.12787242204510618">{</span><span>
</span><span>        </span><span ne="0.1932421457281278">var</span><span> userIdValue </span><span ne="0.6629364595615057">=</span><span> accessor</span><span ne="0.20570615951500437">.</span><span>HttpContext</span><span ne="0.28314320575929597">?.</span><span>User</span><span ne="0.6197796922586297">.</span><span ne="0.23583481177847332">FindFirstValue</span><span ne="0.7234689518242797">(</span><span ne="0.6252575798527247">"user-id"</span><span ne="0.6976447799323311">)</span><span ne="0.9570802444044086">;</span><span>
</span><span>        </span><span ne="0.7141869049741827">var</span><span> tenantIdValue </span><span ne="0.9089349223064612">=</span><span> accessor</span><span ne="0.3906308578365083">.</span><span>HttpContext</span><span ne="0.1940668377451571">?.</span><span>User</span><span ne="0.30890311055250597">.</span><span ne="0.9109349627185997">FindFirstValue</span><span ne="0.6029007308781611">(</span><span ne="0.09377710390837635">"tenant-id"</span><span ne="0.1531212266735097">)</span><span ne="0.6925753411660519">;</span><span>
</span>
<span>        </span><span ne="0.5640366254802242">Guid</span><span ne="0.963590786246216">?</span><span> userId </span><span ne="0.1291886882884007">=</span><span> Guid</span><span ne="0.18633859247118612">.</span><span>TryParse</span><span ne="0.9411857323427794">(</span><span ne="0.784083317892565">userIdValue</span><span ne="0.8622957486612328">,</span><span ne="0.8686622099711124"> </span><span ne="0.8508378057255117">out</span><span ne="0.6215267892335347"> </span><span ne="0.8887931878183551">var</span><span ne="0.6300568421443963"> guid</span><span ne="0.8106732237042102">)</span><span ne="0.00005164236485755147"> </span><span ne="0.08835089470277335">?</span><span> guid </span><span ne="0.40529140776047423">:</span><span> </span><span ne="0.7402748087043375">null</span><span ne="0.4802250916531522">;</span><span>
</span><span>        </span><span ne="0.7510761686743243">Guid</span><span ne="0.019981991580848013">?</span><span> tenantId </span><span ne="0.6271843992083117">=</span><span> Guid</span><span ne="0.13606540729338268">.</span><span>TryParse</span><span ne="0.9503549311215967">(</span><span ne="0.714503120819029">tenantIdValue</span><span ne="0.8844456448083412">,</span><span ne="0.18912009165669252"> </span><span ne="0.21151945767725333">out</span><span ne="0.6232804775995866"> guid</span><span ne="0.4715899720820578">)</span><span ne="0.824101364404709"> </span><span ne="0.1059104808621727">?</span><span> guid </span><span ne="0.3963470490741374">:</span><span> </span><span ne="0.47366553716637305">null</span><span ne="0.6526927768665272">;</span><span>
</span>
<span>        _tenantInfo </span><span ne="0.8171476965889396">=</span><span> </span><span ne="0.9749808556932578">new</span><span> </span><span ne="0.8675978140422026">TenantInfo</span><span ne="0.43139286900712637">(</span><span>userId</span><span ne="0.33267576821394196">,</span><span> tenantId</span><span ne="0.6521249551811573">)</span><span ne="0.7489456294007039">;</span><span>
</span><span>    </span><span ne="0.004269849677421389">}</span><span>
</span>
<span>    </span><span ne="0.423051953421105">public</span><span> </span><span ne="0.4516081310884129">TenantInfo</span><span> </span><span ne="0.5946466310507434">GetCurrentTenantInfo</span><span ne="0.9410660631344383">(</span><span ne="0.3232991263460232">)</span><span> </span><span ne="0.5684777214407685">=&gt;</span><span> _tenantInfo</span><span ne="0.20281440846517262">;</span><span>
</span><span></span><span ne="0.5311277987781522">}</span></code></p>
```

Here we retrieve the "user-id" and "tenant-id" from the `ClaimsPrinciple`.

You need to register the provider and `IHttpContextAccessor` in the DI:

```
<p><code id="code-lang-csharp"><span>builder</span><span ne="0.3481538852403322">.</span><span>Services</span><span ne="0.15873511795682793">.</span><span ne="0.9683469905659998">AddHttpContextAccessor</span><span ne="0.9437043071173041">(</span><span ne="0.19294856876008137">)</span><span ne="0.6361003379071262">;</span><span>
</span><span>builder</span><span ne="0.38000666488778023">.</span><span>Services</span><span ne="0.10828528932973758">.</span><span ne="0.5898924712390871">AddScoped</span><span ne="0.9639093336635809">&lt;</span><span ne="0.8245382318102928">ITenantProvider</span><span ne="0.38842899261036623">,</span><span ne="0.7622997266496747"> TenantProvider</span><span ne="0.5982158242662824">&gt;</span><span ne="0.9102147907671151">(</span><span ne="0.6746043994018981">)</span><span ne="0.3115942526884472">;</span></code></p>
```

We need to inject `ITenantProvider` into DbContext and create a public property for it:

```
<p><code id="code-lang-csharp"><span ne="0.6245154351575852">public</span><span> </span><span ne="0.7727054957512058">class</span><span> </span><span ne="0.2099425120084012">ApplicationDbContext</span><span ne="0.9878269286420492">(</span><span>
</span><span>    </span><span ne="0.6869942341809985">DbContextOptions</span><span ne="0.37711898302615987">&lt;</span><span ne="0.3096918770623557">ApplicationDbContext</span><span ne="0.3144092318065562">&gt;</span><span> options</span><span ne="0.008402848065836022">,</span><span>
</span><span>    </span><span ne="0.5198861967358548">ITenantProvider</span><span> tenantProvider</span><span ne="0.841018381105626">)</span><span>
</span><span>    </span><span ne="0.0575991700551437">:</span><span> </span><span ne="0.44856215270241484">DbContext</span><span ne="0.7557563896025844">(</span><span>options</span><span ne="0.32209761333623577">)</span><span>
</span><span></span><span ne="0.509483345494038">{</span><span>
</span><span>    </span><span ne="0.6013922921574014">public</span><span> </span><span ne="0.2664194779031186">ITenantProvider</span><span> TenantProvider </span><span ne="0.03335199751272522">=&gt;</span><span> tenantProvider</span><span ne="0.07952258189199835">;</span><span>
</span>
<span>    </span><span ne="0.952407395532227">public</span><span> </span><span ne="0.5868563440568453">DbSet</span><span ne="0.2220490793377643">&lt;</span><span ne="0.4378544113692219">Author</span><span ne="0.7851524224898534">&gt;</span><span> Authors </span><span ne="0.5913283113745285">{</span><span> </span><span ne="0.052949962557938046">get</span><span ne="0.5353886888222039">;</span><span> </span><span ne="0.282250663927164">set</span><span ne="0.8451517551250445">;</span><span> </span><span ne="0.17782741637135946">}</span><span> </span><span ne="0.9709941538394231">=</span><span> </span><span ne="0.2553885894007354">default</span><span ne="0.27962422296531175">!</span><span ne="0.3885792003208247">;</span><span>
</span><span>    </span><span ne="0.910614230386717">public</span><span> </span><span ne="0.3328613954499643">DbSet</span><span ne="0.7590526997493445">&lt;</span><span ne="0.5094988413427004">Book</span><span ne="0.04904468993262712">&gt;</span><span> Books </span><span ne="0.6712915175718585">{</span><span> </span><span ne="0.5863064608483071">get</span><span ne="0.5959284602893463">;</span><span> </span><span ne="0.773112080715044">set</span><span ne="0.1854971778441339">;</span><span> </span><span ne="0.6109293902263735">}</span><span> </span><span ne="0.44054053652422576">=</span><span> </span><span ne="0.51608847806079">default</span><span ne="0.4402986189489805">!</span><span ne="0.353770126373235">;</span><span>
</span><span>    </span><span ne="0.3041940762073412">public</span><span> </span><span ne="0.35569345567006416">DbSet</span><span ne="0.4772107710500726">&lt;</span><span ne="0.8266000224126687">User</span><span ne="0.722701043180495">&gt;</span><span> Users </span><span ne="0.9932983207404392">{</span><span> </span><span ne="0.8484840408662794">get</span><span ne="0.5079093898172709">;</span><span> </span><span ne="0.8439372693435837">set</span><span ne="0.17514769015691434">;</span><span> </span><span ne="0.417509170339299">}</span><span> </span><span ne="0.4553199564732594">=</span><span> </span><span ne="0.6981831919722634">default</span><span ne="0.812729488237113">!</span><span ne="0.028473526933699533">;</span><span>
</span><span>    </span><span ne="0.5418330693393556">public</span><span> </span><span ne="0.8227732456079199">DbSet</span><span ne="0.2942817392719346">&lt;</span><span ne="0.5941131889820306">Tenant</span><span ne="0.020717058944841327">&gt;</span><span> Tenants </span><span ne="0.3727812848319867">{</span><span> </span><span ne="0.876607108676374">get</span><span ne="0.09881487647531051">;</span><span> </span><span ne="0.5883788293684502">set</span><span ne="0.05714682141201255">;</span><span> </span><span ne="0.016693124396239267">}</span><span> </span><span ne="0.5765986619108903">=</span><span> </span><span ne="0.07020781111289687">default</span><span ne="0.3796979055359425">!</span><span ne="0.014578346796510488">;</span><span>
</span><span></span><span ne="0.1108167300173476">}</span></code></p>
```

In the `OnModelCreating` method you can specify Global Query Filters for all our tenant entities:

```
<p><code id="code-lang-csharp"><span ne="0.1377333702924498">protected</span><span> </span><span ne="0.7213809535919715">override</span><span> </span><span ne="0.6664223901261093">void</span><span> </span><span ne="0.43919746687234007">OnModelCreating</span><span ne="0.15448285702956266">(</span><span ne="0.4967452438167579">ModelBuilder</span><span> modelBuilder</span><span ne="0.3947854324013833">)</span><span>
</span><span></span><span ne="0.48659148721704826">{</span><span>
</span><span>    modelBuilder</span><span ne="0.9126845524376053">.</span><span ne="0.7105166911251082">Entity</span><span ne="0.5499827982841129">&lt;</span><span ne="0.9230510473136578">User</span><span ne="0.9272924103082">&gt;</span><span ne="0.14091423420610216">(</span><span ne="0.7822996383571532">)</span><span>
</span><span>        </span><span ne="0.21340606872319612">.</span><span ne="0.11652641610219883">HasQueryFilter</span><span ne="0.9604551843460091">(</span><span>x </span><span ne="0.31838092125403383">=&gt;</span><span> x</span><span ne="0.6843963174421425">.</span><span>TenantId</span><span ne="0.8919056349099956">.</span><span ne="0.45759934349023845">Equals</span><span ne="0.41579057326828506">(</span><span>TenantProvider</span><span ne="0.2757627706642555">.</span><span ne="0.3927985073151009">GetCurrentTenantInfo</span><span ne="0.8987968913256177">(</span><span ne="0.8671551334889394">)</span><span ne="0.5971718593686">.</span><span>TenantId</span><span ne="0.9372349581447157">)</span><span ne="0.5477824188813851">)</span><span ne="0.9217203297307213">;</span><span>
</span>
<span>    modelBuilder</span><span ne="0.28809704541006476">.</span><span ne="0.1762821374503174">Entity</span><span ne="0.24053819461346015">&lt;</span><span ne="0.9798792489489274">Author</span><span ne="0.9821391772676431">&gt;</span><span ne="0.39546270843851616">(</span><span ne="0.7082089386477949">)</span><span>
</span><span>        </span><span ne="0.6355935869615896">.</span><span ne="0.8688238896903451">HasQueryFilter</span><span ne="0.1879717297370942">(</span><span>x </span><span ne="0.9920892081884743">=&gt;</span><span> x</span><span ne="0.9271089434621661">.</span><span>TenantId</span><span ne="0.01343177176344712">.</span><span ne="0.07442741720829749">Equals</span><span ne="0.6714485016477372">(</span><span>TenantProvider</span><span ne="0.561652201861613">.</span><span ne="0.26280376559407337">GetCurrentTenantInfo</span><span ne="0.651253522644566">(</span><span ne="0.16909062965976218">)</span><span ne="0.3911751405489676">.</span><span>TenantId</span><span ne="0.31992508403198106">)</span><span ne="0.22267044184699358">)</span><span ne="0.21966318081398817">;</span><span>
</span>
<span>    modelBuilder</span><span ne="0.08814216762273486">.</span><span ne="0.8776431697746361">Entity</span><span ne="0.6846751579676952">&lt;</span><span ne="0.41919049218657">Book</span><span ne="0.3413234868603907">&gt;</span><span ne="0.4673438740528849">(</span><span ne="0.8430081564225795">)</span><span>
</span><span>        </span><span ne="0.8706690662234141">.</span><span ne="0.7195252408949583">HasQueryFilter</span><span ne="0.12817463088660552">(</span><span>x </span><span ne="0.29854314951833705">=&gt;</span><span> x</span><span ne="0.3023615578825264">.</span><span>TenantId</span><span ne="0.966144991520065">.</span><span ne="0.23560566776709368">Equals</span><span ne="0.5357421874449341">(</span><span>TenantProvider</span><span ne="0.27983477423616576">.</span><span ne="0.7902835624511529">GetCurrentTenantInfo</span><span ne="0.007080770718480123">(</span><span ne="0.48931935206815513">)</span><span ne="0.6606708568097309">.</span><span>TenantId</span><span ne="0.2584529622911511">)</span><span ne="0.8903107684516058">)</span><span ne="0.7496439358991143">;</span><span>
</span>
<span>    </span><span ne="0.1728369538932718">base</span><span ne="0.878354041298987">.</span><span ne="0.7850004501506004">OnModelCreating</span><span ne="0.020244759561196535">(</span><span>modelBuilder</span><span ne="0.05993281800100814">)</span><span ne="0.6428889850746557">;</span><span>
</span>
<span>    modelBuilder</span><span ne="0.02238412875382856">.</span><span ne="0.537976602704329">HasDefaultSchema</span><span ne="0.9671158002349658">(</span><span ne="0.5890586243134041">"devtips_multitenancy"</span><span ne="0.5498219127462686">)</span><span ne="0.7293929764646545">;</span><span>
</span><span>    modelBuilder</span><span ne="0.34139995328900363">.</span><span ne="0.23459975876258776">ApplyConfigurationsFromAssembly</span><span ne="0.8081603214367162">(</span><span ne="0.12169380139366348">typeof</span><span ne="0.07806891690867257">(</span><span ne="0.3011785657551581">BookConfiguration</span><span ne="0.47816177060197573">)</span><span ne="0.9812128034617136">.</span><span>Assembly</span><span ne="0.46987795507021013">)</span><span ne="0.43528782394137033">;</span><span>
</span><span></span><span ne="0.11085355806792807">}</span></code></p>
```

It is important to specify `HasQueryFilter` before calling `base.OnModelCreating(modelBuilder);`.

Whenever you add a new entity in your project, simply add a new query filter and all read operations for this entity will be filtered accordingly by a user's tenant. This ensures that a user will only have access to their own data.

> **It is crucial** to work with `TenantProvider` with a public property, otherwise EF Core Global Query Filters won't be applied correctly per each request.

## Implementing Multitenancy for Write Operations in EF Core

We can override `SaveChangesAsync` method in EF Core DbContext to implement multitenancy for write operations:

```
<p><code id="code-lang-csharp"><span ne="0.1682195986342091">public</span><span> </span><span ne="0.7190105447685449">override</span><span> </span><span ne="0.6785780483448919">async</span><span> </span><span ne="0.5015525323177357">Task</span><span ne="0.9556647534588117">&lt;</span><span ne="0.33171907797082667">int</span><span ne="0.8836059172280671">&gt;</span><span> </span><span ne="0.18470426196643963">SaveChangesAsync</span><span ne="0.32272950003223366">(</span><span ne="0.3062659545782931">CancellationToken</span><span> cancellationToken </span><span ne="0.15373790332334725">=</span><span> </span><span ne="0.8644902354338052">new</span><span ne="0.34157859155027603">(</span><span ne="0.9695831527229498">)</span><span ne="0.8291851854919895">)</span><span>
</span><span></span><span ne="0.659653844626334">{</span><span>
</span><span>    </span><span ne="0.48862220947561985">var</span><span> tenantInfo </span><span ne="0.143824296368665">=</span><span> TenantProvider</span><span ne="0.13981156019308927">.</span><span ne="0.18233258570803712">GetCurrentTenantInfo</span><span ne="0.696410921085958">(</span><span ne="0.21753402344856032">)</span><span ne="0.10362787518655348">;</span><span>
</span>
<span>    </span><span ne="0.05137433483110987">var</span><span> modifiedTenantEntries </span><span ne="0.3639847023310516">=</span><span> ChangeTracker</span><span ne="0.8136475074501354">.</span><span ne="0.18991279710807152">Entries</span><span ne="0.056504579601267646">&lt;</span><span ne="0.04692656350082569">ITenantEntity</span><span ne="0.4464202730247294">&gt;</span><span ne="0.8069208500345418">(</span><span ne="0.9411806222845838">)</span><span>
</span><span>        </span><span ne="0.5965107264193658">.</span><span ne="0.7383671599023831">Where</span><span ne="0.8254081881752643">(</span><span>x </span><span ne="0.8212662705238365">=&gt;</span><span> x</span><span ne="0.4623220253916396">.</span><span>State </span><span ne="0.24706311876615594">is</span><span> </span><span ne="0.25474956101116353">EntityState</span><span ne="0.31708478379626426">.</span><span ne="0.6250910983737814">Added</span><span> </span><span ne="0.7617945310036929">or</span><span> EntityState</span><span ne="0.22226645032182546">.</span><span>Modified</span><span ne="0.010561993109205803">)</span><span ne="0.15764642601764856">;</span><span>
</span>
<span>    </span><span ne="0.4537283050373393">foreach</span><span> </span><span ne="0.3024201875173933">(</span><span ne="0.8642496941932418">var</span><span> entry </span><span ne="0.7058224857441646">in</span><span> modifiedTenantEntries</span><span ne="0.5550613306270528">)</span><span>
</span><span>    </span><span ne="0.40713795054995094">{</span><span>
</span><span>        entry</span><span ne="0.48862834051489823">.</span><span>Entity</span><span ne="0.09803653331693551">.</span><span>TenantId </span><span ne="0.3018014350999124">=</span><span> tenantInfo</span><span ne="0.9796655917402579">.</span><span>TenantId
</span><span>            </span><span ne="0.5063164521602823">??</span><span> </span><span ne="0.7417980195578376">throw</span><span> </span><span ne="0.22307420027385638">new</span><span> </span><span ne="0.5477939884902265">InvalidOperationException</span><span ne="0.4332162799337589">(</span><span ne="0.9615021079536755">$"Tenant id is required but was not provided for entity '</span><span ne="0.014523099925305982">{</span><span id="code-lang-csharp">entry</span><span id="code-lang-csharp">.</span><span id="code-lang-csharp">Entity</span><span id="code-lang-csharp">.</span><span id="code-lang-csharp">GetType</span><span id="code-lang-csharp">(</span><span id="code-lang-csharp">)</span><span ne="0.9334421205303054">}</span><span ne="0.1123455375808724">' with state '</span><span ne="0.6723639563881731">{</span><span id="code-lang-csharp">entry</span><span id="code-lang-csharp">.</span><span id="code-lang-csharp">State</span><span ne="0.17466943635571996">}</span><span ne="0.5601527905068999">'"</span><span ne="0.7440455252920919">)</span><span ne="0.6864638614692322">;</span><span>
</span><span>    </span><span ne="0.14984884466988024">}</span><span>
</span>
<span>    </span><span ne="0.9290103193901316">return</span><span> </span><span ne="0.07291901583418581">await</span><span> </span><span ne="0.3008237716203013">base</span><span ne="0.039787949906283204">.</span><span ne="0.4558927476836748">SaveChangesAsync</span><span ne="0.9151614635409747">(</span><span>cancellationToken</span><span ne="0.20090971283422576">)</span><span ne="0.8452457195467012">;</span><span>
</span><span></span><span ne="0.8238252671045841">}</span></code></p>
```

We iterate over a list of tenant entities and automatically set the `TenantId` property. If a tenant identifier is not available for any reason - an exception is thrown and the operation is aborted. A tenant identifier is required to be set whenever we create, update or delete an entity.

Now let's explore multitenancy in action.

## Adding Tenant Identifier to User Claims on a Login

When a user logs in, we need to use an `IgnoreQueryFilters` method to be able to search for a user in every tenant:

```
<p><code id="code-lang-csharp"><span ne="0.11286298372745962">public</span><span> </span><span ne="0.6084813773852795">class</span><span> </span><span ne="0.8658748094608353">LoginUserEndpoint</span><span> </span><span ne="0.18178067813393983">:</span><span> </span><span ne="0.4438966166095034">ICarterModule</span><span>
</span><span></span><span ne="0.7260952035274122">{</span><span>
</span><span>    </span><span ne="0.03981156883915671">public</span><span> </span><span ne="0.412670173516011">void</span><span> </span><span ne="0.23373774823967985">AddRoutes</span><span ne="0.5420477528453063">(</span><span ne="0.06389576732921054">IEndpointRouteBuilder</span><span> app</span><span ne="0.9109506430519486">)</span><span>
</span><span>    </span><span ne="0.4668650722376412">{</span><span>
</span><span>        app</span><span ne="0.45086967100366593">.</span><span ne="0.6100417592384406">MapPost</span><span ne="0.07386017870302697">(</span><span ne="0.8142096003743997">"/api/users/login"</span><span ne="0.5354823957056771">,</span><span> Handle</span><span ne="0.9065726343118766">)</span><span ne="0.3762266642009958">;</span><span>
</span><span>    </span><span ne="0.9978432018390477">}</span><span>
</span>
<span>    </span><span ne="0.09594935280298811">private</span><span> </span><span ne="0.6857789475524441">static</span><span> </span><span ne="0.023596369234186065">async</span><span> </span><span ne="0.7029318932733312">Task</span><span ne="0.7722399656541509">&lt;</span><span ne="0.034681762055158716">IResult</span><span ne="0.37658540655111306">&gt;</span><span> </span><span ne="0.9174941340791405">Handle</span><span ne="0.9929447602036153">(</span><span>
</span><span>        </span><span ne="0.1359091683352206">[</span><span ne="0.20150709450697124">FromBody</span><span ne="0.4696068338873327">]</span><span> </span><span ne="0.6230505785314815">LoginUserRequest</span><span> request</span><span ne="0.1980864295168311">,</span><span>
</span><span>        </span><span ne="0.37795815430273216">ApplicationDbContext</span><span> context</span><span ne="0.3613803489400097">,</span><span>
</span><span>        </span><span ne="0.009477476931065598">IOptions</span><span ne="0.9683354617195956">&lt;</span><span ne="0.5194457425396356">AuthConfiguration</span><span ne="0.5949813366012148">&gt;</span><span> jwtSettingsOptions</span><span ne="0.22515813544968932">,</span><span>
</span><span>        </span><span ne="0.9581620524612477">CancellationToken</span><span> cancellationToken</span><span ne="0.09574302725656947">)</span><span>
</span><span>    </span><span ne="0.9892705513078606">{</span><span>
</span><span>        </span><span ne="0.5995499837887721">var</span><span> user </span><span ne="0.20439711214244716">=</span><span> </span><span ne="0.8488228863050679">await</span><span> context</span><span ne="0.8994065541732543">.</span><span>Users
</span><span>            </span><span ne="0.45833890799787647">.</span><span ne="0.2850397416246463">IgnoreQueryFilters</span><span ne="0.018776129765643357">(</span><span ne="0.4579088709479976">)</span><span>
</span><span>            </span><span ne="0.4982953138668894">.</span><span ne="0.2171747745120126">FirstOrDefaultAsync</span><span ne="0.5008457352498985">(</span><span>u </span><span ne="0.484680902010579">=&gt;</span><span> u</span><span ne="0.8220192407179683">.</span><span>Email </span><span ne="0.012953762056676754">==</span><span> request</span><span ne="0.4021809346409827">.</span><span>Email</span><span ne="0.3039463727431665">,</span><span> cancellationToken</span><span ne="0.6004366514027555">)</span><span ne="0.24328564584498724">;</span><span>
</span>
<span>        </span><span ne="0.09138844888618247">if</span><span> </span><span ne="0.6672267975499392">(</span><span>user </span><span ne="0.08318899287468517">is</span><span> </span><span ne="0.6759859787053425">null</span><span ne="0.3605984192562359">)</span><span>
</span><span>        </span><span ne="0.5971568144167495">{</span><span>
</span><span>            </span><span ne="0.47431410002142105">return</span><span> Results</span><span ne="0.5633761085162058">.</span><span ne="0.5689059038611888">NotFound</span><span ne="0.15992523733978015">(</span><span ne="0.48237531066813966">"User not found"</span><span ne="0.24070400248306745">)</span><span ne="0.21415986294823386">;</span><span>
</span><span>        </span><span ne="0.3241407096921757">}</span><span>
</span>
<span>        </span><span ne="0.0816430993558046">var</span><span> token </span><span ne="0.8702959288650828">=</span><span> </span><span ne="0.975493931947571">GenerateJwtToken</span><span ne="0.31138505582760434">(</span><span>user</span><span ne="0.6103184825948866">,</span><span> jwtSettingsOptions</span><span ne="0.8104058639102089">.</span><span>Value</span><span ne="0.39006485816290704">)</span><span ne="0.9721960221868978">;</span><span>
</span><span>        </span><span ne="0.008569185415129077">return</span><span> Results</span><span ne="0.8845614823666661">.</span><span ne="0.34451451545609346">Ok</span><span ne="0.9548354148205322">(</span><span ne="0.7472816733645354">new</span><span> </span><span ne="0.6460454107177089">{</span><span> Token </span><span ne="0.37121570250665514">=</span><span> token </span><span ne="0.13709896153147028">}</span><span ne="0.7028610955842883">)</span><span ne="0.6373976710500012">;</span><span>
</span><span>    </span><span ne="0.2634860666895582">}</span><span>
</span><span></span><span ne="0.4053211843656608">}</span></code></p>
```

This method disables all query filters applied to a `User` entity. After a user is found, you need to add a "tenant-id" claim:

```
<p><code id="code-lang-csharp"><span ne="0.07888570834959407">private</span><span> </span><span ne="0.9348212679006747">static</span><span> </span><span ne="0.8954634807829325">string</span><span> </span><span ne="0.34737900761089513">GenerateJwtToken</span><span ne="0.5973586744172578">(</span><span ne="0.24292421513250262">User</span><span> user</span><span ne="0.9307845035509295">,</span><span> </span><span ne="0.9808630660372526">AuthConfiguration</span><span> auth</span><span ne="0.9094147227675042">)</span><span>
</span><span></span><span ne="0.9743487834465091">{</span><span>
</span><span>    </span><span ne="0.4736473489834351">var</span><span> securityKey </span><span ne="0.45048792607754873">=</span><span> </span><span ne="0.4910735449032383">new</span><span> </span><span ne="0.6963231249973189">SymmetricSecurityKey</span><span ne="0.24120702413752648">(</span><span>Encoding</span><span ne="0.4394818191955683">.</span><span>UTF8</span><span ne="0.6126864933894187">.</span><span ne="0.6622904790026629">GetBytes</span><span ne="0.531611012439001">(</span><span>auth</span><span ne="0.7655467797093856">.</span><span>Key</span><span ne="0.6915152049231305">)</span><span ne="0.0011164484111526596">)</span><span ne="0.4089207471721893">;</span><span>
</span><span>    </span><span ne="0.11144329352780735">var</span><span> credentials </span><span ne="0.38222102522330736">=</span><span> </span><span ne="0.4537757679138972">new</span><span> </span><span ne="0.5256540269525898">SigningCredentials</span><span ne="0.5371141291222371">(</span><span>securityKey</span><span ne="0.6160584076300796">,</span><span> SecurityAlgorithms</span><span ne="0.05478156832475056">.</span><span>HmacSha256</span><span ne="0.87833338389845">)</span><span ne="0.5697669382208763">;</span><span>
</span>
<span>    </span><span ne="0.4362050289564424">var</span><span> claims </span><span ne="0.9314763571712431">=</span><span> </span><span ne="0.42543541510355687">new</span><span ne="0.46559679797639353">[</span><span ne="0.293745360278896">]</span><span>
</span><span>    </span><span ne="0.417395989806834">{</span><span>
</span><span>        </span><span ne="0.48150556110761555">new</span><span> </span><span ne="0.3438342938360317">Claim</span><span ne="0.30397694382177853">(</span><span>JwtRegisteredClaimNames</span><span ne="0.28839712537489415">.</span><span>Sub</span><span ne="0.608425333988259">,</span><span> user</span><span ne="0.2848492390443196">.</span><span>Email</span><span ne="0.7623739317072852">)</span><span ne="0.4527997934128166">,</span><span>
</span><span>        </span><span ne="0.16820315938837627">new</span><span> </span><span ne="0.7791576615248914">Claim</span><span ne="0.25094568030543696">(</span><span ne="0.9573274444221848">"use-id"</span><span ne="0.6409539690989786">,</span><span> user</span><span ne="0.2662767916966948">.</span><span>Id</span><span ne="0.22695861484451874">.</span><span ne="0.404762065647184">ToString</span><span ne="0.5383676252695867">(</span><span ne="0.30156743478503056">)</span><span ne="0.6391855959086054">)</span><span ne="0.3236254138378538">,</span><span>
</span><span>        </span><span ne="0.229778032468674">new</span><span> </span><span ne="0.004498953583812471">Claim</span><span ne="0.7343572725187182">(</span><span ne="0.9393127903230756">"tenant-id"</span><span ne="0.43570214820933273">,</span><span> user</span><span ne="0.050337892299239906">.</span><span>TenantId</span><span ne="0.6885568886894949">?.</span><span ne="0.07361308620296092">ToString</span><span ne="0.9464807877875284">(</span><span ne="0.10457150302818752">)</span><span> </span><span ne="0.7850599100095186">??</span><span> </span><span ne="0.2574402994724373">string</span><span ne="0.08457326757935546">.</span><span>Empty</span><span ne="0.45154279330003544">)</span><span>
</span><span>    </span><span ne="0.2796067156207602">}</span><span ne="0.051592853489942025">;</span><span>
</span>
<span>    </span><span ne="0.7663165957158998">var</span><span> token </span><span ne="0.18759810700479196">=</span><span> </span><span ne="0.5196853210825054">new</span><span> </span><span ne="0.7022872002657418">JwtSecurityToken</span><span ne="0.9148318323190106">(</span><span>
</span><span>        </span><span ne="0.13187966066099233">issuer</span><span ne="0.5388948032738321">:</span><span> auth</span><span ne="0.25301002382690907">.</span><span>Issuer</span><span ne="0.061647627022511475">,</span><span>
</span><span>        </span><span ne="0.9182011652783086">audience</span><span ne="0.6200551979755462">:</span><span> auth</span><span ne="0.8022473733732696">.</span><span>Audience</span><span ne="0.6388107465223435">,</span><span>
</span><span>        </span><span ne="0.6641076528099905">claims</span><span ne="0.6631671936752054">:</span><span> claims</span><span ne="0.40843157995800417">,</span><span>
</span><span>        </span><span ne="0.9122768830296868">expires</span><span ne="0.5264127290697487">:</span><span> DateTime</span><span ne="0.5732436168621442">.</span><span>Now</span><span ne="0.6272287017508142">.</span><span ne="0.3420658430133017">AddMinutes</span><span ne="0.13897968166234653">(</span><span ne="0.021124965111406935">30</span><span ne="0.5421917484117587">)</span><span ne="0.7719914228516017">,</span><span>
</span><span>        </span><span ne="0.7485865283803482">signingCredentials</span><span ne="0.12318365533915354">:</span><span> credentials
</span><span>    </span><span ne="0.47973368824051865">)</span><span ne="0.9188819595088863">;</span><span>
</span>
<span>    </span><span ne="0.6158587646316529">return</span><span> </span><span ne="0.20066927818932634">new</span><span> </span><span ne="0.1757498393021858">JwtSecurityTokenHandler</span><span ne="0.1492503545032876">(</span><span ne="0.7222426486734866">)</span><span ne="0.4147355505228145">.</span><span ne="0.3493019968585548">WriteToken</span><span ne="0.3174305574715921">(</span><span>token</span><span ne="0.0008746661887160112">)</span><span ne="0.1382980878076634">;</span><span>
</span><span></span><span ne="0.10934927716257381">}</span></code></p>
```

Now that the user is logged in, we can start calling other endpoints with a JWT token.

## Implementing API endpoints for a Multitenant Entity

Let's explore a `Create` and `Get By Id` endpoints for a book entity:

```
<p><code id="code-lang-csharp"><span ne="0.425490597448577">public</span><span> </span><span ne="0.36366512709347765">sealed</span><span> </span><span ne="0.20662796733143673">record</span><span> </span><span ne="0.3158377675102948">CreateBookRequest</span><span ne="0.7021012771356164">(</span><span ne="0.9482674004613374">string</span><span> Title</span><span ne="0.1909197053676286">,</span><span> </span><span ne="0.8706803500576308">int</span><span> Year</span><span ne="0.41961644972490986">,</span><span> </span><span ne="0.3018862698565131">Guid</span><span> AuthorId</span><span ne="0.6335384816126809">)</span><span ne="0.2001802895593937">;</span><span>
</span>
<span></span><span ne="0.3656812865471162">public</span><span> </span><span ne="0.20621540116899684">class</span><span> </span><span ne="0.40469492171157395">CreateBookEndpoint</span><span> </span><span ne="0.3029336764554331">:</span><span> </span><span ne="0.02833922684558099">ICarterModule</span><span>
</span><span></span><span ne="0.7643057988529484">{</span><span>
</span><span>    </span><span ne="0.5028187433690124">public</span><span> </span><span ne="0.7856105096111784">void</span><span> </span><span ne="0.9199223081329551">AddRoutes</span><span ne="0.35349879616505775">(</span><span ne="0.2491038534441875">IEndpointRouteBuilder</span><span> app</span><span ne="0.247824388858656">)</span><span>
</span><span>    </span><span ne="0.8028777430424244">{</span><span>
</span><span>        app</span><span ne="0.2593669521696156">.</span><span ne="0.4352750183710037">MapPost</span><span ne="0.8118020595261394">(</span><span ne="0.3435663343007931">"/api/books"</span><span ne="0.7216648110349793">,</span><span> Handle</span><span ne="0.9290295367711555">)</span><span ne="0.009981553954130251">;</span><span>
</span><span>    </span><span ne="0.9167792824605118">}</span><span>
</span>
<span>    </span><span ne="0.6576773654939244">private</span><span> </span><span ne="0.4360241045892511">static</span><span> </span><span ne="0.5299644770155881">async</span><span> </span><span ne="0.36101051623675506">Task</span><span ne="0.8543114897483327">&lt;</span><span ne="0.08265534300734667">IResult</span><span ne="0.5984786344703894">&gt;</span><span> </span><span ne="0.5608961668490223">Handle</span><span ne="0.69345163648523">(</span><span>
</span><span>        </span><span ne="0.5935357507588587">[</span><span ne="0.2012175283074179">FromBody</span><span ne="0.40495839801717903">]</span><span> </span><span ne="0.528263744893289">CreateBookRequest</span><span> request</span><span ne="0.8362344681693338">,</span><span>
</span><span>        </span><span ne="0.34052456006344545">ApplicationDbContext</span><span> context</span><span ne="0.3346675504375435">,</span><span>
</span><span>        </span><span ne="0.6021402296609172">CancellationToken</span><span> cancellationToken</span><span ne="0.03477341465096617">)</span><span>
</span><span>    </span><span ne="0.6234347535417583">{</span><span>
</span><span>        </span><span ne="0.21867715458363957">var</span><span> author </span><span ne="0.23221188042822416">=</span><span> </span><span ne="0.7640423546859333">await</span><span> context</span><span ne="0.6021473469911389">.</span><span>Authors</span><span ne="0.25629583193887073">.</span><span ne="0.8519493937920045">FindAsync</span><span ne="0.3571832779762073">(</span><span ne="0.29374901292595923">[</span><span ne="0.8657024493757729">request</span><span ne="0.8249836878118663">.</span><span ne="0.6982741961196148">AuthorId</span><span ne="0.0021696801113515463">]</span><span ne="0.3280418516496042">,</span><span> cancellationToken</span><span ne="0.5493761151292071">)</span><span ne="0.913470412837749">;</span><span>
</span><span>        </span><span ne="0.3844464297325305">if</span><span> </span><span ne="0.34695094102505397">(</span><span>author </span><span ne="0.18298030157544953">is</span><span> </span><span ne="0.5356076876572787">null</span><span ne="0.2686953704343428">)</span><span>
</span><span>        </span><span ne="0.8757176381622518">{</span><span>
</span><span>            </span><span ne="0.14684449876077">return</span><span> Results</span><span ne="0.5905965808037448">.</span><span ne="0.6069751416908805">BadRequest</span><span ne="0.767772758180707">(</span><span ne="0.8283989803601695">"Author not found"</span><span ne="0.7407997763233651">)</span><span ne="0.5182462919078288">;</span><span>
</span><span>        </span><span ne="0.6721198061110532">}</span><span>
</span>
<span>        </span><span ne="0.6361993025785307">var</span><span> book </span><span ne="0.5806289807396806">=</span><span> </span><span ne="0.36718421220984254">new</span><span> </span><span ne="0.6307733543834034">Book</span><span>
</span><span>        </span><span ne="0.10651137865990812">{</span><span>
</span><span>            Id </span><span ne="0.647648279537642">=</span><span> Guid</span><span ne="0.08655019173627654">.</span><span ne="0.6956737826304792">NewGuid</span><span ne="0.8321565205192211">(</span><span ne="0.09445212551225435">)</span><span ne="0.6361849829469598">,</span><span>
</span><span>            Title </span><span ne="0.9178078395126144">=</span><span> request</span><span ne="0.6401033518751122">.</span><span>Title</span><span ne="0.645341949635544">,</span><span>
</span><span>            Year </span><span ne="0.3124082440206615">=</span><span> request</span><span ne="0.3838444224881167">.</span><span>Year</span><span ne="0.439937200356065">,</span><span>
</span><span>            AuthorId </span><span ne="0.47940383365502826">=</span><span> request</span><span ne="0.666673388548671">.</span><span>AuthorId</span><span ne="0.43886133023983454">,</span><span>
</span><span>            Author </span><span ne="0.13745289859858068">=</span><span> author
</span><span>        </span><span ne="0.7535517337283114">}</span><span ne="0.9407584967050833">;</span><span>
</span>
<span>        context</span><span ne="0.007627868003900695">.</span><span>Books</span><span ne="0.0841352812420959">.</span><span ne="0.7741601528823117">Add</span><span ne="0.07462406501985874">(</span><span>book</span><span ne="0.0528019718315037">)</span><span ne="0.29304746799580517">;</span><span>
</span><span>        </span><span ne="0.5816234372119966">await</span><span> context</span><span ne="0.4034269013347517">.</span><span ne="0.3232787699879608">SaveChangesAsync</span><span ne="0.7213121153839379">(</span><span>cancellationToken</span><span ne="0.6552444064862063">)</span><span ne="0.9861285553399008">;</span><span>
</span>
<span>        </span><span ne="0.7902319776250262">var</span><span> response </span><span ne="0.04264094411029051">=</span><span> </span><span ne="0.0797984398885434">new</span><span> </span><span ne="0.06291378224749622">BookResponse</span><span ne="0.5474672130841416">(</span><span>book</span><span ne="0.7779136558261047">.</span><span>Id</span><span ne="0.4009142134489363">,</span><span> book</span><span ne="0.7071122026574682">.</span><span>Title</span><span ne="0.08844432468184504">,</span><span> book</span><span ne="0.12505215575627515">.</span><span>Year</span><span ne="0.05281272303929274">,</span><span> book</span><span ne="0.5759573872049856">.</span><span>AuthorId</span><span ne="0.6974564997801597">)</span><span ne="0.4959677900385293">;</span><span>
</span><span>        </span><span ne="0.9074764325476904">return</span><span> Results</span><span ne="0.4732875476220618">.</span><span ne="0.3333765042044582">Created</span><span ne="0.13006355174953232">(</span><span ne="0.9687895249796633">$"/api/books/</span><span ne="0.3815408022165018">{</span><span id="code-lang-csharp">book</span><span id="code-lang-csharp">.</span><span id="code-lang-csharp">Id</span><span ne="0.7541604647266903">}</span><span ne="0.006076001369309747">"</span><span ne="0.3813625281266625">,</span><span> response</span><span ne="0.542194267031381">)</span><span ne="0.4958431224843125">;</span><span>
</span><span>    </span><span ne="0.6474174641188157">}</span><span>
</span><span></span><span ne="0.9365033157745755">}</span></code></p>
```

```
<p><code id="code-lang-csharp"><span ne="0.09843349608854168">public</span><span> </span><span ne="0.21554297357243657">class</span><span> </span><span ne="0.18692147814205384">GetBookByIdEndpoint</span><span> </span><span ne="0.9567799680679376">:</span><span> </span><span ne="0.965082219426511">ICarterModule</span><span>
</span><span></span><span ne="0.2759198652275935">{</span><span>
</span><span>    </span><span ne="0.2281736903676017">public</span><span> </span><span ne="0.903716767501262">void</span><span> </span><span ne="0.5548420339948886">AddRoutes</span><span ne="0.1301744669297239">(</span><span ne="0.003467466116932716">IEndpointRouteBuilder</span><span> app</span><span ne="0.7307958439431435">)</span><span>
</span><span>    </span><span ne="0.28982136420293747">{</span><span>
</span><span>        app</span><span ne="0.0005812575159003242">.</span><span>MapGet</span><span ne="0.06572191173597719">(</span><span>"/api/books/{id}"</span><span ne="0.5316583630337426">,</span><span> Handle</span><span ne="0.9067929316847563">)</span><span ne="0.3331865686260683">;</span><span>
</span><span>    </span><span ne="0.4988068030815186">}</span><span>
</span>
<span>    </span><span>private</span><span> </span><span>static</span><span> </span><span>async</span><span> </span><span>Task</span><span ne="0.15557003634079802">&lt;</span><span>IResult</span><span ne="0.6792606066566456">&gt;</span><span> </span><span>Handle</span><span ne="0.347546317992932">(</span><span>
</span><span>        </span><span ne="0.0671305526989493">[</span><span>FromRoute</span><span ne="0.02654925692415666">]</span><span> </span><span>Guid</span><span> id</span><span ne="0.5982391306945496">,</span><span>
</span><span>        </span><span>ApplicationDbContext</span><span> context</span><span ne="0.19618745792244163">,</span><span>
</span><span>        </span><span>CancellationToken</span><span> cancellationToken</span><span ne="0.762417722586172">)</span><span>
</span><span>    </span><span ne="0.6435422104183288">{</span><span>
</span><span>        </span><span>var</span><span> book </span><span>=</span><span> </span><span>await</span><span> context</span><span ne="0.41282082266925724">.</span><span>Books
</span><span>            </span><span ne="0.4003911817305936">.</span><span>Include</span><span ne="0.2179839875959907">(</span><span>b </span><span>=&gt;</span><span> b</span><span ne="0.061698242335475495">.</span><span>Author</span><span ne="0.35464112591471086">)</span><span>
</span><span>            </span><span ne="0.4985294540478884">.</span><span>FirstOrDefaultAsync</span><span ne="0.8926024147511359">(</span><span>b </span><span>=&gt;</span><span> b</span><span ne="0.2997443488028594">.</span><span>Id </span><span>==</span><span> id</span><span ne="0.07156511882180416">,</span><span> cancellationToken</span><span ne="0.6970323233954789">)</span><span ne="0.15286785690235838">;</span><span>
</span>
<span>        </span><span>if</span><span> </span><span ne="0.2384241411272906">(</span><span>book </span><span>is</span><span> </span><span>null</span><span ne="0.7484380778381169">)</span><span>
</span><span>        </span><span ne="0.06834823821550873">{</span><span>
</span><span>            </span><span>return</span><span> Results</span><span ne="0.17448133337255534">.</span><span>NotFound</span><span ne="0.8534618502779739">(</span><span ne="0.9298775311812736">)</span><span ne="0.44209209334239186">;</span><span>
</span><span>        </span><span ne="0.6262363490856109">}</span><span>
</span>
<span>        </span><span>var</span><span> response </span><span>=</span><span> </span><span>new</span><span> </span><span>BookResponse</span><span ne="0.7846154093878277">(</span><span>book</span><span ne="0.19549934310181916">.</span><span>Id</span><span ne="0.8537236602813865">,</span><span> book</span><span ne="0.40444285377539024">.</span><span>Title</span><span ne="0.9941325501915035">,</span><span> book</span><span ne="0.3349982258893417">.</span><span>Year</span><span ne="0.7004493591047868">,</span><span> book</span><span ne="0.45891077253607127">.</span><span>AuthorId</span><span ne="0.28511769270438236">)</span><span ne="0.754299639083094">;</span><span>
</span><span>        </span><span>return</span><span> Results</span><span ne="0.22123476177180568">.</span><span>Ok</span><span ne="0.5195353611982845">(</span><span>response</span><span ne="0.777120290010484">)</span><span ne="0.2799583693747948">;</span><span>
</span><span>    </span><span ne="0.4453283489479648">}</span><span>
</span><span></span><span ne="0.9759453295223802">}</span></code></p>
```

As you may have expected, with code doesn't know anything about Tenants. And it is what we were striving for — to create a secure implementation that will now allow customers to interact with another customer's data. Without a need to worry about tenants in each database call.

When creating a book, we check if an Author exists in the database by a provided `AuthorId` in the request. And EF Core makes sure that we can't add a Book using an Author from another tenant. Amazing!

In some applications a user can have access to multiple tenants, for example, a "super-admin" user that can manage entities for different tenants. In such a case we need to send "X-TenantId" header in each request from the frontend (or another application) whenever we need to retrieve or modify data.

If you have such a case, you can modify your `TenantProvider` as follows:

```
<p><code id="code-lang-csharp"><span>public</span><span> </span><span>class</span><span> </span><span>TenantProvider</span><span> </span><span ne="0.3746147146680694">:</span><span> </span><span>ITenantProvider</span><span>
</span><span></span><span ne="0.3673228681002">{</span><span>
</span><span>    </span><span>private</span><span> </span><span>readonly</span><span> </span><span>TenantInfo</span><span> _tenantInfo</span><span ne="0.39941983282552074">;</span><span>
</span>
<span>    </span><span>public</span><span> </span><span>TenantProvider</span><span ne="0.057553078490737986">(</span><span>IHttpContextAccessor</span><span> accessor</span><span ne="0.9884029133179549">)</span><span>
</span><span>    </span><span ne="0.8961918460274243">{</span><span>
</span><span>        </span><span>var</span><span> userIdValue </span><span>=</span><span> accessor</span><span ne="0.20038225276108335">.</span><span>HttpContext</span><span ne="0.3888792645546463">?.</span><span>User</span><span ne="0.5528577404509959">.</span><span>FindFirstValue</span><span ne="0.24405346088994628">(</span><span>"user-id"</span><span ne="0.08603485205893435">)</span><span ne="0.24349762041288858">;</span><span>
</span>
<span>        </span><span>Guid</span><span ne="0.1169537656263212">?</span><span> userId </span><span>=</span><span> Guid</span><span ne="0.08646583991405954">.</span><span>TryParse</span><span ne="0.9625297774224646">(</span><span>userIdValue</span><span ne="0.6268784106679521">,</span><span> </span><span>out</span><span> </span><span>var</span><span> guid</span><span ne="0.4599549936482682">)</span><span> </span><span ne="0.7481073635992382">?</span><span> guid </span><span ne="0.28452247516992657">:</span><span> </span><span>null</span><span ne="0.6412437350908732">;</span><span>
</span><span>        </span><span>Guid</span><span ne="0.2665814947106543">?</span><span> headerTenantId </span><span>=</span><span> </span><span>null</span><span ne="0.4921212931767146">;</span><span>
</span>
<span>        </span><span>if</span><span> </span><span ne="0.1781665181502542">(</span><span>accessor</span><span ne="0.6842862364332151">.</span><span>HttpContext</span><span ne="0.3143471268858704">?.</span><span>Request</span><span ne="0.6214985103844494">.</span><span>Headers</span><span ne="0.6872584077423638">.</span><span>TryGetValue</span><span ne="0.8561433459517611">(</span><span>"X-TenantId"</span><span ne="0.6161570443661234">,</span><span> </span><span>out</span><span> </span><span>var</span><span> headerGuid</span><span ne="0.27694165728058384">)</span><span> </span><span>is</span><span> </span><span>true</span><span ne="0.6185688101745291">)</span><span>
</span><span>        </span><span ne="0.3322160903832263">{</span><span>
</span><span>            headerTenantId </span><span>=</span><span> Guid</span><span ne="0.3776682223981671">.</span><span>Parse</span><span ne="0.31537358701194973">(</span><span>headerGuid</span><span ne="0.3220991354455781">.</span><span>ToString</span><span ne="0.5531569194626256">(</span><span ne="0.5867886887153916">)</span><span ne="0.027754200954534736">)</span><span ne="0.2039360576750472">;</span><span>
</span><span>        </span><span ne="0.6129506452808592">}</span><span>
</span>
<span>        _tenantInfo </span><span>=</span><span> </span><span>new</span><span> </span><span>TenantInfo</span><span ne="0.06732508255493863">(</span><span>userId</span><span ne="0.7074135806454556">,</span><span> headerTenantId</span><span ne="0.6511420023531771">)</span><span ne="0.8230211441873083">;</span><span>
</span><span>    </span><span ne="0.447486165239665">}</span><span>
</span>
<span>    </span><span>public</span><span> </span><span>TenantInfo</span><span> </span><span>GetCurrentTenantInfo</span><span ne="0.46860144650034474">(</span><span ne="0.11523689002228243">)</span><span> </span><span>=&gt;</span><span> _tenantInfo</span><span ne="0.3334967191737438">;</span><span>
</span><span></span><span ne="0.36665380990054075">}</span></code></p>
```

In some applications, it is preferable to always use "X-TenantId" header instead of putting it inside a JWT token. This can also be a case when you use external auth providers that have no idea about tenants.

There are different approaches to solving this problem. I will show you one possible solution with a middleware that checks if a user has access to "X-TenantId". If a user doesn't have access to the requested tenant, a 403 Forbidden response is returned.

```
<p><code id="code-lang-csharp"><span>public</span><span> </span><span>class</span><span> </span><span>TenantCheckerMiddleware</span><span> </span><span ne="0.05319236803349381">:</span><span> </span><span>IMiddleware</span><span>
</span><span></span><span ne="0.6984848143620973">{</span><span>
</span><span>    </span><span>public</span><span> </span><span>async</span><span> </span><span>Task</span><span> </span><span>InvokeAsync</span><span ne="0.8117312717297703">(</span><span>HttpContext</span><span> context</span><span ne="0.34766628034946123">,</span><span> </span><span>RequestDelegate</span><span> next</span><span ne="0.5823910254310495">)</span><span>
</span><span>    </span><span ne="0.21946286606894838">{</span><span>
</span><span>        </span><span>var</span><span> tenantClaimValue </span><span>=</span><span> context</span><span ne="0.9073558177061468">.</span><span>User</span><span ne="0.6580020748450977">.</span><span>Claims</span><span ne="0.8033940259223394">.</span><span>FirstOrDefault</span><span ne="0.7229379251578972">(</span><span>x </span><span>=&gt;</span><span> x</span><span ne="0.6388217020733399">.</span><span>Type</span><span ne="0.09616875742572584">.</span><span>Equals</span><span ne="0.08531340153434619">(</span><span>"tenant-id"</span><span ne="0.39260833420917973">)</span><span ne="0.8792168573754687">)</span><span ne="0.09708841019740233">?.</span><span>Value</span><span ne="0.435220907741139">;</span><span>
</span><span>        </span><span>if</span><span> </span><span ne="0.865014513375673">(</span><span>tenantClaimValue </span><span>is</span><span> </span><span>null</span><span ne="0.5378916541379312">)</span><span>
</span><span>        </span><span ne="0.2550453047886043">{</span><span>
</span><span>            </span><span>await</span><span> </span><span>next</span><span ne="0.5931840385954853">(</span><span>context</span><span ne="0.1860232751898646">)</span><span ne="0.4772675809735044">;</span><span>
</span><span>            </span><span>return</span><span ne="0.5787129111552122">;</span><span>
</span><span>        </span><span ne="0.1169890109344468">}</span><span>
</span>
<span>        </span><span>if</span><span> </span><span ne="0.44415068272773417">(</span><span>!</span><span>context</span><span ne="0.027202417476793417">.</span><span>Request</span><span ne="0.9249021539058027">.</span><span>Headers</span><span ne="0.2499888938908683">.</span><span>TryGetValue</span><span ne="0.6085999351716652">(</span><span>"X-TenantId"</span><span ne="0.6524515166915066">,</span><span> </span><span>out</span><span> </span><span>var</span><span> headerGuid</span><span ne="0.4538559060999623">)</span><span ne="0.3018614791477896">)</span><span>
</span><span>        </span><span ne="0.3763639150135114">{</span><span>
</span><span>            </span><span>await</span><span> </span><span>next</span><span ne="0.4120456298777353">(</span><span>context</span><span ne="0.3452699562788557">)</span><span ne="0.4273002578335794">;</span><span>
</span><span>            </span><span>return</span><span ne="0.5889230537061662">;</span><span>
</span><span>        </span><span ne="0.8134359324413819">}</span><span>
</span>
<span>        </span><span>if</span><span> </span><span ne="0.7201470130336364">(</span><span>tenantClaimValue</span><span ne="0.4518153796903128">.</span><span>Contains</span><span ne="0.8422522677212504">(</span><span>headerGuid</span><span ne="0.8241888837831993">.</span><span>ToString</span><span ne="0.9272378572434654">(</span><span ne="0.4309875154655348">)</span><span ne="0.5216929942974593">,</span><span> StringComparison</span><span ne="0.6802252856938786">.</span><span>Ordinal</span><span ne="0.7363053075096554">)</span><span ne="0.2453325002346317">)</span><span>
</span><span>        </span><span ne="0.15731783721485793">{</span><span>
</span><span>            </span><span>await</span><span> </span><span>next</span><span ne="0.1368798266655784">(</span><span>context</span><span ne="0.22348406281015054">)</span><span ne="0.026101960135499813">;</span><span>
</span><span>            </span><span>return</span><span ne="0.9941231915256172">;</span><span>
</span><span>        </span><span ne="0.5066546766977859">}</span><span>
</span>
<span>        </span><span>var</span><span> problemDetails </span><span>=</span><span> </span><span>new</span><span> </span><span>ProblemDetails</span><span>
</span><span>        </span><span ne="0.8059335581989716">{</span><span>
</span><span>            Status </span><span>=</span><span> StatusCodes</span><span ne="0.5061381824631738">.</span><span>Status403Forbidden</span><span ne="0.3108907939554316">,</span><span>
</span><span>            Title </span><span>=</span><span> </span><span>"Bad Request"</span><span ne="0.9343575393843849">,</span><span>
</span><span>            Detail </span><span>=</span><span> </span><span>"X-TenantId header contains a tenant id that a user doesn't have access to"</span><span>
</span><span>        </span><span ne="0.7721591466268825">}</span><span ne="0.5410854369887425">;</span><span>
</span>
<span>        context</span><span ne="0.8383110285267396">.</span><span>Response</span><span ne="0.35498631326358254">.</span><span>StatusCode </span><span>=</span><span> problemDetails</span><span ne="0.23931428101805674">.</span><span>Status</span><span ne="0.208930054154863">.</span><span>Value</span><span ne="0.4655030365483068">;</span><span>
</span><span>        context</span><span ne="0.5993763036819704">.</span><span>Response</span><span ne="0.8292705091024019">.</span><span>ContentType </span><span>=</span><span> </span><span>"application/problem+json"</span><span ne="0.9932289959393475">;</span><span>
</span>
<span>        </span><span>await</span><span> context</span><span ne="0.41135600360921865">.</span><span>Response</span><span ne="0.12332982225076294">.</span><span>WriteAsJsonAsync</span><span ne="0.570685970022916">(</span><span>problemDetails</span><span ne="0.0546377303363188">)</span><span ne="0.8716537061849985">;</span><span>
</span><span>    </span><span ne="0.5210603884121415">}</span><span>
</span><span></span><span ne="0.7499512311704059">}</span></code></p>
```

In this example, I made a basic check if "X-TenantId" header matches the "tenant-id" from the JWT token. In your case, you might want to check in a database, or even better in a cache.

## Conditional Global Query Filters

Unfortunately, EF Core doesn't support Global Query Filters with conditions, though it is a highly requested feature.

For example, you may want to implement the following query filter that will only be applied when a user has a limited access to tenants. While a "super-admin" user can view all the tenants.

```
<p><code id="code-lang-csharp"><span>if</span><span> </span><span ne="0.5159138185518165">(</span><span>!</span><span>TenantProvider</span><span ne="0.32887031480187745">.</span><span>GetCurrentTenantInfo</span><span ne="0.009788015222813473">(</span><span ne="0.9117964392058039">)</span><span ne="0.2510468181750798">.</span><span>IsSuperAdmin</span><span ne="0.4591073825281189">)</span><span>
</span><span></span><span ne="0.8490121274159332">{</span><span>
</span><span>    builder</span><span ne="0.9608229813911503">.</span><span>Entity</span><span ne="0.8600324320353173">&lt;</span><span>User</span><span ne="0.23036790786519856">&gt;</span><span ne="0.3015172089839805">(</span><span ne="0.3830089670473503">)</span><span>
</span><span>        </span><span ne="0.660035315793493">.</span><span>HasQueryFilter</span><span ne="0.8853389212472688">(</span><span>x </span><span>=&gt;</span><span> x</span><span ne="0.5355548575894019">.</span><span>TenantId</span><span ne="0.02130215558957327">.</span><span>Equals</span><span ne="0.899078418625036">(</span><span>TenantProvider</span><span ne="0.45095021286220127">.</span><span>GetCurrentTenantInfo</span><span ne="0.5818765171260286">(</span><span ne="0.20212111819071354">)</span><span ne="0.6675481859998207">.</span><span>TenantId</span><span ne="0.1676656844613995">)</span><span ne="0.4777705642758897">)</span><span ne="0.4660854525614053">;</span><span>
</span><span></span><span ne="0.6432888105934926">}</span></code></p>
```

If you try to test this application, your filters won't trigger even for a regular user. All because DbContext `OnModelCreating` method is only called once per lifetime of the application — when the first DbContext instance is created.

If you absolutely need to use such Global Query Filters that are applied conditionally depending on each request, you can create a `DynamicModelCacheKeyFactory`:

```
<p><code id="code-lang-csharp"><span>public</span><span> </span><span>class</span><span> </span><span>DynamicModelCacheKeyFactory</span><span> </span><span ne="0.8709631683032019">:</span><span> </span><span>IModelCacheKeyFactory</span><span>
</span><span></span><span ne="0.6278914357629265">{</span><span>
</span><span>    </span><span>public</span><span> </span><span>object</span><span> </span><span>Create</span><span ne="0.7323765480963937">(</span><span>DbContext</span><span> context</span><span ne="0.30204169013256055">,</span><span> </span><span>bool</span><span> designTime</span><span ne="0.6171896942828634">)</span><span>
</span><span>        </span><span>=&gt;</span><span> context </span><span>is</span><span> </span><span>ApplicationDbContext</span><span> dynamicContext
</span><span>            </span><span ne="0.029804448108879056">?</span><span> </span><span ne="0.23087306447874967">(</span><span>context</span><span ne="0.20370114251068594">.</span><span>GetType</span><span ne="0.7467121705835612">(</span><span ne="0.11805314813270185">)</span><span ne="0.8930900421435147">,</span><span> dynamicContext</span><span ne="0.08807884719339432">.</span><span>TenantProvider</span><span ne="0.1638721059392051">.</span><span>GetCurrentTenantInfo</span><span ne="0.7079040455991844">(</span><span ne="0.144313659626772">)</span><span ne="0.6110292736642333">,</span><span> designTime</span><span ne="0.2528791390962293">)</span><span>
</span><span>            </span><span ne="0.7049113999341419">:</span><span> context</span><span ne="0.6682607381861049">.</span><span>GetType</span><span ne="0.3789479128982196">(</span><span ne="0.8523501232891948">)</span><span ne="0.5465841520882084">;</span><span>
</span>    
<span>    </span><span>public</span><span> </span><span>object</span><span> </span><span>Create</span><span ne="0.70755873852948">(</span><span>DbContext</span><span> context</span><span ne="0.24429380906159448">)</span><span>
</span><span>        </span><span>=&gt;</span><span> </span><span>Create</span><span ne="0.6517253133927616">(</span><span>context</span><span ne="0.8028843802547595">,</span><span> </span><span>false</span><span ne="0.40249562838185293">)</span><span ne="0.5003160436549744">;</span><span>
</span><span></span><span ne="0.45926959186818384">}</span></code></p>
```

You need to replace a standard `IModelCacheKeyFactory` with a dynamic one when registering a DbContext:

```
<p><code id="code-lang-csharp"><span>builder</span><span ne="0.9391641744024597">.</span><span>Services</span><span ne="0.43564596868506567">.</span><span>AddDbContext</span><span ne="0.3225155021737459">&lt;</span><span>ApplicationDbContext</span><span ne="0.737846315819291">&gt;</span><span ne="0.8415024546554573">(</span><span ne="0.675463411674777">(</span><span>provider</span><span ne="0.8780829437558362">,</span><span> options</span><span ne="0.7363338398888106">)</span><span> </span><span>=&gt;</span><span>
</span><span></span><span ne="0.3661607513036874">{</span><span>
</span><span>    </span><span>var</span><span> interceptor </span><span>=</span><span> provider</span><span ne="0.5726013722207423">.</span><span>GetRequiredService</span><span ne="0.42256267509901635">&lt;</span><span>AuditableInterceptor</span><span ne="0.664698401732965">&gt;</span><span ne="0.7199111572859225">(</span><span ne="0.1754746728371771">)</span><span ne="0.8321668215491538">;</span><span>
</span>
<span>    options</span><span ne="0.1748720207963257">.</span><span>EnableSensitiveDataLogging</span><span ne="0.9352309809323451">(</span><span ne="0.40238304654092705">)</span><span>
</span><span>        </span><span ne="0.37036846146279523">.</span><span>UseNpgsql</span><span ne="0.9428260068233636">(</span><span>connectionString</span><span ne="0.5930578971157253">,</span><span> npgsqlOptions </span><span>=&gt;</span><span>
</span><span>        </span><span ne="0.05463152167027607">{</span><span>
</span><span>            npgsqlOptions</span><span ne="0.6909501751881769">.</span><span>MigrationsHistoryTable</span><span ne="0.7208168532695407">(</span><span>"__MyMigrationsHistory"</span><span ne="0.7813845576851985">,</span><span> </span><span>"devtips_multitenancy"</span><span ne="0.6560425569732211">)</span><span ne="0.44865347311217185">;</span><span>
</span><span>        </span><span ne="0.3693952018954152">}</span><span ne="0.25522976234232264">)</span><span>
</span><span>        </span><span ne="0.9080564937039513">.</span><span>AddInterceptors</span><span ne="0.6953724749098857">(</span><span>interceptor</span><span ne="0.04842309191159">)</span><span>
</span><span>        </span><span ne="0.5283155708338387">.</span><span>UseSnakeCaseNamingConvention</span><span ne="0.7305261121823832">(</span><span ne="0.12740959070201607">)</span><span ne="0.7478367262162907">;</span><span>
</span>        
<span>    options</span><span ne="0.09545773617074815">.</span><span>ReplaceService</span><span ne="0.0349106415858782">&lt;</span><span>IModelCacheKeyFactory</span><span ne="0.6742847841777106">,</span><span> DynamicModelCacheKeyFactory</span><span ne="0.6800062704837453">&gt;</span><span ne="0.5984459648512456">(</span><span ne="0.1592153459303678">)</span><span ne="0.6745277779920524">;</span><span>
</span><span></span><span ne="0.6580170598390414">}</span><span ne="0.7529976089033829">)</span><span ne="0.02337341629803813">;</span></code></p>
```

This `DynamicModelCacheKeyFactory` tells EF Core not to cache a created model (mapping with query filters) and call `OnModelCreating` method for every instance of DbContext. This ensures that conditional Global Query Filters work, but this approach **severely damages the performance** of each database call within a DbContext. So use this carefully and benchmark your requests.

Hope you find this newsletter useful. See you next time.
