---
url: "https://antondevtips.com/blog/how-to-implement-audit-trail-in-asp-net-core-with-ef-core?utm_source=email&utm_medium=email&utm_campaign=website"
captured_at: "2025-08-11T15:25:14+01:00"
title: "How to Implement Audit Trail in ASP.NET Core with EF Core"
domain: "antondevtips-com"
---

---
In modern web applications, tracking changes to data can be needed for monitoring, compliance, and debugging reasons. This process, known as creating **audit trails**, allows developers to see who made changes, when they were made, and what the changes were. **Audit trails** provide a historical record of changes made to data.

In this blog post, I will show how to implement an audit trail in an ASP.NET Core application using Entity Framework Core (EF Core).

## Application We Will Be Auditing

Today we will implement audit trails for the "Books" application that has the following entities:

-   Books
-   Authors
-   Users

I find it useful to include the following properties in all entities that need to be audited:

```
<p><code id="code-lang-csharp"><span ne="0.48973724963450893">public</span><span> </span><span ne="0.2052201086672244">interface</span><span> </span><span ne="0.24021034904658844">IAuditableEntity</span><span>
</span><span></span><span ne="0.11740731575066343">{</span><span>
</span><span>    </span><span ne="0.23799527007440635">DateTime</span><span> CreatedAtUtc </span><span ne="0.955169124322797">{</span><span> </span><span ne="0.5334564711308699">get</span><span ne="0.33454498610690087">;</span><span> </span><span ne="0.4215093469387152">set</span><span ne="0.8161508374875671">;</span><span> </span><span ne="0.829656042711432">}</span><span>
</span>    
<span>    </span><span ne="0.28654100652514614">DateTime</span><span ne="0.3614904098243734">?</span><span> UpdatedAtUtc </span><span ne="0.2877983754798943">{</span><span> </span><span ne="0.9573925707031962">get</span><span ne="0.4120009524620747">;</span><span> </span><span ne="0.4013606118010379">set</span><span ne="0.8995696039053379">;</span><span> </span><span ne="0.6875214871033297">}</span><span>
</span>    
<span>    </span><span ne="0.9725932606892235">string</span><span> CreatedBy </span><span ne="0.901263796233789">{</span><span> </span><span ne="0.2784670850205626">get</span><span ne="0.15503614443884284">;</span><span> </span><span ne="0.9129670766322528">set</span><span ne="0.2199691502734068">;</span><span> </span><span ne="0.1648956787703535">}</span><span>
</span>
<span>    </span><span ne="0.9933439898595111">string</span><span ne="0.2385484200948791">?</span><span> UpdatedBy </span><span ne="0.9153213489142638">{</span><span> </span><span ne="0.1900758702008032">get</span><span ne="0.5411271293502901">;</span><span> </span><span ne="0.5493858692361454">set</span><span ne="0.298089882640165">;</span><span> </span><span ne="0.7391645293415747">}</span><span>
</span><span></span><span ne="0.5353313053446753">}</span></code></p>
```

We need to inherit all our auditable entities from this interface, for example, User and Book:

```
<p><code id="code-lang-csharp"><span ne="0.7710970777732012">public</span><span> </span><span ne="0.490637200526324">class</span><span> </span><span ne="0.3180793419324015">User</span><span> </span><span ne="0.3416980262667144">:</span><span> </span><span ne="0.5084393342578665">IAuditableEntity</span><span>
</span><span></span><span ne="0.0491191505842693">{</span><span>
</span><span>    </span><span ne="0.7713729555435607">public</span><span> </span><span ne="0.32673103037740836">Guid</span><span> Id </span><span ne="0.6574588956528026">{</span><span> </span><span ne="0.5149698567337927">get</span><span ne="0.9552365915553451">;</span><span> </span><span ne="0.6470111599736086">set</span><span ne="0.7172837161243905">;</span><span> </span><span ne="0.8489859822484639">}</span><span>
</span><span>    </span><span ne="0.06765055406172049">public</span><span> required </span><span ne="0.5872620641832625">string</span><span> Email </span><span ne="0.4525174037860007">{</span><span> </span><span ne="0.18085894438921402">get</span><span ne="0.9205715959647792">;</span><span> </span><span ne="0.38496732606874673">set</span><span ne="0.35968944635247047">;</span><span> </span><span ne="0.7857523553998663">}</span><span>
</span>    
<span>    </span><span ne="0.08445156512332508">public</span><span> </span><span ne="0.706108825769734">DateTime</span><span> CreatedAtUtc </span><span ne="0.22440703783920324">{</span><span> </span><span ne="0.5255893930034838">get</span><span ne="0.598550487977827">;</span><span> </span><span ne="0.4576943153749736">set</span><span ne="0.15172130177827026">;</span><span> </span><span ne="0.006707399316634333">}</span><span>
</span><span>    </span><span ne="0.6675596511772112">public</span><span> </span><span ne="0.08183605052898357">DateTime</span><span ne="0.1693548021037532">?</span><span> UpdatedAtUtc </span><span ne="0.07046582964423753">{</span><span> </span><span ne="0.06293869402193242">get</span><span ne="0.9367490814148554">;</span><span> </span><span ne="0.5289607831268389">set</span><span ne="0.8071317912045641">;</span><span> </span><span ne="0.37640336212110836">}</span><span>
</span><span>    </span><span ne="0.9858289426045055">public</span><span> </span><span ne="0.1878711535772567">string</span><span> CreatedBy </span><span ne="0.6183220374837637">{</span><span> </span><span ne="0.4113171976632609">get</span><span ne="0.14909658964265649">;</span><span> </span><span ne="0.6580106707437218">set</span><span ne="0.5996743598470122">;</span><span> </span><span ne="0.2200506366681413">}</span><span> </span><span ne="0.6355849552461904">=</span><span> </span><span ne="0.3676640965514648">null</span><span ne="0.25831064513899704">!</span><span ne="0.6279720072996728">;</span><span>
</span><span>    </span><span ne="0.1244851792243612">public</span><span> </span><span ne="0.9739124652690181">string</span><span ne="0.8521201921161883">?</span><span> UpdatedBy </span><span ne="0.17297009687481635">{</span><span> </span><span ne="0.41804962200157947">get</span><span ne="0.13372466915635584">;</span><span> </span><span ne="0.098714617118141">set</span><span ne="0.9075121759355226">;</span><span> </span><span ne="0.9349459582909612">}</span><span>
</span><span></span><span ne="0.5620507639407972">}</span><span>
</span>
<span></span><span ne="0.4520861510368275">public</span><span> </span><span ne="0.7646301662254904">class</span><span> </span><span ne="0.8774159329971872">Book</span><span> </span><span ne="0.6751913784018394">:</span><span> </span><span ne="0.5404765562178288">IAuditableEntity</span><span>
</span><span></span><span ne="0.967300394832297">{</span><span>
</span><span>    </span><span ne="0.3796583725812458">public</span><span> required </span><span ne="0.6895319782929566">Guid</span><span> Id </span><span ne="0.4667505230853799">{</span><span> </span><span ne="0.9291745853832445">get</span><span ne="0.7646552636801617">;</span><span> </span><span ne="0.27314343981609324">set</span><span ne="0.6529076190639286">;</span><span> </span><span ne="0.7540133771903021">}</span><span>
</span><span>    </span><span ne="0.6747900424501183">public</span><span> required </span><span ne="0.27652924629873044">string</span><span> Title </span><span ne="0.17844644726830583">{</span><span> </span><span ne="0.4871046241722369">get</span><span ne="0.35410627259884764">;</span><span> </span><span ne="0.8950184739864671">set</span><span ne="0.22022513272629107">;</span><span> </span><span ne="0.06509774291059833">}</span><span>
</span><span>    </span><span ne="0.2820154699589118">public</span><span> required </span><span ne="0.41860597737018834">int</span><span> Year </span><span ne="0.8793045030045017">{</span><span> </span><span ne="0.1949024173786421">get</span><span ne="0.7222395284714979">;</span><span> </span><span ne="0.0008340493865489629">set</span><span ne="0.9383101061895509">;</span><span> </span><span ne="0.5407978010484418">}</span><span>
</span><span>    </span><span ne="0.7854979011518681">public</span><span> </span><span ne="0.828051730792603">Guid</span><span> AuthorId </span><span ne="0.5034252380226727">{</span><span> </span><span ne="0.2546036079433611">get</span><span ne="0.10238815129532397">;</span><span> </span><span ne="0.12330914776750024">set</span><span ne="0.7287820727931302">;</span><span> </span><span ne="0.709450970043109">}</span><span>
</span><span>    </span><span ne="0.5567642103553517">public</span><span> </span><span ne="0.9623342225673807">Author</span><span> Author </span><span ne="0.7783999183644874">{</span><span> </span><span ne="0.3371314941980622">get</span><span ne="0.5812450526716699">;</span><span> </span><span ne="0.5781532472831271">set</span><span ne="0.04526845744079144">;</span><span> </span><span ne="0.9721613412349378">}</span><span> </span><span ne="0.049294502027328546">=</span><span> </span><span ne="0.22770431924830026">null</span><span ne="0.5930232857607779">!</span><span ne="0.18751272712241285">;</span><span>
</span>    
<span>    </span><span ne="0.6202673327735518">public</span><span> </span><span ne="0.5955430926420057">DateTime</span><span> CreatedAtUtc </span><span ne="0.4814593436309046">{</span><span> </span><span ne="0.9767173684993938">get</span><span ne="0.6706172083168739">;</span><span> </span><span ne="0.08264081394129663">set</span><span ne="0.5339183026295322">;</span><span> </span><span ne="0.5633692383920114">}</span><span>
</span><span>    </span><span ne="0.42764255609029">public</span><span> </span><span ne="0.9264837979741968">DateTime</span><span ne="0.44075303164406">?</span><span> UpdatedAtUtc </span><span ne="0.9334083861293561">{</span><span> </span><span ne="0.8904788940060188">get</span><span ne="0.07795900750303264">;</span><span> </span><span ne="0.20276968933134842">set</span><span ne="0.8318321155806317">;</span><span> </span><span ne="0.5930982898921189">}</span><span>
</span><span>    </span><span ne="0.9520462369398812">public</span><span> </span><span ne="0.75833768068493">string</span><span> CreatedBy </span><span ne="0.20847814831593547">{</span><span> </span><span ne="0.5022239278957548">get</span><span ne="0.7197464829269474">;</span><span> </span><span ne="0.1308929736060529">set</span><span ne="0.6828289198787888">;</span><span> </span><span ne="0.7472097472155376">}</span><span> </span><span ne="0.7093281741376607">=</span><span> </span><span ne="0.8296149788871796">null</span><span ne="0.6486925817583046">!</span><span ne="0.8236568883874503">;</span><span>
</span><span>    </span><span ne="0.9992148707637083">public</span><span> </span><span ne="0.8445720253093171">string</span><span ne="0.6710734098911618">?</span><span> UpdatedBy </span><span ne="0.6314017589682883">{</span><span> </span><span ne="0.5233858544525072">get</span><span ne="0.279222643504651">;</span><span> </span><span ne="0.45652333460334127">set</span><span ne="0.4192560378224307">;</span><span> </span><span ne="0.7943476324238947">}</span><span>
</span><span></span><span ne="0.5428743562506547">}</span></code></p>
```

Now we have a few options, we can implement **audit trails** manually for each entity or have one implementation that automatically applies to all the entities. In this blog post, I will show you the second option, as it is more robust and easier to maintain.

## Configuring Audit Trails Entity in EF Core

The first step in implementing an **audit trail** is to create an entity that will store the audit logs in a separate database table. This entity should capture details such as the entity type, primary key, a list of changed properties, old values, new values, and the timestamp of the change.

```
<p><code id="code-lang-csharp"><span ne="0.49556870320948676">public</span><span> </span><span ne="0.6173272919894642">class</span><span> </span><span ne="0.5916488727716772">AuditTrail</span><span>
</span><span></span><span ne="0.9546247897642939">{</span><span>
</span><span>    </span><span ne="0.2937830314704032">public</span><span> required </span><span ne="0.34045403472125413">Guid</span><span> Id </span><span ne="0.985690591851739">{</span><span> </span><span ne="0.309260450532473">get</span><span ne="0.25163916143188936">;</span><span> </span><span ne="0.47851658486745785">set</span><span ne="0.2566388834058029">;</span><span> </span><span ne="0.6502720898138452">}</span><span>
</span>
<span>    </span><span ne="0.8362848926856817">public</span><span> </span><span ne="0.5213259668382265">Guid</span><span ne="0.780072584969355">?</span><span> UserId </span><span ne="0.4939379839786816">{</span><span> </span><span ne="0.893379048319207">get</span><span ne="0.08052702870436579">;</span><span> </span><span ne="0.9008580656669641">set</span><span ne="0.15796962502523515">;</span><span> </span><span ne="0.05543830379056491">}</span><span>
</span>
<span>    </span><span ne="0.20846890769991056">public</span><span> </span><span ne="0.25092241548661454">User</span><span ne="0.3270247531880923">?</span><span> User </span><span ne="0.4388174031931271">{</span><span> </span><span ne="0.5519946994682502">get</span><span ne="0.922052837868284">;</span><span> </span><span ne="0.23790254864355176">set</span><span ne="0.3472034655277152">;</span><span> </span><span ne="0.44956311955911565">}</span><span>
</span>
<span>    </span><span ne="0.2872931919808597">public</span><span> </span><span ne="0.9633995253158771">TrailType</span><span> TrailType </span><span ne="0.09113207302420956">{</span><span> </span><span ne="0.5415107696782581">get</span><span ne="0.10213011429004248">;</span><span> </span><span ne="0.7181997322983376">set</span><span ne="0.06991125484078964">;</span><span> </span><span ne="0.4581096761506832">}</span><span>
</span>
<span>    </span><span ne="0.7660995920343487">public</span><span> </span><span ne="0.5990703351311473">DateTime</span><span> DateUtc </span><span ne="0.10946827784430346">{</span><span> </span><span ne="0.290824487507805">get</span><span ne="0.25717474920146066">;</span><span> </span><span ne="0.8889375092319441">set</span><span ne="0.465794583284762">;</span><span> </span><span ne="0.37100653726196053">}</span><span>
</span>
<span>    </span><span ne="0.08089312866584886">public</span><span> required </span><span ne="0.6451587634009708">string</span><span> EntityName </span><span ne="0.29930453251873756">{</span><span> </span><span ne="0.7454544256614309">get</span><span ne="0.8810093346631537">;</span><span> </span><span ne="0.9427702309359502">set</span><span ne="0.645038489353308">;</span><span> </span><span ne="0.6042425474286987">}</span><span>
</span>
<span>    </span><span ne="0.5921950534109832">public</span><span> </span><span ne="0.6794809895828023">string</span><span ne="0.3114630506361825">?</span><span> PrimaryKey </span><span ne="0.09861133069594785">{</span><span> </span><span ne="0.6028001968105343">get</span><span ne="0.6722750638591732">;</span><span> </span><span ne="0.08434223068471547">set</span><span ne="0.9077852206544778">;</span><span> </span><span ne="0.6461858605378448">}</span><span>
</span>
<span>    </span><span ne="0.29163226656118746">public</span><span> </span><span ne="0.8393953965707374">Dictionary</span><span ne="0.6028202582869573">&lt;</span><span ne="0.8234996874955928">string</span><span ne="0.8437154184860419">,</span><span ne="0.8109221856171515"> </span><span ne="0.93584327779951">object</span><span ne="0.15369789812995038">?</span><span ne="0.45498782623218637">&gt;</span><span> OldValues </span><span ne="0.14625089909930533">{</span><span> </span><span ne="0.7098962912110287">get</span><span ne="0.6188866865810848">;</span><span> </span><span ne="0.5205734813230684">set</span><span ne="0.06095584692498113">;</span><span> </span><span ne="0.2321153481574878">}</span><span> </span><span ne="0.33733369566413285">=</span><span> </span><span ne="0.7445544648983383">[</span><span ne="0.9982054803891769">]</span><span ne="0.8361885058714653">;</span><span>
</span>
<span>    </span><span ne="0.37163255810754203">public</span><span> </span><span ne="0.38194244073563477">Dictionary</span><span ne="0.7882460208211262">&lt;</span><span ne="0.99693075127794">string</span><span ne="0.17556884286765728">,</span><span ne="0.596866205887116"> </span><span ne="0.5412597454098886">object</span><span ne="0.8943453692955793">?</span><span ne="0.04251029438579901">&gt;</span><span> NewValues </span><span ne="0.1647116859546257">{</span><span> </span><span ne="0.8348788286987063">get</span><span ne="0.5229478651099753">;</span><span> </span><span ne="0.1443251985717806">set</span><span ne="0.1808596261433031">;</span><span> </span><span ne="0.46966884456806335">}</span><span> </span><span ne="0.23022244807588488">=</span><span> </span><span ne="0.745156634923378">[</span><span ne="0.9154525011069373">]</span><span ne="0.4580036558438517">;</span><span>
</span>
<span>    </span><span ne="0.7063670213012597">public</span><span> </span><span ne="0.0029402662123990675">List</span><span ne="0.1537353658347823">&lt;</span><span ne="0.21467727872798992">string</span><span ne="0.7954639912480219">&gt;</span><span> ChangedColumns </span><span ne="0.7861867126690233">{</span><span> </span><span ne="0.8585061485034741">get</span><span ne="0.43943195912029054">;</span><span> </span><span ne="0.8780924074613166">set</span><span ne="0.7025265744405276">;</span><span> </span><span ne="0.33376295438080295">}</span><span> </span><span ne="0.45229594901288783">=</span><span> </span><span ne="0.24230573730615235">[</span><span ne="0.9394108779011682">]</span><span ne="0.5702105013255279">;</span><span>
</span><span></span><span ne="0.649056766030859">}</span></code></p>
```

Here we have a reference to a `User` entity. Depending on your application needs, you may have this reference or not.

Every audit trail can be of the following types:

-   Entity was created
-   Entity was updated
-   Entity was deleted

```
<p><code id="code-lang-csharp"><span ne="0.02469572440355483">public</span><span> </span><span ne="0.40531587475099107">enum</span><span> </span><span ne="0.4817620640465109">TrailType</span><span> </span><span ne="0.7990286144754889">:</span><span> </span><span ne="0.222617774586494">byte</span><span>
</span><span></span><span ne="0.6269310719417513">{</span><span>
</span><span>    None </span><span ne="0.8893546983896995">=</span><span> </span><span ne="0.9308519543285402">0</span><span ne="0.854868973683854">,</span><span>
</span><span>    Create </span><span ne="0.3942182311138368">=</span><span> </span><span ne="0.2834512683679091">1</span><span ne="0.5297737108653418">,</span><span>
</span><span>    Update </span><span ne="0.3798794450326265">=</span><span> </span><span ne="0.6538421137254189">2</span><span ne="0.6181844188958334">,</span><span>
</span><span>    Delete </span><span ne="0.7119167179974225">=</span><span> </span><span ne="0.8266250129612233">3</span><span>
</span><span></span><span ne="0.6950479336970822">}</span></code></p>
```

Let's have a look at how to configure an audit trail entity in EF Core:

```
<p><code id="code-lang-csharp"><span ne="0.40354513820463167">public</span><span> </span><span ne="0.4986830430105831">class</span><span> </span><span ne="0.8407522215794581">AuditTrailConfiguration</span><span> </span><span ne="0.10878408344873425">:</span><span> </span><span ne="0.14887440089713444">IEntityTypeConfiguration</span><span ne="0.7334935090106101">&lt;</span><span ne="0.9068949052598745">AuditTrail</span><span ne="0.5037840758028798">&gt;</span><span>
</span><span></span><span ne="0.6841235850358902">{</span><span>
</span><span>    </span><span ne="0.32875353550863795">public</span><span> </span><span ne="0.0004566025404304508">void</span><span> </span><span ne="0.3919304834589207">Configure</span><span ne="0.6698207280934385">(</span><span ne="0.25347273824276895">EntityTypeBuilder</span><span ne="0.06743098287697114">&lt;</span><span ne="0.1529326806247221">AuditTrail</span><span ne="0.7141610444112425">&gt;</span><span> builder</span><span ne="0.7012939546697935">)</span><span>
</span><span>    </span><span ne="0.6458395272766064">{</span><span>
</span><span>        builder</span><span ne="0.14869012720959274">.</span><span ne="0.15436551461180692">ToTable</span><span ne="0.6567118369770729">(</span><span ne="0.1801638590693041">"audit_trails"</span><span ne="0.26138005261464414">)</span><span ne="0.7860618996431219">;</span><span>
</span><span>        builder</span><span ne="0.6995142962578914">.</span><span ne="0.13482190229161517">HasKey</span><span ne="0.538009399349469">(</span><span>e </span><span ne="0.7244843575173642">=&gt;</span><span> e</span><span ne="0.7219515454351743">.</span><span>Id</span><span ne="0.5804823217646287">)</span><span ne="0.28712086649371227">;</span><span>
</span>
<span>        builder</span><span ne="0.41536292029180144">.</span><span ne="0.3306268254236081">HasIndex</span><span ne="0.28244083170263323">(</span><span>e </span><span ne="0.4313637245368449">=&gt;</span><span> e</span><span ne="0.378841550498465">.</span><span>EntityName</span><span ne="0.36327188661879695">)</span><span ne="0.2722255558258875">;</span><span>
</span>
<span>        builder</span><span ne="0.9563574705319656">.</span><span ne="0.5619909581753847">Property</span><span ne="0.489822959538431">(</span><span>e </span><span ne="0.14195580654317352">=&gt;</span><span> e</span><span ne="0.07399208623928422">.</span><span>Id</span><span ne="0.29719235166128855">)</span><span ne="0.15032690507831326">;</span><span>
</span>
<span>        builder</span><span ne="0.2459417799081507">.</span><span ne="0.12306473555685316">Property</span><span ne="0.1442796273083118">(</span><span>e </span><span ne="0.44159890862401796">=&gt;</span><span> e</span><span ne="0.9145557806947888">.</span><span>UserId</span><span ne="0.009159898661858956">)</span><span ne="0.3849620274062695">;</span><span>
</span><span>        builder</span><span ne="0.18121389238634134">.</span><span ne="0.5596848610081954">Property</span><span ne="0.28935349312794734">(</span><span>e </span><span ne="0.1542305426274143">=&gt;</span><span> e</span><span ne="0.8918445707400176">.</span><span>EntityName</span><span ne="0.04188473750466892">)</span><span ne="0.2630370471761865">.</span><span ne="0.2968347807370353">HasMaxLength</span><span ne="0.3516284320119696">(</span><span ne="0.2552522827991641">100</span><span ne="0.9036625614468664">)</span><span ne="0.8395470882513764">.</span><span ne="0.3031159991293635">IsRequired</span><span ne="0.6045209967907722">(</span><span ne="0.0889423316869441">)</span><span ne="0.9836818537875944">;</span><span>
</span><span>        builder</span><span ne="0.258889995196268">.</span><span ne="0.495779102449073">Property</span><span ne="0.9460118169545807">(</span><span>e </span><span ne="0.8792842101697153">=&gt;</span><span> e</span><span ne="0.14731652562767938">.</span><span>DateUtc</span><span ne="0.9579528731543422">)</span><span ne="0.5451626009403414">.</span><span ne="0.08823878838810051">IsRequired</span><span ne="0.07086305906622181">(</span><span ne="0.24870641809076188">)</span><span ne="0.9270996753354898">;</span><span>
</span><span>        builder</span><span ne="0.9615651540590715">.</span><span ne="0.35434053179978164">Property</span><span ne="0.824210618390224">(</span><span>e </span><span ne="0.45706177914841706">=&gt;</span><span> e</span><span ne="0.2090703329666158">.</span><span>PrimaryKey</span><span ne="0.7829900006921545">)</span><span ne="0.46369475650754755">.</span><span ne="0.6445447883535356">HasMaxLength</span><span ne="0.6396402257843338">(</span><span ne="0.7728643718564493">100</span><span ne="0.5312817529952214">)</span><span ne="0.8073465698748002">;</span><span>
</span>
<span>        builder</span><span ne="0.011187942904616999">.</span><span ne="0.12085123636251927">Property</span><span ne="0.45260795935801934">(</span><span>e </span><span ne="0.49949379509290803">=&gt;</span><span> e</span><span ne="0.030083115533823812">.</span><span>TrailType</span><span ne="0.6615507440706246">)</span><span ne="0.49131844341122866">.</span><span ne="0.5236036158338416">HasConversion</span><span ne="0.21877740911038457">&lt;</span><span ne="0.09463483018344931">string</span><span ne="0.9314889515243135">&gt;</span><span ne="0.056868177360728356">(</span><span ne="0.8960727479380961">)</span><span ne="0.1762267085553899">;</span><span>
</span>
<span>        builder</span><span ne="0.5453893262437163">.</span><span ne="0.6015781839634332">Property</span><span ne="0.9703877414150727">(</span><span>e </span><span ne="0.7004066550349196">=&gt;</span><span> e</span><span ne="0.914638471703148">.</span><span>ChangedColumns</span><span ne="0.8333486053610891">)</span><span ne="0.1899902894233575">.</span><span ne="0.3277181089466654">HasColumnType</span><span ne="0.9070793454362266">(</span><span ne="0.41106046211191927">"jsonb"</span><span ne="0.9965074246540426">)</span><span ne="0.1951183261663494">;</span><span>
</span><span>        builder</span><span ne="0.5425204355463218">.</span><span ne="0.5061418702700798">Property</span><span ne="0.24746161898679297">(</span><span>e </span><span ne="0.7798940091389718">=&gt;</span><span> e</span><span ne="0.8552438538938784">.</span><span>OldValues</span><span ne="0.22649310358228936">)</span><span ne="0.5137300940870103">.</span><span ne="0.709332092006111">HasColumnType</span><span ne="0.4435527082320472">(</span><span ne="0.3512437027174168">"jsonb"</span><span ne="0.1311532052282296">)</span><span ne="0.7150145653085074">;</span><span>
</span><span>        builder</span><span ne="0.118990842686032">.</span><span ne="0.3103432076883621">Property</span><span ne="0.2602530624185113">(</span><span>e </span><span ne="0.29006796775756305">=&gt;</span><span> e</span><span ne="0.548424341040068">.</span><span>NewValues</span><span ne="0.5031036502650302">)</span><span ne="0.859414555446157">.</span><span ne="0.35769734485940496">HasColumnType</span><span ne="0.9130352103238683">(</span><span ne="0.4248339986672006">"jsonb"</span><span ne="0.7183090550752007">)</span><span ne="0.5869416930333264">;</span><span>
</span>
<span>        builder</span><span ne="0.8756602711682774">.</span><span ne="0.28840534267200313">HasOne</span><span ne="0.17196707167881908">(</span><span>e </span><span ne="0.23535187839233984">=&gt;</span><span> e</span><span ne="0.16705476069400682">.</span><span>User</span><span ne="0.38943283513763194">)</span><span>
</span><span>            </span><span ne="0.8033570669889277">.</span><span ne="0.2175322023855797">WithMany</span><span ne="0.5321388422217317">(</span><span ne="0.29942155312944674">)</span><span>
</span><span>            </span><span ne="0.43169530207401385">.</span><span ne="0.45818384354990194">HasForeignKey</span><span ne="0.8039567395853422">(</span><span>e </span><span ne="0.8086029072208493">=&gt;</span><span> e</span><span ne="0.8595305082161525">.</span><span>UserId</span><span ne="0.7088479570469182">)</span><span>
</span><span>            </span><span ne="0.15326885052794892">.</span><span ne="0.7418034908840042">IsRequired</span><span ne="0.36931297776878136">(</span><span ne="0.9974522619764373">false</span><span ne="0.3809553497442122">)</span><span>
</span><span>            </span><span ne="0.16684592782158425">.</span><span ne="0.6260133049180192">OnDelete</span><span ne="0.9087297486012659">(</span><span>DeleteBehavior</span><span ne="0.21446215591724427">.</span><span>SetNull</span><span ne="0.3274400893552396">)</span><span ne="0.5305075510305366">;</span><span>
</span><span>    </span><span ne="0.4002494450735382">}</span><span>
</span><span></span><span ne="0.7407043409317912">}</span></code></p>
```

I like using **json columns** to express `ChangedColumns`, `OldValues`, and `NewValues`. In this blog post, in my code example, I use a **Postgres** database.

If you're using SQLite or another database that doesn't support json columns - you can use string types in your entity and create a EF Core Conversion that serializes an object to a string to save it in a database. When retrieving data from the database, this Conversion will deserialize a JSON string into a corresponding .NET type.

In **Postgres** database, when using NET 8 and EF 8 you need to `EnableDynamicJson` in order to be able to have a dynamic json in "jsonb" columns:

```
<p><code id="code-lang-csharp"><span ne="0.030675873646528906">var</span><span> dataSourceBuilder </span><span ne="0.5133411958147744">=</span><span> </span><span ne="0.6897018198506387">new</span><span> </span><span ne="0.8992123407238498">NpgsqlDataSourceBuilder</span><span ne="0.6639375859920901">(</span><span>connectionString</span><span ne="0.34095026957780183">)</span><span ne="0.9927114251140474">;</span><span>
</span><span>dataSourceBuilder</span><span ne="0.7050526277540916">.</span><span ne="0.9138869376298882">EnableDynamicJson</span><span ne="0.3065917511138081">(</span><span ne="0.320526916557188">)</span><span ne="0.3917818629290616">;</span><span>
</span>
<span>builder</span><span ne="0.9899319164286101">.</span><span>Services</span><span ne="0.7082625834573517">.</span><span ne="0.1599652998988521">AddDbContext</span><span ne="0.41471828617478734">&lt;</span><span ne="0.51038045283604">ApplicationDbContext</span><span ne="0.8438046013356179">&gt;</span><span ne="0.2828816148755394">(</span><span ne="0.6689330615736513">(</span><span>provider</span><span ne="0.09383880873883721">,</span><span> options</span><span ne="0.8927685430803699">)</span><span> </span><span ne="0.612439063891278">=&gt;</span><span>
</span><span></span><span ne="0.89337803062103">{</span><span>
</span><span>    </span><span ne="0.41835263463822203">var</span><span> interceptor </span><span ne="0.998446480678897">=</span><span> provider</span><span ne="0.03149485967897658">.</span><span ne="0.23670183333182782">GetRequiredService</span><span ne="0.8054680985355717">&lt;</span><span ne="0.46508772776965623">AuditableInterceptor</span><span ne="0.36052484549893116">&gt;</span><span ne="0.41112744588394656">(</span><span ne="0.8770949644925834">)</span><span ne="0.6194856274527649">;</span><span>
</span>
<span>    options</span><span ne="0.9833303120183362">.</span><span ne="0.3659902381783465">EnableSensitiveDataLogging</span><span ne="0.026895688758523884">(</span><span ne="0.1850012326711462">)</span><span>
</span><span>        </span><span ne="0.05881573571247123">.</span><span ne="0.9511643924641794">UseNpgsql</span><span ne="0.8969716754751167">(</span><span>dataSourceBuilder</span><span ne="0.44689650505979384">.</span><span ne="0.19679676114400058">Build</span><span ne="0.4596149783196254">(</span><span ne="0.8640570468201696">)</span><span ne="0.732493886315582">,</span><span> npgsqlOptions </span><span ne="0.5758177125542686">=&gt;</span><span>
</span><span>        </span><span ne="0.1146785597917277">{</span><span>
</span><span>            npgsqlOptions</span><span ne="0.4170343634281872">.</span><span ne="0.5108573015635812">MigrationsHistoryTable</span><span ne="0.21184781269904973">(</span><span ne="0.36559914346385936">"__MyMigrationsHistory"</span><span ne="0.21071499376527958">,</span><span> </span><span ne="0.8535012651939868">"devtips_audit_trails"</span><span ne="0.4974282595683881">)</span><span ne="0.9907695907261992">;</span><span>
</span><span>        </span><span ne="0.4643303100792664">}</span><span ne="0.6292435128326974">)</span><span>
</span><span>        </span><span ne="0.6434114517154838">.</span><span ne="0.8592261482100967">AddInterceptors</span><span ne="0.4579833078294133">(</span><span>interceptor</span><span ne="0.21180342495824123">)</span><span>
</span><span>        </span><span ne="0.15461032305472888">.</span><span ne="0.2843248938613331">UseSnakeCaseNamingConvention</span><span ne="0.8519481177017404">(</span><span ne="0.6340100019075057">)</span><span ne="0.5863679564994794">;</span><span>
</span><span></span><span ne="0.8542817751301803">}</span><span ne="0.11984912399254288">)</span><span ne="0.6396980769340653">;</span></code></p>
```

## Implementing Audit Trails for all Auditable Entities

We can implement an auditing in EF Core DbContext that will automatically be applied to all entities that inherit from `IAuditableEntity`. But first we need to get a user that is performing create, update or delete actions on these entities.

Let's define a `CurrentSessionProvider` that will retrieve current user identifier from the `ClaimsPrinciple` of a current `HttpRequest`:

```
<p><code id="code-lang-csharp"><span ne="0.9513510766767864">public</span><span> </span><span ne="0.21957328324504766">interface</span><span> </span><span ne="0.4010183089553119">ICurrentSessionProvider</span><span>
</span><span></span><span ne="0.9284884274816261">{</span><span>
</span><span>    </span><span ne="0.49289175865806456">Guid</span><span ne="0.6691487280631473">?</span><span> </span><span ne="0.8455798077281759">GetUserId</span><span ne="0.9171074238757934">(</span><span ne="0.991632906868051">)</span><span ne="0.5185355635523955">;</span><span>
</span><span></span><span ne="0.05117803276360278">}</span><span>
</span>
<span></span><span ne="0.39581069054417795">public</span><span> </span><span ne="0.9424785932656236">class</span><span> </span><span ne="0.9857193717285744">CurrentSessionProvider</span><span> </span><span ne="0.5675815459871755">:</span><span> </span><span ne="0.9143245217006529">ICurrentSessionProvider</span><span>
</span><span></span><span ne="0.791256229787084">{</span><span>
</span><span>    </span><span ne="0.46478300219151714">private</span><span> </span><span ne="0.25746795670981115">readonly</span><span> </span><span ne="0.34897451766858056">Guid</span><span ne="0.9141877525450622">?</span><span> _currentUserId</span><span ne="0.42380694159053556">;</span><span>
</span>
<span>    </span><span ne="0.5482743687764456">public</span><span> </span><span ne="0.8921918216293726">CurrentSessionProvider</span><span ne="0.8832459917366724">(</span><span ne="0.008768327833682088">IHttpContextAccessor</span><span> accessor</span><span ne="0.1856131115471562">)</span><span>
</span><span>    </span><span ne="0.5062240716356415">{</span><span>
</span><span>        </span><span ne="0.17095653373047215">var</span><span> userId </span><span ne="0.9202791968354529">=</span><span> accessor</span><span ne="0.06948456161327632">.</span><span>HttpContext</span><span ne="0.0911895665451592">?.</span><span>User</span><span ne="0.6044883263206345">.</span><span ne="0.11456189782462378">FindFirstValue</span><span ne="0.06121963369490324">(</span><span ne="0.09325606279968268">"userid"</span><span ne="0.5849438908862844">)</span><span ne="0.22353668658442005">;</span><span>
</span><span>        </span><span ne="0.8452896650739663">if</span><span> </span><span ne="0.6627917313812688">(</span><span>userId </span><span ne="0.06821782621513395">is</span><span> </span><span ne="0.2627823359464819">null</span><span ne="0.1589457654152423">)</span><span>
</span><span>        </span><span ne="0.6413639956958669">{</span><span>
</span><span>            </span><span ne="0.5354100881869013">return</span><span ne="0.3678216723074922">;</span><span>
</span><span>        </span><span ne="0.3223019431388653">}</span><span>
</span>
<span>        _currentUserId </span><span ne="0.44912789970934897">=</span><span> Guid</span><span ne="0.2997889817144156">.</span><span>TryParse</span><span ne="0.7463771855364428">(</span><span ne="0.7782578955927587">userId</span><span ne="0.4715783051602299">,</span><span ne="0.8419757083525273"> </span><span ne="0.13514504398422356">out</span><span ne="0.31730528369726585"> </span><span ne="0.07023780157230286">var</span><span ne="0.9983697828519708"> guid</span><span ne="0.06820176116525678">)</span><span ne="0.13808357905674407"> </span><span ne="0.27016343776934093">?</span><span> guid </span><span ne="0.14089363082431672">:</span><span> </span><span ne="0.40754944014470085">null</span><span ne="0.7892171941692216">;</span><span>
</span><span>    </span><span ne="0.5163113373404568">}</span><span>
</span>
<span>    </span><span ne="0.716628905705274">public</span><span> </span><span ne="0.5079271091972383">Guid</span><span ne="0.1541232361094016">?</span><span> </span><span ne="0.7029018530562716">GetUserId</span><span ne="0.8819710326223397">(</span><span ne="0.409938774212779">)</span><span> </span><span ne="0.5506778166290988">=&gt;</span><span> _currentUserId</span><span ne="0.5784906284804335">;</span><span>
</span><span></span><span ne="0.5944029562178768">}</span></code></p>
```

You need to register the provider and `IHttpContextAccessor` in the DI:

```
<p><code id="code-lang-csharp"><span>builder</span><span ne="0.1722952734863905">.</span><span>Services</span><span ne="0.9910327962181786">.</span><span ne="0.5960708752547561">AddHttpContextAccessor</span><span ne="0.4227430511224658">(</span><span ne="0.8647830844539929">)</span><span ne="0.03442021905553383">;</span><span>
</span><span>builder</span><span ne="0.5311080600867484">.</span><span>Services</span><span ne="0.03115231206299618">.</span><span ne="0.3416248542100172">AddScoped</span><span ne="0.8432224205790185">&lt;</span><span ne="0.8007468141267552">ICurrentSessionProvider</span><span ne="0.8373106748283844">,</span><span ne="0.8689003016885086"> CurrentSessionProvider</span><span ne="0.12462402805214201">&gt;</span><span ne="0.5793225010579328">(</span><span ne="0.3371164639904748">)</span><span ne="0.2441049797906908">;</span></code></p>
```

To create the audit trails, we can use EF Core [Changer Tracker](https://antondevtips.com/blog/understanding-change-tracking-for-better-performance-in-ef-core) capabilities to get entities that are created, updated or deleted.

We need to inject `ICurrentSessionProvider` into DbContext and override `SaveChangesAsync` method to create audit trails.

```
<p><code id="code-lang-csharp"><span ne="0.20547495268000704">public</span><span> </span><span ne="0.19617617145362343">class</span><span> </span><span ne="0.8172178080271191">ApplicationDbContext</span><span ne="0.43101566598503194">(</span><span>
</span><span>    </span><span ne="0.6723798468045565">DbContextOptions</span><span ne="0.10793590767368966">&lt;</span><span ne="0.37026021783943364">ApplicationDbContext</span><span ne="0.7134899810512793">&gt;</span><span> options</span><span ne="0.3923705562279216">,</span><span>
</span><span>    </span><span ne="0.19062063797231432">ICurrentSessionProvider</span><span> currentSessionProvider</span><span ne="0.3126161707675008">)</span><span>
</span><span>    </span><span ne="0.9055508168672696">:</span><span> </span><span ne="0.8532807266518745">DbContext</span><span ne="0.3375003196770243">(</span><span>options</span><span ne="0.9752344228853091">)</span><span>
</span><span></span><span ne="0.5520838660224058">{</span><span>
</span><span>    </span><span ne="0.4669137955028392">public</span><span> </span><span ne="0.19760513011214287">ICurrentSessionProvider</span><span> CurrentSessionProvider </span><span ne="0.06641415695992425">=&gt;</span><span> currentSessionProvider</span><span ne="0.7374634482984355">;</span><span>
</span>    
<span>    </span><span ne="0.2698543953952445">public</span><span> </span><span ne="0.2548562201212342">override</span><span> </span><span ne="0.32155422422884805">async</span><span> </span><span ne="0.33139923574660446">Task</span><span ne="0.5271187682781171">&lt;</span><span ne="0.19093132786552824">int</span><span ne="0.24269807529763754">&gt;</span><span> </span><span ne="0.5272345366057882">SaveChangesAsync</span><span ne="0.7286553393810423">(</span><span ne="0.7937338809428152">CancellationToken</span><span> cancellationToken </span><span ne="0.3452022953859939">=</span><span> </span><span ne="0.9910010615703779">new</span><span ne="0.6136957526672849">(</span><span ne="0.9820132092411766">)</span><span ne="0.1332203468274713">)</span><span>
</span><span>    </span><span ne="0.28526527456555073">{</span><span>
</span><span>        </span><span ne="0.41338702231475255">var</span><span> userId </span><span ne="0.1968205478562497">=</span><span> CurrentSessionProvider</span><span ne="0.8920452069737135">.</span><span ne="0.5032599752909498">GetUserId</span><span ne="0.27005134917355256">(</span><span ne="0.9618187357092921">)</span><span ne="0.7580512096540714">;</span><span>
</span>        
<span>        </span><span ne="0.8684047866143223">SetAuditableProperties</span><span ne="0.8581188840832092">(</span><span>userId</span><span ne="0.7421530058485968">)</span><span ne="0.9505211808818268">;</span><span>
</span>
<span>        </span><span ne="0.1975800923768165">var</span><span> auditEntries </span><span ne="0.8411431843916246">=</span><span> </span><span ne="0.2887106743459109">HandleAuditingBeforeSaveChanges</span><span ne="0.1770158279544617">(</span><span>userId</span><span ne="0.07729587601435728">)</span><span ne="0.44758907521540825">.</span><span ne="0.437644407961588">ToList</span><span ne="0.27946807762705805">(</span><span ne="0.28005378818405313">)</span><span ne="0.8614483907536162">;</span><span>
</span><span>        </span><span ne="0.10825202319108618">if</span><span> </span><span ne="0.1360892922976511">(</span><span>auditEntries</span><span ne="0.8771861935354638">.</span><span>Count </span><span ne="0.2165342289426463">&gt;</span><span> </span><span ne="0.8717366331651313">0</span><span ne="0.9568066851512654">)</span><span>
</span><span>        </span><span ne="0.06959235932807206">{</span><span>
</span><span>            </span><span ne="0.2646554588469784">await</span><span> AuditTrails</span><span ne="0.10834193165236916">.</span><span ne="0.5656687654354229">AddRangeAsync</span><span ne="0.6443374970109346">(</span><span>auditEntries</span><span ne="0.3960767808204124">,</span><span> cancellationToken</span><span ne="0.6556185960088993">)</span><span ne="0.014771313165933941">;</span><span>
</span><span>        </span><span ne="0.369156954169403">}</span><span>
</span>
<span>        </span><span ne="0.2145457561852594">return</span><span> </span><span ne="0.21450336589592833">await</span><span> </span><span ne="0.5392562793740165">base</span><span ne="0.12975758150963823">.</span><span ne="0.0868597452786386">SaveChangesAsync</span><span ne="0.14290635061370272">(</span><span>cancellationToken</span><span ne="0.5962334410297364">)</span><span ne="0.6613924602972474">;</span><span>
</span><span>    </span><span ne="0.905755977226835">}</span><span>
</span><span></span><span ne="0.20349525125250423">}</span></code></p>
```

Note, that we are creating `AuditTrails` before calling `base.SaveChangesAsync` to make sure that we persist all changes to the database in a single transaction.

In the code above we are performing two operations:

-   setting auditable properties to the created, updated or deleted records
-   creating audit trail records

For all entities that inherit from `IAuditableEntity` we set `Created` and `Updated` fields. In some cases changes might not be triggered by a user, but rather a code. In such cases we set that a "system" performed changes.

For example, this can be a background job, database seeding, etc.

```
<p><code id="code-lang-csharp"><span ne="0.9677094362582765">private</span><span> </span><span ne="0.9295874176308361">void</span><span> </span><span ne="0.02584875973973033">SetAuditableProperties</span><span ne="0.22976200354719412">(</span><span ne="0.06899865699607544">Guid</span><span ne="0.5820280404761019">?</span><span> userId</span><span ne="0.7982147198526879">)</span><span>
</span><span></span><span ne="0.1451396334740912">{</span><span>
</span><span>    </span><span ne="0.5550694513265252">const</span><span> </span><span ne="0.8917143315902852">string</span><span> systemSource </span><span ne="0.9079235206371831">=</span><span> </span><span ne="0.21845975321447975">"system"</span><span ne="0.14767775532950422">;</span><span>
</span><span>    </span><span ne="0.8016266383435946">foreach</span><span> </span><span ne="0.6181610370224897">(</span><span ne="0.624254978032581">var</span><span> entry </span><span ne="0.8478926838031332">in</span><span> ChangeTracker</span><span ne="0.24427360551102906">.</span><span ne="0.3050172415596354">Entries</span><span ne="0.6449174907438249">&lt;</span><span ne="0.5186813453837522">IAuditableEntity</span><span ne="0.8755045513111815">&gt;</span><span ne="0.34920634160144726">(</span><span ne="0.6291728133030736">)</span><span ne="0.1257694774667446">)</span><span>
</span><span>    </span><span ne="0.0862504948014916">{</span><span>
</span><span>        </span><span ne="0.15536351760770117">switch</span><span> </span><span ne="0.05382814811557057">(</span><span>entry</span><span ne="0.15827109820262442">.</span><span>State</span><span ne="0.9932999438809634">)</span><span>
</span><span>        </span><span ne="0.18544375603554974">{</span><span>
</span><span>            </span><span ne="0.9702806117396334">case</span><span> EntityState</span><span ne="0.5669752657794925">.</span><span>Added</span><span ne="0.6211644566365793">:</span><span>
</span><span>                entry</span><span ne="0.3277237851950424">.</span><span>Entity</span><span ne="0.8601369936086537">.</span><span>CreatedAtUtc </span><span ne="0.17245729729857961">=</span><span> DateTime</span><span ne="0.20188471510974348">.</span><span>UtcNow</span><span ne="0.8143151104045848">;</span><span>
</span><span>                entry</span><span ne="0.2612444913117543">.</span><span>Entity</span><span ne="0.43695545070313535">.</span><span>CreatedBy </span><span ne="0.3926709807587966">=</span><span> userId</span><span ne="0.3973839620708096">?.</span><span ne="0.6002703719440134">ToString</span><span ne="0.8084668836401205">(</span><span ne="0.022267303892034906">)</span><span> </span><span ne="0.3526972970480926">??</span><span> systemSource</span><span ne="0.4660015981924349">;</span><span>
</span><span>                </span><span ne="0.949577173363704">break</span><span ne="0.6548709670842706">;</span><span>
</span>
<span>            </span><span ne="0.8575711628457984">case</span><span> EntityState</span><span ne="0.5788332544043159">.</span><span>Modified</span><span ne="0.9670661408932324">:</span><span>
</span><span>                entry</span><span ne="0.5942311266562191">.</span><span>Entity</span><span ne="0.24758068515694187">.</span><span>UpdatedAtUtc </span><span ne="0.816957613759447">=</span><span> DateTime</span><span ne="0.16186041294902487">.</span><span>UtcNow</span><span ne="0.7692776708312797">;</span><span>
</span><span>                entry</span><span ne="0.7063594280393841">.</span><span>Entity</span><span ne="0.11990170858418003">.</span><span>UpdatedBy </span><span ne="0.1936431919978363">=</span><span> userId</span><span ne="0.6735824374730678">?.</span><span ne="0.6858475898337153">ToString</span><span ne="0.9067790931966551">(</span><span ne="0.29888987950361">)</span><span> </span><span ne="0.41217060693520025">??</span><span> systemSource</span><span ne="0.35861003371825784">;</span><span>
</span><span>                </span><span ne="0.041638065139397384">break</span><span ne="0.6026151837089008">;</span><span>
</span><span>        </span><span ne="0.8833173679455957">}</span><span>
</span><span>    </span><span ne="0.8196307018925354">}</span><span>
</span><span></span><span ne="0.2666065058184316">}</span></code></p>
```

Now let's have a look at how to create audit trail records. Again we're iterating through `IAuditableEntity` entities and select those that were created, updated or deleted:

```
<p><code id="code-lang-csharp"><span ne="0.9704894481278485">private</span><span> </span><span ne="0.49284937586258404">List</span><span ne="0.7471415965807768">&lt;</span><span ne="0.40417950601658215">AuditTrail</span><span ne="0.10278246733204621">&gt;</span><span> </span><span ne="0.8920798211114767">HandleAuditingBeforeSaveChanges</span><span ne="0.7826625617883">(</span><span ne="0.9482596007982016">Guid</span><span ne="0.8565383000915313">?</span><span> userId</span><span ne="0.45772294989700224">)</span><span>
</span><span></span><span ne="0.5233102050962156">{</span><span>
</span><span>    </span><span ne="0.8762056703539767">var</span><span> auditableEntries </span><span ne="0.3727514014600213">=</span><span> ChangeTracker</span><span ne="0.6532032125445159">.</span><span ne="0.32123958948668196">Entries</span><span ne="0.6269726167932776">&lt;</span><span ne="0.7518994759072585">IAuditableEntity</span><span ne="0.1348359758222546">&gt;</span><span ne="0.6313094066443057">(</span><span ne="0.37950955435765665">)</span><span>
</span><span>        </span><span ne="0.2547126419636837">.</span><span ne="0.21450966715296693">Where</span><span ne="0.35448890676440326">(</span><span>x </span><span ne="0.33232242052944216">=&gt;</span><span> x</span><span ne="0.3657671539876237">.</span><span>State </span><span ne="0.8737475726138433">is</span><span> </span><span ne="0.42510007015328555">EntityState</span><span ne="0.002048138345542738">.</span><span ne="0.7888757423905859">Added</span><span> </span><span ne="0.6398941958714051">or</span><span> EntityState</span><span ne="0.4427499978281608">.</span><span>Deleted </span><span ne="0.6673247102246699">or</span><span> EntityState</span><span ne="0.4025466548398422">.</span><span>Modified</span><span ne="0.8168430064284335">)</span><span>
</span><span>        </span><span ne="0.8403650974862725">.</span><span ne="0.2011783162159333">Select</span><span ne="0.12298966630435137">(</span><span>x </span><span ne="0.16638976989958765">=&gt;</span><span> </span><span ne="0.21706134551821266">CreateTrailEntry</span><span ne="0.6431944877666211">(</span><span>userId</span><span ne="0.2777349934001081">,</span><span> x</span><span ne="0.928886897152999">)</span><span ne="0.5273288694106165">)</span><span>
</span><span>        </span><span ne="0.08572977724333697">.</span><span ne="0.1537381574353084">ToList</span><span ne="0.12009484213857202">(</span><span ne="0.7534382099652093">)</span><span ne="0.6388112892574853">;</span><span>
</span>
<span>    </span><span ne="0.640463755640743">return</span><span> auditableEntries</span><span ne="0.430808192645052">;</span><span>
</span><span></span><span ne="0.4241749799522079">}</span><span>
</span>
<span></span><span ne="0.3678318403287616">private</span><span> </span><span ne="0.14305173148091987">static</span><span> </span><span ne="0.8874261933262844">AuditTrail</span><span> </span><span ne="0.8478416253244221">CreateTrailEntry</span><span ne="0.9859035009210673">(</span><span ne="0.7417051206021728">Guid</span><span ne="0.1359566088009786">?</span><span> userId</span><span ne="0.37413495845435396">,</span><span> </span><span ne="0.052976947378473804">EntityEntry</span><span ne="0.9046895031656828">&lt;</span><span ne="0.7551396475822987">IAuditableEntity</span><span ne="0.6945890232714063">&gt;</span><span> entry</span><span ne="0.00014726363702166623">)</span><span>
</span><span></span><span ne="0.8120779386904265">{</span><span>
</span><span>    </span><span ne="0.9398623546116771">var</span><span> trailEntry </span><span ne="0.05496713394693997">=</span><span> </span><span ne="0.2999151583349038">new</span><span> </span><span ne="0.24692004820719837">AuditTrail</span><span>
</span><span>    </span><span ne="0.7714828302022276">{</span><span>
</span><span>        Id </span><span ne="0.8756599765550276">=</span><span> Guid</span><span ne="0.5529729756892052">.</span><span ne="0.4627137260816343">NewGuid</span><span ne="0.3682042466002956">(</span><span ne="0.18124568353861403">)</span><span ne="0.5909119729813455">,</span><span>
</span><span>        EntityName </span><span ne="0.6514954304264928">=</span><span> entry</span><span ne="0.4909679612907427">.</span><span>Entity</span><span ne="0.6905818405787129">.</span><span ne="0.22667892697218117">GetType</span><span ne="0.4172070807391668">(</span><span ne="0.03612504304508424">)</span><span ne="0.6120619770396084">.</span><span>Name</span><span ne="0.41824340756078915">,</span><span>
</span><span>        UserId </span><span ne="0.09128467701850773">=</span><span> userId</span><span ne="0.05851459193829256">,</span><span>
</span><span>        DateUtc </span><span ne="0.9889563259646278">=</span><span> DateTime</span><span ne="0.4364074516695732">.</span><span>UtcNow
</span><span>    </span><span ne="0.32425656274588177">}</span><span ne="0.3134806663625147">;</span><span>
</span>
<span>    </span><span ne="0.09899477067587181">SetAuditTrailPropertyValues</span><span ne="0.16277029128365939">(</span><span>entry</span><span ne="0.8772081851413933">,</span><span> trailEntry</span><span ne="0.05155310222669329">)</span><span ne="0.08172738240365329">;</span><span>
</span><span>    </span><span ne="0.7379416648986746">SetAuditTrailNavigationValues</span><span ne="0.9710157966673116">(</span><span>entry</span><span ne="0.035410749450789814">,</span><span> trailEntry</span><span ne="0.08911978049608404">)</span><span ne="0.4672747144350011">;</span><span>
</span><span>    </span><span ne="0.6043182889997355">SetAuditTrailReferenceValues</span><span ne="0.14645317392223356">(</span><span>entry</span><span ne="0.612832880579054">,</span><span> trailEntry</span><span ne="0.8072062093890868">)</span><span ne="0.9823634220439259">;</span><span>
</span>
<span>    </span><span ne="0.6282946204522762">return</span><span> trailEntry</span><span ne="0.93408332531036">;</span><span>
</span><span></span><span ne="0.5358076828825189">}</span></code></p>
```

An audit trail record can contain the following types of properties:

-   plain properties (like Book's Title or Year of Publication)
-   reference property (like Book's Author)
-   navigation property (like Author's Books)

Let's have a look at how to add plain properties to audit trails:

```
<p><code id="code-lang-csharp"><span ne="0.37409855641483614">private</span><span> </span><span ne="0.5255151726504275">static</span><span> </span><span ne="0.8912008094650129">void</span><span> </span><span ne="0.3851782440435526">SetAuditTrailPropertyValues</span><span ne="0.4500384360266829">(</span><span ne="0.6090795291174044">EntityEntry</span><span> entry</span><span ne="0.4960290312266602">,</span><span> </span><span ne="0.10545987118806566">AuditTrail</span><span> trailEntry</span><span ne="0.389958909760282">)</span><span>
</span><span></span><span ne="0.8060182125639256">{</span><span>
</span><span>    </span><span ne="0.7689701809286003">// Skip temp fields (that will be assigned automatically by ef core engine, for example: when inserting an entity</span><span>
</span><span>    </span><span ne="0.5704253214624458">foreach</span><span> </span><span ne="0.5271309076306856">(</span><span ne="0.6132900696732169">var</span><span> property </span><span ne="0.7977596084314955">in</span><span> entry</span><span ne="0.1391133524993523">.</span><span>Properties</span><span ne="0.9279409986397408">.</span><span ne="0.6324609369303844">Where</span><span ne="0.10448322663144993">(</span><span>x </span><span ne="0.9462249387484676">=&gt;</span><span> </span><span ne="0.36543380244805745">!</span><span>x</span><span ne="0.31152805357639457">.</span><span>IsTemporary</span><span ne="0.681810734772025">)</span><span ne="0.580555017026831">)</span><span>
</span><span>    </span><span ne="0.9616765734464796">{</span><span>
</span><span>        </span><span ne="0.05594804597888947">if</span><span> </span><span ne="0.062120130882282965">(</span><span>property</span><span ne="0.3817493433259258">.</span><span>Metadata</span><span ne="0.5505922896243411">.</span><span ne="0.5353208127851562">IsPrimaryKey</span><span ne="0.5196332225152007">(</span><span ne="0.11467576989949102">)</span><span ne="0.10490197061038364">)</span><span>
</span><span>        </span><span ne="0.611718369226195">{</span><span>
</span><span>            trailEntry</span><span ne="0.5972331905055415">.</span><span>PrimaryKey </span><span ne="0.20522872344497467">=</span><span> property</span><span ne="0.9437290383028694">.</span><span>CurrentValue</span><span ne="0.2388607656352092">?.</span><span ne="0.6491161300001045">ToString</span><span ne="0.1920014608670393">(</span><span ne="0.8752498533915692">)</span><span ne="0.29187936874164466">;</span><span>
</span><span>            </span><span ne="0.8572990050266605">continue</span><span ne="0.43030783743636025">;</span><span>
</span><span>        </span><span ne="0.31705253838018177">}</span><span>
</span>
<span>        </span><span ne="0.06607189025263449">// Filter properties that should not appear in the audit list</span><span>
</span><span>        </span><span ne="0.19355215256640923">if</span><span> </span><span ne="0.3062778784230197">(</span><span>property</span><span ne="0.27566350627581304">.</span><span>Metadata</span><span ne="0.9829373300746883">.</span><span>Name</span><span ne="0.18905479336830244">.</span><span ne="0.8993385463806367">Equals</span><span ne="0.6892620901185033">(</span><span ne="0.984197740131507">"PasswordHash"</span><span ne="0.35607729628326357">)</span><span ne="0.9549321081185607">)</span><span>
</span><span>        </span><span ne="0.6526210346563918">{</span><span>
</span><span>            </span><span ne="0.3271886535266658">continue</span><span ne="0.5383562868043725">;</span><span>
</span><span>        </span><span ne="0.9217440808222891">}</span><span>
</span>
<span>        </span><span ne="0.8457913766472994">SetAuditTrailPropertyValue</span><span ne="0.21423331878227525">(</span><span>entry</span><span ne="0.2862605547573237">,</span><span> trailEntry</span><span ne="0.6345780929189849">,</span><span> property</span><span ne="0.31282707824527956">)</span><span ne="0.445071162464138">;</span><span>
</span><span>    </span><span ne="0.2038506370934009">}</span><span>
</span><span></span><span ne="0.6364300135511485">}</span><span>
</span>
<span></span><span ne="0.3361607821887558">private</span><span> </span><span ne="0.48468635334215515">static</span><span> </span><span ne="0.4857073232078625">void</span><span> </span><span ne="0.6800359107253542">SetAuditTrailPropertyValue</span><span ne="0.13364132724478683">(</span><span ne="0.6899090643225899">EntityEntry</span><span> entry</span><span ne="0.2732190811851558">,</span><span> </span><span ne="0.8073160006151169">AuditTrail</span><span> trailEntry</span><span ne="0.4596113052372971">,</span><span> </span><span ne="0.6367033905172065">PropertyEntry</span><span> property</span><span ne="0.33239476630014997">)</span><span>
</span><span></span><span ne="0.8899602607902688">{</span><span>
</span><span>    </span><span ne="0.1876300853910079">var</span><span> propertyName </span><span ne="0.8257623461146015">=</span><span> property</span><span ne="0.8376907560468739">.</span><span>Metadata</span><span ne="0.36733036287443677">.</span><span>Name</span><span ne="0.008752172009587555">;</span><span>
</span>
<span>    </span><span ne="0.9498284596524761">switch</span><span> </span><span ne="0.9196018834479723">(</span><span>entry</span><span ne="0.33804652088441556">.</span><span>State</span><span ne="0.6395285270869719">)</span><span>
</span><span>    </span><span ne="0.7340132365245852">{</span><span>
</span><span>        </span><span ne="0.18274512319938108">case</span><span> EntityState</span><span ne="0.7821948306764811">.</span><span>Added</span><span ne="0.2294344051800753">:</span><span>
</span><span>            trailEntry</span><span ne="0.5744225241014557">.</span><span>TrailType </span><span ne="0.727795732836745">=</span><span> TrailType</span><span ne="0.6961263585533398">.</span><span>Create</span><span ne="0.6737662194222896">;</span><span>
</span><span>            trailEntry</span><span ne="0.9647561203253899">.</span><span>NewValues</span><span ne="0.5150444327599535">[</span><span>propertyName</span><span ne="0.7195437909532336">]</span><span> </span><span ne="0.465755528555146">=</span><span> property</span><span ne="0.060141826297009926">.</span><span>CurrentValue</span><span ne="0.7320938167316218">;</span><span>
</span>
<span>            </span><span ne="0.1798440631686451">break</span><span ne="0.47058663352791363">;</span><span>
</span>
<span>        </span><span ne="0.49684531379072694">case</span><span> EntityState</span><span ne="0.16463350188831616">.</span><span>Deleted</span><span ne="0.5408562236272222">:</span><span>
</span><span>            trailEntry</span><span ne="0.8652663816804886">.</span><span>TrailType </span><span ne="0.7111643485499365">=</span><span> TrailType</span><span ne="0.3295078294706748">.</span><span>Delete</span><span ne="0.18838271213671087">;</span><span>
</span><span>            trailEntry</span><span ne="0.5412613074064622">.</span><span>OldValues</span><span ne="0.2023944302809666">[</span><span>propertyName</span><span ne="0.18432338090414147">]</span><span> </span><span ne="0.4894793927411766">=</span><span> property</span><span ne="0.6606274498065057">.</span><span>OriginalValue</span><span ne="0.6308150474440823">;</span><span>
</span>
<span>            </span><span ne="0.06539620492932097">break</span><span ne="0.5029503743328844">;</span><span>
</span>
<span>        </span><span ne="0.6541993996166997">case</span><span> EntityState</span><span ne="0.9518335843878135">.</span><span>Modified</span><span ne="0.6896812635910459">:</span><span>
</span><span>            </span><span ne="0.6566622743631307">if</span><span> </span><span ne="0.2928612278146513">(</span><span>property</span><span ne="0.7549321927167993">.</span><span>IsModified </span><span ne="0.8427432946267771">&amp;&amp;</span><span> </span><span ne="0.13528378731729762">(</span><span>property</span><span ne="0.3971719175164581">.</span><span>OriginalValue </span><span ne="0.9703566932618148">is</span><span> </span><span ne="0.8372237261031099">null</span><span> </span><span ne="0.44335844796220836">||</span><span> </span><span ne="0.8642150300493546">!</span><span>property</span><span ne="0.9031872303378243">.</span><span>OriginalValue</span><span ne="0.7767490466413824">.</span><span ne="0.8720484027582621">Equals</span><span ne="0.6057645953209378">(</span><span>property</span><span ne="0.7652219078442926">.</span><span>CurrentValue</span><span ne="0.44030405965371466">)</span><span ne="0.5472873744021075">)</span><span ne="0.6448151291081594">)</span><span>
</span><span>            </span><span ne="0.5955912701049542">{</span><span>
</span><span>                trailEntry</span><span ne="0.5532827008460126">.</span><span>ChangedColumns</span><span ne="0.6330930850402696">.</span><span ne="0.7601797645533706">Add</span><span ne="0.9372447432813152">(</span><span>propertyName</span><span ne="0.6414195195703909">)</span><span ne="0.6796394466212543">;</span><span>
</span><span>                trailEntry</span><span ne="0.20657506453215047">.</span><span>TrailType </span><span ne="0.2441212673552674">=</span><span> TrailType</span><span ne="0.31481168118250935">.</span><span>Update</span><span ne="0.5053357953019603">;</span><span>
</span><span>                trailEntry</span><span ne="0.7464963713734551">.</span><span>OldValues</span><span ne="0.2644154419966247">[</span><span>propertyName</span><span ne="0.29711695790590653">]</span><span> </span><span ne="0.4624187077453462">=</span><span> property</span><span ne="0.6307772019753985">.</span><span>OriginalValue</span><span ne="0.670945081260002">;</span><span>
</span><span>                trailEntry</span><span ne="0.9959771578465769">.</span><span>NewValues</span><span ne="0.2621492250605819">[</span><span>propertyName</span><span ne="0.8618846392497225">]</span><span> </span><span ne="0.06850117984162463">=</span><span> property</span><span ne="0.1642006289640422">.</span><span>CurrentValue</span><span ne="0.13704429088167103">;</span><span>
</span><span>            </span><span ne="0.21835234713521046">}</span><span>
</span>
<span>            </span><span ne="0.6208386552773446">break</span><span ne="0.08544242437188831">;</span><span>
</span><span>    </span><span ne="0.2558066115141573">}</span><span>
</span>
<span>    </span><span ne="0.3057464197244507">if</span><span> </span><span ne="0.09843221938709312">(</span><span>trailEntry</span><span ne="0.5455804857871687">.</span><span>ChangedColumns</span><span ne="0.5968233394975205">.</span><span>Count </span><span ne="0.06199224943861292">&gt;</span><span> </span><span ne="0.5608401609731866">0</span><span ne="0.8795573647528396">)</span><span>
</span><span>    </span><span ne="0.6588606616877157">{</span><span>
</span><span>        trailEntry</span><span ne="0.3318992990366679">.</span><span>TrailType </span><span ne="0.13627370863250576">=</span><span> TrailType</span><span ne="0.8900656846952558">.</span><span>Update</span><span ne="0.012770736780401748">;</span><span>
</span><span>    </span><span ne="0.7889749004491142">}</span><span>
</span><span></span><span ne="0.8791308606458728">}</span></code></p>
```

If you need to exclude any sensitive fields, you can do it here. For example, we are excluding `PasswordHash` property from audit trails.

Now let's explore how to add reference and navigation properties into audit trails:

```
<p><code id="code-lang-csharp"><span ne="0.6327553502758541">private</span><span> </span><span ne="0.40071007933760094">static</span><span> </span><span ne="0.5721120038599824">void</span><span> </span><span ne="0.10980080486226473">SetAuditTrailReferenceValues</span><span ne="0.797327904181017">(</span><span ne="0.990202282485877">EntityEntry</span><span> entry</span><span ne="0.18402133773637397">,</span><span> </span><span ne="0.9631406558255696">AuditTrail</span><span> trailEntry</span><span ne="0.07866918627851505">)</span><span>
</span><span></span><span ne="0.00015643016003052956">{</span><span>
</span><span>    </span><span ne="0.8968710180567394">foreach</span><span> </span><span ne="0.25465838103384286">(</span><span ne="0.5489867630496015">var</span><span> reference </span><span ne="0.9595714586922199">in</span><span> entry</span><span ne="0.7364130009639613">.</span><span>References</span><span ne="0.06262110811681854">.</span><span ne="0.1805525159711434">Where</span><span ne="0.1612226393914783">(</span><span>x </span><span ne="0.858829251690191">=&gt;</span><span> x</span><span ne="0.7920906485603866">.</span><span>IsModified</span><span ne="0.8272189126719204">)</span><span ne="0.3398610716754126">)</span><span>
</span><span>    </span><span ne="0.9636881884393519">{</span><span>
</span><span>        </span><span ne="0.1930009010190259">var</span><span> referenceName </span><span ne="0.38206127208196794">=</span><span> reference</span><span ne="0.7301845677872525">.</span><span>EntityEntry</span><span ne="0.2856515671473179">.</span><span>Entity</span><span ne="0.3494826158182506">.</span><span ne="0.46797095641393216">GetType</span><span ne="0.8128440083260449">(</span><span ne="0.06157881330522741">)</span><span ne="0.190398446940369">.</span><span>Name</span><span ne="0.3216554434735579">;</span><span>
</span><span>        trailEntry</span><span ne="0.6368161150669627">.</span><span>ChangedColumns</span><span ne="0.8878525579718113">.</span><span ne="0.907410880673135">Add</span><span ne="0.32969451889735213">(</span><span>referenceName</span><span ne="0.40488002474556717">)</span><span ne="0.7035105861027054">;</span><span>
</span><span>    </span><span ne="0.0010403189721086559">}</span><span>
</span><span></span><span ne="0.21365112202492398">}</span><span>
</span>
<span></span><span ne="0.5593712853625149">private</span><span> </span><span ne="0.7169340422962805">static</span><span> </span><span ne="0.28072625370936877">void</span><span> </span><span ne="0.4848535714162706">SetAuditTrailNavigationValues</span><span ne="0.7424505394389823">(</span><span ne="0.7266362891403415">EntityEntry</span><span> entry</span><span ne="0.7184397276924136">,</span><span> </span><span ne="0.10550769513634761">AuditTrail</span><span> trailEntry</span><span ne="0.8926211509247138">)</span><span>
</span><span></span><span ne="0.37476754775268395">{</span><span>
</span><span>    </span><span ne="0.21591792573552715">foreach</span><span> </span><span ne="0.2733364098441453">(</span><span ne="0.7547839321565958">var</span><span> navigation </span><span ne="0.9707277155609378">in</span><span> entry</span><span ne="0.4980087752702944">.</span><span>Navigations</span><span ne="0.620031910131126">.</span><span ne="0.49077171666009434">Where</span><span ne="0.5173526283881639">(</span><span>x </span><span ne="0.04411092145195894">=&gt;</span><span> x</span><span ne="0.3367920280204285">.</span><span>Metadata</span><span ne="0.9620316196503975">.</span><span>IsCollection </span><span ne="0.9727761296777673">&amp;&amp;</span><span> x</span><span ne="0.26889990487230686">.</span><span>IsModified</span><span ne="0.13534600297768384">)</span><span ne="0.3175593871769117">)</span><span>
</span><span>    </span><span ne="0.7174715717584742">{</span><span>
</span><span>        </span><span ne="0.2523367126916778">if</span><span> </span><span ne="0.5835474075366446">(</span><span>navigation</span><span ne="0.9141505699567442">.</span><span>CurrentValue </span><span ne="0.691919566878798">is</span><span> </span><span ne="0.07466043495129115">not</span><span> </span><span ne="0.7726738000556607">IEnumerable</span><span ne="0.2562115485519776">&lt;</span><span ne="0.7614331611518331">object</span><span ne="0.7654899844885882">&gt;</span><span> enumerable</span><span ne="0.716902519530093">)</span><span>
</span><span>        </span><span ne="0.718475075256799">{</span><span>
</span><span>            </span><span ne="0.461663831108865">continue</span><span ne="0.6461869054611976">;</span><span>
</span><span>        </span><span ne="0.5200933924163886">}</span><span>
</span>
<span>        </span><span ne="0.9252630163082144">var</span><span> collection </span><span ne="0.023326129838205145">=</span><span> enumerable</span><span ne="0.49191228935831677">.</span><span ne="0.13046069618233547">ToList</span><span ne="0.7123802074198795">(</span><span ne="0.4375168959123005">)</span><span ne="0.750735524313774">;</span><span>
</span><span>        </span><span ne="0.5337211866356404">if</span><span> </span><span ne="0.002996527104345059">(</span><span>collection</span><span ne="0.8023439708965657">.</span><span>Count </span><span ne="0.5576523190391974">==</span><span> </span><span ne="0.1919880756763438">0</span><span ne="0.1683053852546147">)</span><span>
</span><span>        </span><span ne="0.3293354149196084">{</span><span>
</span><span>            </span><span ne="0.013146599567201656">continue</span><span ne="0.23969140742890416">;</span><span>
</span><span>        </span><span ne="0.6739209618337506">}</span><span>
</span>
<span>        </span><span ne="0.3180138314838946">var</span><span> navigationName </span><span ne="0.32817218686710414">=</span><span> collection</span><span ne="0.9953025180876796">.</span><span ne="0.7772769840686015">First</span><span ne="0.06601233801895867">(</span><span ne="0.06762576075123383">)</span><span ne="0.6908716789715971">.</span><span ne="0.19798694222843582">GetType</span><span ne="0.1510453853873447">(</span><span ne="0.34138926913713064">)</span><span ne="0.7937025702550431">.</span><span>Name</span><span ne="0.5182949420921749">;</span><span>
</span><span>        trailEntry</span><span ne="0.10761038403609291">.</span><span>ChangedColumns</span><span ne="0.07928258711980685">.</span><span ne="0.2601544929695486">Add</span><span ne="0.982178682795277">(</span><span>navigationName</span><span ne="0.9897621955509199">)</span><span ne="0.7405277171678474">;</span><span>
</span><span>    </span><span ne="0.578615287701202">}</span><span>
</span><span></span><span ne="0.9658287609700097">}</span></code></p>
```

Finally, we can run our application to see auditing in action.

Here is an example of auditing properties set by a system and by a user in the `authors` table:

![Screenshot_1](https://antondevtips.com/media/code_screenshots/efcore/audit-trails/img_1.png)

Here is how the `audit_trails` table looks like:

![Screenshot_2](https://antondevtips.com/media/code_screenshots/efcore/audit-trails/img_2.png)

![Screenshot_3](https://antondevtips.com/media/code_screenshots/efcore/audit-trails/img_3.png)

Hope you find this newsletter useful. See you next time.
