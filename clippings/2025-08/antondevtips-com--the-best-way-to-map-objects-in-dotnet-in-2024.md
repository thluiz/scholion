---
url: "https://antondevtips.com/blog/the-best-way-to-map-objects-in-dotnet-in-2024?utm_source=email&utm_medium=email&utm_campaign=website"
captured_at: "2025-08-11T15:13:12+01:00"
title: "The Best Way To Map Objects in .Net in 2024"
domain: "antondevtips-com"
---

---
In today's blog post you will learn how to map objects in .NET using various techniques and libraries. We'll explore what is the best way to map objects in .NET in 2024.

## What is Object Mapping

What is **object mapping** and why do you need one in ASP.NET Core applications?

**Object mapping** is a transformation of objects from one type to another, often between different layers of an application.

Mapping is essential for separation of concerns

Here are a few reasons to use object mapping:

-   **Separation of concerns:** keeps business logic and data transfer logic distinct.
-   **Performance:** decreases size of objects transferred through the network, sending only the necessary piece of data needed by clients.
-   **Security:** hides private domain data from the clients. Like real entity ids, personal data, and internal domain properties.
-   **Maintainability:** simplifies updates and changes to the data structures, as domain models are distinguished from the public contract used by clients.

In many applications, usually there are 2 levels of models: domain and public contracts. These public contract models are often called DTOs (data transfer objects).

DTOs are the models consumed by a client, and usually they are tinier than their domain counterparts. Also, a DTO model may contain properties from few domain models.

It is essential to distinguish domain internal models from the public models. Clients should receive the exact piece of data they need, no more. And they shouldn't consume models that contain private and internal data due to security considerations.

Another reason for using separate models for public contracts: you can change your domain models while keeping your public contracts unchanged, so you won't break the clients using the API.

## How To Do Object Mapping

We figured out what object mapping is, now let's explore some of the most used mapping techniques.

There are 2 main approaches of object mapping: **manual** and **automated** by using mapping libraries.

Manual approach involves manually writing code that performs mapping, for example:

```
<p><code id="code-lang-csharp"><span ne="0.28324819239824695">public</span><span> </span><span ne="0.4363475892304255">static</span><span> </span><span ne="0.04417826816252557">BookDto</span><span> </span><span ne="0.1951172747798985">MapToBookDto</span><span ne="0.8771087046908116">(</span><span ne="0.0007797646130516256">this</span><span> </span><span ne="0.5722181202412603">Book</span><span> entity</span><span ne="0.8080141228752875">)</span><span>
</span><span></span><span ne="0.1435501626393877">{</span><span>
</span><span>    </span><span ne="0.614249149768828">return</span><span> </span><span ne="0.5272446267249971">new</span><span> </span><span ne="0.1597535848331968">BookDto</span><span>
</span><span>    </span><span ne="0.7616385410646843">{</span><span>
</span><span>        Title </span><span ne="0.9111869381582012">=</span><span> entity</span><span ne="0.3286298152023348">.</span><span>Title</span><span ne="0.36475000331780794">,</span><span>
</span><span>        Year </span><span ne="0.5454094581905196">=</span><span> entity</span><span ne="0.31173351712019426">.</span><span>Year</span><span ne="0.0903447892294077">,</span><span>
</span><span>        Isbn </span><span ne="0.16115781543247554">=</span><span> entity</span><span ne="0.651963709872071">.</span><span>Isbn</span><span ne="0.3175663801587162">,</span><span>
</span><span>        Price </span><span ne="0.778324233849829">=</span><span> entity</span><span ne="0.07783340116935877">.</span><span>Price
</span><span>    </span><span ne="0.0805144711564334">}</span><span ne="0.24347355642419655">;</span><span>
</span><span></span><span ne="0.38481596498520176">}</span><span>
</span>
<span></span><span ne="0.054649372308952615">var</span><span> bookDto </span><span ne="0.9505308683363335">=</span><span> book</span><span ne="0.1525325159808829">.</span><span ne="0.45306007172311025">MapToBookDto</span><span ne="0.4398219832639594">(</span><span ne="0.07892075349900407">)</span><span ne="0.10874849533644415">;</span></code></p>
```

When mapping properties of `Book` domain entity to `BookDto` we need to manually set all properties of the DTO model.

This if often tiresome, that's why a mapping libraries were created. These libraries automate the process of mapping and reduce the boilerplate code. On paper, these libraries should minimize the risk of errors, but the reality is the opposite.

To showcase why using mapping libraries is not the best option in 2024, first we need to have a look at these libraries and how they perform object mapping.

## Mapping Using AutoMapper Library

**AutoMapper** is one of the most popular libraries for object-to-object mapping in .NET.

To add AutoMapper to your project, you need to run the following command to install NuGet package:

```
<p><code id="code-lang-bash"><span>dotnet </span><span ne="0.44226350439798856">add</span><span> package AutoMapper</span></code></p>
```

Let's create a mapping from `Book` entity to `BookDto`:

```
<p><code id="code-lang-csharp"><span ne="0.9915713979874411">public</span><span> </span><span ne="0.6070397465659718">class</span><span> </span><span ne="0.25935150908029136">Book</span><span>
</span><span></span><span ne="0.40794295416858783">{</span><span>
</span><span>    </span><span ne="0.35473307495759665">public</span><span> </span><span ne="0.8951351729393369">Guid</span><span> Id </span><span ne="0.3523444783430868">{</span><span> </span><span ne="0.6717868489270737">get</span><span ne="0.16811777340638956">;</span><span> </span><span ne="0.3964701858766547">set</span><span ne="0.5384433236570788">;</span><span> </span><span ne="0.24087198053751768">}</span><span>
</span>    
<span>    </span><span ne="0.016657137749321316">public</span><span> </span><span ne="0.7481552498252716">string</span><span> Title </span><span ne="0.4841328633753603">{</span><span> </span><span ne="0.9306458272811464">get</span><span ne="0.4371460873819436">;</span><span> </span><span ne="0.09863076564305251">set</span><span ne="0.7513619948788752">;</span><span> </span><span ne="0.8983456242278955">}</span><span>
</span>    
<span>    </span><span ne="0.999738040203786">public</span><span> </span><span ne="0.2417461359773999">int</span><span> Year </span><span ne="0.13754749604954974">{</span><span> </span><span ne="0.5666445409241555">get</span><span ne="0.26468497750042974">;</span><span> </span><span ne="0.6436142103519434">set</span><span ne="0.2717287714549538">;</span><span> </span><span ne="0.5144129422896202">}</span><span>
</span>    
<span>    </span><span ne="0.9992632887478062">public</span><span> </span><span ne="0.6057917217962778">string</span><span> Isbn </span><span ne="0.9654737939303861">{</span><span> </span><span ne="0.5189879813095469">get</span><span ne="0.9497643149118181">;</span><span> </span><span ne="0.43560240694311736">set</span><span ne="0.13252212381929318">;</span><span> </span><span ne="0.6676114165016205">}</span><span>
</span>    
<span>    </span><span ne="0.29768308472075">public</span><span> </span><span ne="0.39515147093735326">decimal</span><span> Price </span><span ne="0.7897802894788382">{</span><span> </span><span ne="0.8079266044613408">get</span><span ne="0.08123975435511555">;</span><span> </span><span ne="0.9506907656681487">set</span><span ne="0.15632891231222557">;</span><span> </span><span ne="0.25630253428994054">}</span><span>
</span>    
<span>    </span><span ne="0.2725669615508619">public</span><span> </span><span ne="0.638944272472288">Author</span><span> Author </span><span ne="0.9528307441880982">{</span><span> </span><span ne="0.8655702009403232">get</span><span ne="0.3518255839023332">;</span><span> </span><span ne="0.5889957793328399">set</span><span ne="0.031539992398160854">;</span><span> </span><span ne="0.6523070284156522">}</span><span>
</span><span></span><span ne="0.18192404531205109">}</span><span>
</span>
<span></span><span ne="0.5919485569359417">public</span><span> </span><span ne="0.07435079192640037">record</span><span> </span><span ne="0.3089773410905986">BookDto</span><span>
</span><span></span><span ne="0.20497080501757858">{</span><span>
</span><span>    </span><span ne="0.27025368945719763">public</span><span> </span><span ne="0.23292973187136679">string</span><span> Isbn </span><span ne="0.36785999162836114">{</span><span> </span><span ne="0.13374034391017187">get</span><span ne="0.7455738580488102">;</span><span> </span><span ne="0.07839491317810854">set</span><span ne="0.04027806722688343">;</span><span> </span><span ne="0.1856115586527025">}</span><span>
</span>    
<span>    </span><span ne="0.26289046516219183">public</span><span> </span><span ne="0.7639662955520898">string</span><span> Title </span><span ne="0.5623516637092603">{</span><span> </span><span ne="0.22203590712545063">get</span><span ne="0.8239230451266949">;</span><span> </span><span ne="0.9529680200033526">init</span><span ne="0.7715885157743132">;</span><span> </span><span ne="0.3386779138124809">}</span><span>
</span>    
<span>    </span><span ne="0.9246384945000907">public</span><span> </span><span ne="0.3760147217290013">int</span><span> Year </span><span ne="0.7665026593249888">{</span><span> </span><span ne="0.5428499520427297">get</span><span ne="0.39561342811201927">;</span><span> </span><span ne="0.6415247517155341">init</span><span ne="0.09061643029710731">;</span><span> </span><span ne="0.10500578982073294">}</span><span>
</span>    
<span>    </span><span ne="0.6838792035067441">public</span><span> </span><span ne="0.9604703858950918">decimal</span><span> Price </span><span ne="0.5441270501339969">{</span><span> </span><span ne="0.5557722845017997">get</span><span ne="0.45380424220373694">;</span><span> </span><span ne="0.9464700870280294">set</span><span ne="0.2485228483422255">;</span><span> </span><span ne="0.012359176111992887">}</span><span>
</span>    
<span>    </span><span ne="0.7005041253686289">public</span><span> </span><span ne="0.5586940499228336">string</span><span> Author </span><span ne="0.5582724448106985">{</span><span> </span><span ne="0.822533365769282">get</span><span ne="0.38834892896121365">;</span><span> </span><span ne="0.33124774565168613">set</span><span ne="0.7550265997583538">;</span><span> </span><span ne="0.9405103115834663">}</span><span>
</span><span></span><span ne="0.4178015419624237">}</span></code></p>
```

First, you need to configure AutoMapper how to map these objects. You need to create a mapping class that inherits from base `Profile` class.

In this mapping profile, you need to specify only those fields that differ between the models. Other properties are mapped automatically.

```
<p><code id="code-lang-csharp"><span ne="0.5282428594609464">public</span><span> </span><span ne="0.7122087477799818">class</span><span> </span><span ne="0.6578291175224453">BookProfile</span><span> </span><span ne="0.18184611286625874">:</span><span> </span><span ne="0.24375015900349162">Profile</span><span>
</span><span></span><span ne="0.692836131007339">{</span><span>
</span><span>    </span><span ne="0.24906699116375652">public</span><span> </span><span ne="0.35466125533753523">BookProfile</span><span ne="0.7433802045973679">(</span><span ne="0.5132281242139496">)</span><span>
</span><span>    </span><span ne="0.6700657115537947">{</span><span>
</span><span>        </span><span ne="0.20865753592545944">CreateMap</span><span ne="0.21836687580337133">&lt;</span><span ne="0.5933190897103391">Book</span><span ne="0.15629323778024862">,</span><span ne="0.5993499537915342"> BookDto</span><span ne="0.8101756351599437">&gt;</span><span ne="0.3060406042452548">(</span><span ne="0.031299178132936034">)</span><span>
</span><span>            </span><span ne="0.12666063300164598">.</span><span ne="0.33304414858675246">ForMember</span><span ne="0.8014759892875969">(</span><span>dest </span><span ne="0.6211755623318547">=&gt;</span><span> dest</span><span ne="0.22416959150365467">.</span><span>Author</span><span ne="0.4929743458001309">,</span><span> opt </span><span ne="0.1779342590125118">=&gt;</span><span> opt</span><span ne="0.05128708968136386">.</span><span ne="0.9657288152475628">MapFrom</span><span ne="0.24136833047827067">(</span><span>src </span><span ne="0.8713878211203918">=&gt;</span><span> src</span><span ne="0.10081091042813006">.</span><span>Author</span><span ne="0.17597985914456982">.</span><span>Name</span><span ne="0.8133865469021218">)</span><span ne="0.07033049278526438">)</span><span ne="0.9616091493941311">;</span><span>
</span>            
<span>        </span><span ne="0.7212244450382269">CreateMap</span><span ne="0.13375303431706742">&lt;</span><span ne="0.1557595560878423">BookDto</span><span ne="0.16343557731150404">,</span><span ne="0.6772764725152469"> Book</span><span ne="0.3457553775081349">&gt;</span><span ne="0.9035443766535053">(</span><span ne="0.1604412304572056">)</span><span>
</span><span>            </span><span ne="0.9194122725220909">.</span><span ne="0.024163240458143886">ForPath</span><span ne="0.22046410768964753">(</span><span>dest </span><span ne="0.8000916254213365">=&gt;</span><span> dest</span><span ne="0.0382972782890616">.</span><span>Author</span><span ne="0.2910111526764496">.</span><span>Name</span><span ne="0.5446552973531531">,</span><span> opt </span><span ne="0.9745434593980898">=&gt;</span><span> opt</span><span ne="0.4326111896348874">.</span><span ne="0.9017117227455625">MapFrom</span><span ne="0.20674619881219491">(</span><span>src </span><span ne="0.10970409765638989">=&gt;</span><span> src</span><span ne="0.027867122292572155">.</span><span>Author</span><span ne="0.13849104229873077">)</span><span ne="0.7915971199697892">)</span><span ne="0.9762383774951432">;</span><span>
</span><span>    </span><span ne="0.6390710551475626">}</span><span>
</span><span></span><span ne="0.7901671604352258">}</span></code></p>
```

`BookDto` is very similar to the `Book` entity, but has no `Id` property and has `Author` name as string that is mapped to the child `Author` entity.

Next, you need to register AutoMapper and its profiles in the DI container.

```
<p><code id="code-lang-csharp"><span>builder</span><span ne="0.2944978334803062">.</span><span>Services</span><span ne="0.8733159189144093">.</span><span ne="0.39462416475466566">AddAutoMapper</span><span ne="0.9595479226285342">(</span><span ne="0.04487628198287463">typeof</span><span ne="0.2701548855357384">(</span><span ne="0.36953835485472586">Program</span><span ne="0.24920780176851542">)</span><span ne="0.013998207377115768">)</span><span ne="0.470590384738822">;</span></code></p>
```

In the `AddAutoMapper` method you need to specify types of assemblies that contain the mapping profiles.

Finally, to use mapping, you need to use the `IMapper` interface and call the `Map` method:

```
<p><code id="code-lang-csharp"><span ne="0.760840326054036">public</span><span> </span><span ne="0.3048943375382652">class</span><span> </span><span ne="0.42756722948739334">SomeService</span><span>
</span><span></span><span ne="0.41554170414875324">{</span><span>
</span><span>    </span><span ne="0.5729226705760654">private</span><span> </span><span ne="0.5665916571601664">readonly</span><span> </span><span ne="0.790428017263065">IMapper</span><span> _mapper</span><span ne="0.23177159051596286">;</span><span>
</span>
<span>    </span><span ne="0.12142353292357633">public</span><span> </span><span ne="0.3582825635366934">SomeService</span><span ne="0.45622672419810484">(</span><span ne="0.6659693083006624">IMapper</span><span> mapper</span><span ne="0.9859282616449218">)</span><span>
</span><span>    </span><span ne="0.45415627813301807">{</span><span>
</span><span>        _mapper </span><span ne="0.030482777643807912">=</span><span> mapper</span><span ne="0.737508321608878">;</span><span>
</span><span>    </span><span ne="0.6150113744657468">}</span><span>
</span>
<span>    </span><span ne="0.39107122155851115">public</span><span> </span><span ne="0.5267386114468995">BookDto</span><span> </span><span ne="0.6586629498546797">ToBookDto</span><span ne="0.6855469412333487">(</span><span ne="0.7489292394335975">Book</span><span> entity</span><span ne="0.9386579705071183">)</span><span>
</span><span>    </span><span ne="0.9828540852024477">{</span><span>
</span><span>        </span><span ne="0.8407934051941989">return</span><span> _mapper</span><span ne="0.10596836403245802">.</span><span ne="0.8715274512032531">Map</span><span ne="0.22701762366579115">&lt;</span><span ne="0.35408666352268026">BookDto</span><span ne="0.8292543839042915">&gt;</span><span ne="0.4085773857352727">(</span><span>entity</span><span ne="0.31311713763474314">)</span><span ne="0.9187551529674013">;</span><span>
</span><span>    </span><span ne="0.7549123141694397">}</span><span>
</span><span></span><span ne="0.695582460793527">}</span></code></p>
```

## Mapping Using Mapster Library

**Mapster** is another powerful library for object mapping in .NET, known for its high performance and flexibility. This library is newer and faster when compared to AutoMapper.

To install Mapster, use the NuGet package manager:

```
<p><code id="code-lang-bash"><span>dotnet </span><span ne="0.9057969882238902">add</span><span> package Mapster.DependencyInjection</span></code></p>
```

Mapster setup is much similar to the AutoMapper. First, create a profile by inheriting from the `IRegister` interface:

```
<p><code id="code-lang-csharp"><span ne="0.8929128832014646">public</span><span> </span><span ne="0.6983681474267324">class</span><span> </span><span ne="0.12614207998424032">BookProfile</span><span> </span><span ne="0.4869124487959704">:</span><span> </span><span ne="0.2959411412981878">IRegister</span><span>
</span><span></span><span ne="0.9042806640493589">{</span><span>
</span><span>    </span><span ne="0.11964002683230823">public</span><span> </span><span ne="0.9412978824671272">void</span><span> </span><span ne="0.8592099201287485">Register</span><span ne="0.20587810102116932">(</span><span ne="0.017182097520397233">TypeAdapterConfig</span><span> config</span><span ne="0.8443172033582346">)</span><span>
</span><span>    </span><span ne="0.9705522157731473">{</span><span>
</span>        config
<span>            </span><span ne="0.09846654226972151">.</span><span ne="0.19102853146110854">NewConfig</span><span ne="0.015929924936338602">&lt;</span><span ne="0.6061999791857281">Book</span><span ne="0.7568653658509175">,</span><span ne="0.9094506872745367"> BookDto</span><span ne="0.8641460057894548">&gt;</span><span ne="0.26664261181576476">(</span><span ne="0.8897158479052993">)</span><span>
</span><span>            </span><span ne="0.958834567545005">.</span><span ne="0.20298021716927783">TwoWays</span><span ne="0.10800707949253174">(</span><span ne="0.599751408839987">)</span><span>
</span><span>            </span><span ne="0.17387517479847214">.</span><span ne="0.8484069087477036">Map</span><span ne="0.08102615256962398">(</span><span>dest </span><span ne="0.19907254561658472">=&gt;</span><span> dest</span><span ne="0.9255837000930972">.</span><span>Author</span><span ne="0.35998590495246485">,</span><span> src </span><span ne="0.23232273290557703">=&gt;</span><span> src</span><span ne="0.11777921719041562">.</span><span>Author</span><span ne="0.21900468790840844">.</span><span>Name</span><span ne="0.9797264174435228">)</span><span ne="0.6964077281742148">;</span><span>
</span><span>    </span><span ne="0.26184440194725156">}</span><span>
</span><span></span><span ne="0.8581903181000007">}</span></code></p>
```

Then register Mapster in DI and add all the mapping profiles:

```
<p><code id="code-lang-csharp"><span>builder</span><span ne="0.06853067154675185">.</span><span>Services</span><span ne="0.2674059021294256">.</span><span ne="0.5781923530680712">AddMapster</span><span ne="0.3870612638599479">(</span><span ne="0.3268778868015525">)</span><span ne="0.6611529113606592">;</span><span>
</span>
<span>TypeAdapterConfig</span><span ne="0.4709138285300547">.</span><span>GlobalSettings</span><span ne="0.585035594194908">.</span><span ne="0.7431811240909512">Scan</span><span ne="0.3752016486913169">(</span><span>Assembly</span><span ne="0.8236262980217726">.</span><span ne="0.2494942178940608">GetExecutingAssembly</span><span ne="0.6837927242036712">(</span><span ne="0.5278335786206387">)</span><span ne="0.8194954366908009">)</span><span ne="0.5049426367798653">;</span></code></p>
```

To use Mapster, inject the same `IMapper` interface, but from another namespace:

```
<p><code id="code-lang-csharp"><span ne="0.8020366204300738">public</span><span> </span><span ne="0.4639366516854643">class</span><span> </span><span ne="0.8166289825895628">SomeService</span><span>
</span><span></span><span ne="0.23104096803055074">{</span><span>
</span><span>    </span><span ne="0.18712051864016732">private</span><span> </span><span ne="0.4331687773063414">readonly</span><span> </span><span ne="0.6374566416261311">IMapper</span><span> _mapper</span><span ne="0.7743018019898902">;</span><span>
</span>
<span>    </span><span ne="0.0028337765213221067">public</span><span> </span><span ne="0.40523430155143414">SomeService</span><span ne="0.5554879247960042">(</span><span ne="0.8959134687522408">IMapper</span><span> mapper</span><span ne="0.43440081515302675">)</span><span>
</span><span>    </span><span ne="0.7238282376423406">{</span><span>
</span><span>        _mapper </span><span ne="0.42771244158791666">=</span><span> mapper</span><span ne="0.08303627521965784">;</span><span>
</span><span>    </span><span ne="0.22314841541268116">}</span><span>
</span>
<span>    </span><span ne="0.06733803871424748">public</span><span> </span><span ne="0.2202922486937986">BookDto</span><span> </span><span ne="0.8593078789482377">ToBookDto</span><span ne="0.43452301048715525">(</span><span ne="0.2617566061972906">Book</span><span> entity</span><span ne="0.9481378266490385">)</span><span>
</span><span>    </span><span ne="0.8266884452393348">{</span><span>
</span><span>        </span><span ne="0.9512964304296191">return</span><span> _mapper</span><span ne="0.20858741760661603">.</span><span ne="0.5276747066040129">Map</span><span ne="0.7079749498399045">&lt;</span><span ne="0.42419860253661523">BookDto</span><span ne="0.7083157547973179">&gt;</span><span ne="0.7830811478524372">(</span><span>entity</span><span ne="0.8692509698069706">)</span><span ne="0.16488149612744885">;</span><span>
</span><span>    </span><span ne="0.8650009826566903">}</span><span>
</span><span></span><span ne="0.9931429668722392">}</span></code></p>
```

Mapster also supports a static extension method `Adapt`, available for any object. This method performs an automatic mapping that doesn't require any mapping configuration:

```
<p><code id="code-lang-csharp"><span ne="0.27991402144807187">var</span><span> bookDto </span><span ne="0.5349274955593741">=</span><span> bookEntity</span><span ne="0.3450899169966124">.</span><span ne="0.5385928231619282">Adapt</span><span ne="0.28978715439126024">&lt;</span><span ne="0.7395319841681984">BookDto</span><span ne="0.8068702057784034">&gt;</span><span ne="0.8392601397244221">(</span><span ne="0.09294725191582465">)</span><span ne="0.5864249873215399">;</span></code></p>
```

You can use this method for simple mappings where two models differ slightly.

So mapping libraries seem to be a great option, but why this is not the best approach to do the object mapping? Let's find out!

## Why Using Mapping Libraries is Not a Silver Bullet

Mapping libraries have a lot of advantages.

Despite their advantages, mapping libraries also come with several potential drawbacks:

1.  **Performance Overhead** - mapping libraries often use reflection to inspect and map object properties at runtime. This can introduce performance overhead, especially in high-performance applications or when dealing with complex or large volumes of data.
2.  **Complex configurations** - while mapping libraries aim to simplify the mapping process, they can sometimes lead to complex configurations, especially for advanced scenarios. Configuring custom mappings, value resolvers, and type converters can become cumbersome and error-prone.
3.  **Debugging Challenges** - when using mapping libraries, debugging mapping issues can be challenging. Errors might appear only at runtime, making it harder to trace and fix problems.
4.  **Error prone** - if you ever used mapping libraries in real applications, I am certain that you have run into runtime errors, only because you forgot to update the mapping profile after adding a new property to the mapping object.

So what is the best option to map objects?

It might sound shocking - but this is manual mapping. But with one interesting addition from me. Let's have a look!

## The Best Way To Do Mapping in .NET in 2024

First, let's explore entities for the blog posts application:

```
<p><code id="code-lang-csharp"><span ne="0.31190491481636173">public</span><span> </span><span ne="0.797885193510153">class</span><span> </span><span ne="0.20662077865276662">BlogPost</span><span>
</span><span></span><span ne="0.37811392483660444">{</span><span>
</span><span>    </span><span ne="0.16969917476308427">public</span><span> required </span><span ne="0.5279481900516464">Guid</span><span> Id </span><span ne="0.8420060293023337">{</span><span> </span><span ne="0.858529336216049">get</span><span ne="0.9334608734183608">;</span><span> </span><span ne="0.7361381712258424">init</span><span ne="0.5947383200876177">;</span><span> </span><span ne="0.6598491512057421">}</span><span>
</span>
<span>    </span><span ne="0.20051021341077035">public</span><span> required </span><span ne="0.16279600360487945">string</span><span> Title </span><span ne="0.02173354720314724">{</span><span> </span><span ne="0.846410441778428">get</span><span ne="0.9836531089011783">;</span><span> </span><span ne="0.21607320340876546">init</span><span ne="0.7398376777539067">;</span><span> </span><span ne="0.2980452827071167">}</span><span>
</span>
<span>    </span><span ne="0.0030253175994425785">public</span><span> required </span><span ne="0.07307670922260112">string</span><span> Content </span><span ne="0.4137861248003186">{</span><span> </span><span ne="0.8060045831431379">get</span><span ne="0.010334748316492615">;</span><span> </span><span ne="0.6810931689545787">set</span><span ne="0.9224187766289577">;</span><span> </span><span ne="0.9218113447956013">}</span><span>
</span>
<span>    </span><span ne="0.5497269343212245">public</span><span> required </span><span ne="0.003845307436755152">DateTime</span><span> PublishedUtc </span><span ne="0.5035256777182145">{</span><span> </span><span ne="0.6326492819234691">get</span><span ne="0.37783921307525314">;</span><span> </span><span ne="0.4056995755575076">set</span><span ne="0.07457565669402855">;</span><span> </span><span ne="0.06740753488855156">}</span><span>
</span>
<span>    </span><span ne="0.1224005618033367">public</span><span> required </span><span ne="0.7798570837537684">Guid</span><span> PublisherId </span><span ne="0.45287828972715916">{</span><span> </span><span ne="0.9729311621864218">get</span><span ne="0.19971302969156424">;</span><span> </span><span ne="0.6531317409203898">set</span><span ne="0.8836231990620819">;</span><span> </span><span ne="0.6291763112033074">}</span><span>
</span>
<span>    </span><span ne="0.4210152935845921">public</span><span> required </span><span ne="0.19572752020666595">Publisher</span><span> Publisher </span><span ne="0.9521969188492639">{</span><span> </span><span ne="0.08659739505971087">get</span><span ne="0.02402345321900501">;</span><span> </span><span ne="0.5570546298357775">set</span><span ne="0.8975560740273998">;</span><span> </span><span ne="0.1700726488666846">}</span><span>
</span>
<span>    </span><span ne="0.9464062919309959">public</span><span> required </span><span ne="0.08523865236216077">List</span><span ne="0.7869285378758133">&lt;</span><span ne="0.9574778808584335">BlogHistoryRecord</span><span ne="0.5573854950733195">&gt;</span><span> BlogHistoryRecords </span><span ne="0.40630247433663613">{</span><span> </span><span ne="0.6627379680451236">get</span><span ne="0.24872301198704216">;</span><span> </span><span ne="0.6697655597868094">init</span><span ne="0.5760637246275858">;</span><span> </span><span ne="0.3020564175810826">}</span><span> </span><span ne="0.6699276862962033">=</span><span> </span><span ne="0.9327532280658287">[</span><span ne="0.9998435212448052">]</span><span ne="0.1850755505079179">;</span><span>
</span><span></span><span ne="0.6046083319585454">}</span><span>
</span>
<span></span><span ne="0.3138840849089152">public</span><span> </span><span ne="0.02930325377743681">class</span><span> </span><span ne="0.9477335984199634">Publisher</span><span>
</span><span></span><span ne="0.5008689254648817">{</span><span>
</span><span>    </span><span ne="0.6299265710797063">public</span><span> required </span><span ne="0.5535129820784561">Guid</span><span> Id </span><span ne="0.33187724646303285">{</span><span> </span><span ne="0.8850626820780126">get</span><span ne="0.16965115053461644">;</span><span> </span><span ne="0.6044066660242503">init</span><span ne="0.9229373428352767">;</span><span> </span><span ne="0.07156250880932802">}</span><span>
</span>
<span>    </span><span ne="0.638103063847464">public</span><span> required </span><span ne="0.1320963897025781">string</span><span> Email </span><span ne="0.00022184760475230103">{</span><span> </span><span ne="0.0943269156753147">get</span><span ne="0.30578140732697356">;</span><span> </span><span ne="0.6263922222093484">init</span><span ne="0.7514484590355112">;</span><span> </span><span ne="0.32892666486000033">}</span><span>
</span>
<span>    </span><span ne="0.41456300110927946">public</span><span> required </span><span ne="0.5912749071907202">string</span><span> Name </span><span ne="0.40321719056205596">{</span><span> </span><span ne="0.9570346446606064">get</span><span ne="0.586604672087706">;</span><span> </span><span ne="0.7127574212534654">init</span><span ne="0.5735748278806395">;</span><span> </span><span ne="0.789648033140397">}</span><span>
</span>    
<span>    </span><span ne="0.7375781320401192">public</span><span> required </span><span ne="0.9022301910130996">string</span><span> Role </span><span ne="0.2604889992450633">{</span><span> </span><span ne="0.7457501498365363">get</span><span ne="0.879438330265978">;</span><span> </span><span ne="0.34366026831266516">init</span><span ne="0.9273224244405435">;</span><span> </span><span ne="0.740610563137119">}</span><span>
</span>
<span>    </span><span ne="0.3430052397713046">public</span><span> required </span><span ne="0.49743340159196103">List</span><span ne="0.3143982889631024">&lt;</span><span ne="0.3917469602172504">BlogPost</span><span ne="0.49204713854570514">&gt;</span><span> BlogPosts </span><span ne="0.9040493717865589">{</span><span> </span><span ne="0.3444174253648693">get</span><span ne="0.45417880213841577">;</span><span> </span><span ne="0.39548010570078296">init</span><span ne="0.7008083016893174">;</span><span> </span><span ne="0.21375524326488293">}</span><span> </span><span ne="0.755753670028031">=</span><span> </span><span ne="0.3392109661476814">[</span><span ne="0.28311147172621676">]</span><span ne="0.7238238639619395">;</span><span>
</span><span></span><span ne="0.9490915554391227">}</span><span>
</span>
<span></span><span ne="0.617054534201515">public</span><span> </span><span ne="0.12006829468056324">class</span><span> </span><span ne="0.3732786014532834">BlogHistoryRecord</span><span>
</span><span></span><span ne="0.7197275105773236">{</span><span>
</span><span>    </span><span ne="0.8671891643840313">public</span><span> required </span><span ne="0.18128770955715634">Guid</span><span> Id </span><span ne="0.23197227056704472">{</span><span> </span><span ne="0.6154789263329089">get</span><span ne="0.6263387368334951">;</span><span> </span><span ne="0.07077964413196969">init</span><span ne="0.4848209503838976">;</span><span> </span><span ne="0.7599769974025431">}</span><span>
</span>
<span>    </span><span ne="0.0874142496319058">public</span><span> required </span><span ne="0.46662398335639854">Guid</span><span> BlogPostId </span><span ne="0.5932057096159216">{</span><span> </span><span ne="0.675835295629451">get</span><span ne="0.5479402360877779">;</span><span> </span><span ne="0.016868657689932176">init</span><span ne="0.8073873320417536">;</span><span> </span><span ne="0.2528740178265375">}</span><span>
</span>
<span>    </span><span ne="0.9396504625121078">public</span><span> required </span><span ne="0.4796100959956804">BlogPost</span><span> BlogPost </span><span ne="0.09646541939042363">{</span><span> </span><span ne="0.8289006558904101">get</span><span ne="0.870707217100347">;</span><span> </span><span ne="0.8031511077928664">init</span><span ne="0.6298375611262794">;</span><span> </span><span ne="0.794405067582811">}</span><span>
</span>
<span>    </span><span ne="0.22120644659793087">public</span><span> required </span><span ne="0.7378294616116268">DateTime</span><span> Date </span><span ne="0.9394870525596102">{</span><span> </span><span ne="0.7431460273838932">get</span><span ne="0.8046413614083319">;</span><span> </span><span ne="0.6191997260503898">init</span><span ne="0.7614868877245986">;</span><span> </span><span ne="0.3479717178718078">}</span><span>
</span>
<span>    </span><span ne="0.1572348278706437">public</span><span> required </span><span ne="0.3727946238875881">double</span><span> Rating </span><span ne="0.7068839292377682">{</span><span> </span><span ne="0.6533136635003268">get</span><span ne="0.2591462953531294">;</span><span> </span><span ne="0.4163857237930766">init</span><span ne="0.6259255812581367">;</span><span> </span><span ne="0.12965533293509712">}</span><span>
</span><span></span><span ne="0.3081160559910232">}</span></code></p>
```

We have a `BlogPost` entity, a `Publisher` entity that represents a user in the system that write blogs. And a `BlogHistoryRecord` entity that holds information for all user ratings for each blog post.

Now, let's explore the public contract (DTO) models that are returned from the webapi:

```
<p><code id="code-lang-csharp"><span ne="0.1490443947911838">public</span><span> </span><span ne="0.8338800568452699">record</span><span> </span><span ne="0.6047448411374646">BlogPostDto</span><span>
</span><span></span><span ne="0.5630739747197403">{</span><span>
</span><span>    </span><span ne="0.13457955817966927">public</span><span> required </span><span ne="0.7696741182922874">string</span><span> Url </span><span ne="0.8806811659123059">{</span><span> </span><span ne="0.2199850219252999">get</span><span ne="0.12232571002331727">;</span><span> </span><span ne="0.6042267375231559">init</span><span ne="0.31004365602635564">;</span><span> </span><span ne="0.14339094829271382">}</span><span>
</span>
<span>    </span><span ne="0.3563074444026407">public</span><span> required </span><span ne="0.7945216549221195">string</span><span> Title </span><span ne="0.04132084618041676">{</span><span> </span><span ne="0.8289906810126673">get</span><span ne="0.4572256036007015">;</span><span> </span><span ne="0.7839897153672628">init</span><span ne="0.3117240892418477">;</span><span> </span><span ne="0.07523347880311315">}</span><span>
</span>
<span>    </span><span ne="0.6380361558408838">public</span><span> required </span><span ne="0.01758223711036444">string</span><span> Content </span><span ne="0.4797959480221151">{</span><span> </span><span ne="0.05358805499853525">get</span><span ne="0.3744654405623573">;</span><span> </span><span ne="0.2725211241452905">init</span><span ne="0.42580059545851034">;</span><span> </span><span ne="0.2895221080465582">}</span><span>
</span>
<span>    </span><span ne="0.9383112611854594">public</span><span> required </span><span ne="0.2197945662515074">DateOnly</span><span> PublishedDate </span><span ne="0.045834085271974634">{</span><span> </span><span ne="0.12760220553852109">get</span><span ne="0.4435866103359707">;</span><span> </span><span ne="0.7071860572965875">init</span><span ne="0.5154467792040179">;</span><span> </span><span ne="0.038672921998536">}</span><span>
</span>
<span>    </span><span ne="0.05050763607047315">public</span><span> required </span><span ne="0.12363361648986615">PublisherDto</span><span> Publisher </span><span ne="0.33748756184643514">{</span><span> </span><span ne="0.739741770002448">get</span><span ne="0.3585598488741195">;</span><span> </span><span ne="0.2260084350322039">init</span><span ne="0.2743476981206775">;</span><span> </span><span ne="0.6259334971183609">}</span><span>
</span>
<span>    </span><span ne="0.7640539266491815">public</span><span> required </span><span ne="0.4040563750936623">double</span><span> Rating </span><span ne="0.8734796315450574">{</span><span> </span><span ne="0.32524460921504983">get</span><span ne="0.930294700677264">;</span><span> </span><span ne="0.8984359072339644">init</span><span ne="0.16587413651943095">;</span><span> </span><span ne="0.041102982513014696">}</span><span>
</span><span></span><span ne="0.9050340388264172">}</span><span>
</span>
<span></span><span ne="0.6246037038624648">public</span><span> </span><span ne="0.865946170328479">record</span><span> </span><span ne="0.08570865901403868">PublisherDto</span><span>
</span><span></span><span ne="0.21855662519887897">{</span><span>
</span><span>    </span><span ne="0.9307860236747061">public</span><span> required </span><span ne="0.3396683142730186">string</span><span> Name </span><span ne="0.6408207958149957">{</span><span> </span><span ne="0.46134750538424907">get</span><span ne="0.10720473926275242">;</span><span> </span><span ne="0.5696221135683759">init</span><span ne="0.26190650297396956">;</span><span> </span><span ne="0.03149918486804204">}</span><span>
</span>
<span>    </span><span ne="0.16121118945619606">public</span><span> required </span><span ne="0.582323343093619">int</span><span> TotalPosts </span><span ne="0.0015287750721615367">{</span><span> </span><span ne="0.4813210830242136">get</span><span ne="0.58483655646655">;</span><span> </span><span ne="0.6278702764463521">init</span><span ne="0.20802243080713456">;</span><span> </span><span ne="0.9396103995335542">}</span><span>
</span>
<span>    </span><span ne="0.22919500281257355">public</span><span> required </span><span ne="0.48944955371557286">double</span><span> Rating </span><span ne="0.9061428467723792">{</span><span> </span><span ne="0.21496213062735103">get</span><span ne="0.4335847466970192">;</span><span> </span><span ne="0.28077986552667533">init</span><span ne="0.5046083965168168">;</span><span> </span><span ne="0.6210721066155414">}</span><span>
</span><span></span><span ne="0.5461406205417921">}</span></code></p>
```

These models have interesting features:

-   `BlogPost` has `Rating` property that represents the average blog rating, taking into account all the user reviews
-   `PublisherDto` has `TotalPosts` and `Rating` properties. The `Rating` property represents the average blog rating of all publisher's blogs, taking into account all the user reviews

Now let's create a mapping for these objects. First, you need to create a static class which is a place for the mapping extension methods.

Next, you need to define mapping methods, I like making them in the following way:

```
<p><code id="code-lang-csharp"><span ne="0.6591132388615459">public</span><span> </span><span ne="0.22870101436214396">static</span><span> </span><span ne="0.6914262935581105">class</span><span> </span><span ne="0.1820044094254506">BlogPostMappingExtensions</span><span>
</span><span></span><span ne="0.1871374832842525">{</span><span>
</span><span>    </span><span ne="0.7863205326591182">public</span><span> </span><span ne="0.032867857730652705">static</span><span> </span><span ne="0.5630187173516424">BlogPostDto</span><span> </span><span ne="0.11230129234254027">MapToBlogPostDto</span><span ne="0.8753750867908406">(</span><span ne="0.14031996817191605">this</span><span> </span><span ne="0.054360764316427224">BlogPost</span><span> entity</span><span ne="0.9844465497671898">)</span><span>
</span><span>    </span><span ne="0.9728636616232326">{</span><span>
</span><span>        </span><span ne="0.9434786981709421">// ...</span><span>
</span><span>    </span><span ne="0.6923546463738515">}</span><span>
</span><span></span><span ne="0.950515354017963">}</span><span>
</span>
<span></span><span ne="0.1600548852993504">var</span><span> blogPostDto </span><span ne="0.8388689088027554">=</span><span> blogPost</span><span ne="0.6701878206723876">.</span><span ne="0.036255794006766484">MapToBlogPostDto</span><span ne="0.8463415505474358">(</span><span ne="0.05468910803137916">)</span><span ne="0.6849399180821248">;</span></code></p>
```

This code is pretty straightforward as you can navigate to the `MapToBlogPostDto` method while reading the code or debugging and see exactly what is going on in the mapping. When using mapping libraries, you need to search for the mapping profiles or extensions in the entire solution to find out how the mapping is done.

Let's explore the full mapping implementation:

```
<p><code id="code-lang-csharp"><span ne="0.7028797782997414">public</span><span> </span><span ne="0.0044605461456062034">static</span><span> </span><span ne="0.13266558351045943">class</span><span> </span><span ne="0.9384339828669214">BlogPostMappingExtensions</span><span>
</span><span></span><span ne="0.676582309525396">{</span><span>
</span><span>    </span><span ne="0.6490331344871842">public</span><span> </span><span ne="0.6271931956888263">static</span><span> </span><span ne="0.44709902483308783">BlogPostDto</span><span> </span><span ne="0.47766705262373976">MapToBlogPostDto</span><span ne="0.253457632678997">(</span><span ne="0.4998459627218014">this</span><span> </span><span ne="0.463475806451194">BlogPost</span><span> entity</span><span ne="0.9443860184798626">)</span><span>
</span><span>    </span><span ne="0.538926151040141">{</span><span>
</span><span>        </span><span ne="0.02928043669275937">return</span><span> </span><span ne="0.8281843322551483">new</span><span> </span><span ne="0.9347124380077976">BlogPostDto</span><span>
</span><span>        </span><span ne="0.6715447697174556">{</span><span>
</span><span>            Url </span><span ne="0.9795434641128549">=</span><span> entity</span><span ne="0.5373808944360806">.</span><span>Id</span><span ne="0.7232158907557735">.</span><span ne="0.16448964405436006">ToString</span><span ne="0.988972878826058">(</span><span ne="0.3442927730107973">)</span><span ne="0.7934731758134456">,</span><span>
</span><span>            Title </span><span ne="0.1869869708285382">=</span><span> entity</span><span ne="0.6091630444329673">.</span><span>Title</span><span ne="0.1316711236682312">,</span><span>
</span><span>            Content </span><span ne="0.62068188236496">=</span><span> entity</span><span ne="0.8191016223132755">.</span><span>Content</span><span ne="0.5478351694673831">,</span><span>
</span><span>            PublishedDate </span><span ne="0.47028105940725906">=</span><span> DateOnly</span><span ne="0.550954558197627">.</span><span ne="0.6044779764496512">FromDateTime</span><span ne="0.6204773932152879">(</span><span>entity</span><span ne="0.19735707405418934">.</span><span>PublishedUtc</span><span ne="0.09577568845806317">)</span><span ne="0.05219628259799247">,</span><span>
</span><span>            Publisher </span><span ne="0.24795802574875014">=</span><span> entity</span><span ne="0.07604158235882441">.</span><span>Publisher</span><span ne="0.374056369957414">.</span><span ne="0.6590954304675464">MapToPublisherDto</span><span ne="0.8411923180921829">(</span><span ne="0.9536213263537207">)</span><span ne="0.938940504170332">,</span><span>
</span><span>            Rating </span><span ne="0.8479581630077885">=</span><span> </span><span ne="0.44871703452220346">CalculateRating</span><span ne="0.210630559167848">(</span><span>entity</span><span ne="0.3604859830759901">.</span><span>BlogHistoryRecords</span><span ne="0.09128647995673167">)</span><span>
</span><span>        </span><span ne="0.11457602226207741">}</span><span ne="0.6677315984746177">;</span><span>
</span><span>    </span><span ne="0.12816460031093313">}</span><span>
</span>
<span>    </span><span ne="0.0786712064498426">public</span><span> </span><span ne="0.28241188641400106">static</span><span> </span><span ne="0.9826999492906445">PublisherDto</span><span> </span><span ne="0.681106461915502">MapToPublisherDto</span><span ne="0.9024210484827053">(</span><span ne="0.7012277220813712">this</span><span> </span><span ne="0.5331347419830226">Publisher</span><span> entity</span><span ne="0.6238085443546637">)</span><span>
</span><span>    </span><span ne="0.6429066490986889">{</span><span>
</span><span>        </span><span ne="0.5635409028009323">var</span><span> blogPostRatings </span><span ne="0.022976800956201138">=</span><span> entity</span><span ne="0.9671069144681124">.</span><span>BlogPosts
</span><span>            </span><span ne="0.255065092020329">.</span><span ne="0.1826502832112642">SelectMany</span><span ne="0.9680382316266947">(</span><span>x </span><span ne="0.5217936757070888">=&gt;</span><span> x</span><span ne="0.786388575932855">.</span><span>BlogHistoryRecords</span><span ne="0.7570505139002033">)</span><span>
</span><span>            </span><span ne="0.40613453807355615">.</span><span ne="0.585124412032501">Select</span><span ne="0.6426177037440804">(</span><span>x </span><span ne="0.07937273399124156">=&gt;</span><span> x</span><span ne="0.8698479076061677">.</span><span>Rating</span><span ne="0.11467866947245264">)</span><span>
</span><span>            </span><span ne="0.25567203877669475">.</span><span ne="0.5179585544867573">ToList</span><span ne="0.1963116444703208">(</span><span ne="0.9443574561511474">)</span><span ne="0.7643926144506717">;</span><span>
</span>
<span>        </span><span ne="0.31034365723772706">var</span><span> averageRating </span><span ne="0.41687527261109436">=</span><span> Math</span><span ne="0.045478251664877956">.</span><span ne="0.8091748782285418">Round</span><span ne="0.16236554161133443">(</span><span>blogPostRatings</span><span ne="0.12263503545850685">.</span><span ne="0.6614484704838757">Average</span><span ne="0.3179289584915781">(</span><span ne="0.0603146857868575">)</span><span ne="0.0674910914753315">,</span><span> </span><span ne="0.5215047873760658">2</span><span ne="0.08537948686842667">)</span><span ne="0.6476085937280907">;</span><span>
</span>
<span>        </span><span ne="0.8947535859291501">return</span><span> </span><span ne="0.9631418648757414">new</span><span> </span><span ne="0.07578480288849765">PublisherDto</span><span>
</span><span>        </span><span ne="0.2398087445008089">{</span><span>
</span><span>            Name </span><span ne="0.9270924638922331">=</span><span> entity</span><span ne="0.8837872122278082">.</span><span>Name</span><span ne="0.9429156995492473">,</span><span>
</span><span>            TotalPosts </span><span ne="0.865131864240851">=</span><span> entity</span><span ne="0.327582627770324">.</span><span>BlogPosts</span><span ne="0.20165509783216395">.</span><span>Count</span><span ne="0.34511056174737564">,</span><span>
</span><span>            Rating </span><span ne="0.7952980776882799">=</span><span> averageRating
</span><span>        </span><span ne="0.8645152703801087">}</span><span ne="0.42380772971795355">;</span><span>
</span><span>    </span><span ne="0.5921822966618925">}</span><span>
</span>
<span>    </span><span ne="0.6446502426471097">private</span><span> </span><span ne="0.2447416774828043">static</span><span> </span><span ne="0.9826012105534313">double</span><span> </span><span ne="0.06513033318447181">CalculateRating</span><span ne="0.8095034607031844">(</span><span ne="0.8883658266737707">List</span><span ne="0.4934152546093602">&lt;</span><span ne="0.9171169019404619">BlogHistoryRecord</span><span ne="0.2709629480785011">&gt;</span><span> historyRecords</span><span ne="0.9145915290265774">)</span><span>
</span><span>    </span><span ne="0.42348060155579703">{</span><span>
</span><span>        </span><span ne="0.1959712452154998">return</span><span> Math</span><span ne="0.18699582367324497">.</span><span ne="0.2561523970027699">Round</span><span ne="0.20593267263016846">(</span><span>historyRecords</span><span ne="0.6625929712195769">.</span><span ne="0.420743112098415">Average</span><span ne="0.10209852783894913">(</span><span ne="0.3206986205291634">record</span><span> </span><span ne="0.13602951675942643">=&gt;</span><span> </span><span ne="0.5889338134147635">record</span><span ne="0.7080816062955345">.</span><span>Rating</span><span ne="0.9349077046822182">)</span><span ne="0.8299884852875905">,</span><span> </span><span ne="0.7668962074239524">2</span><span ne="0.05701584252011005">)</span><span ne="0.2873039932130391">;</span><span>
</span><span>    </span><span ne="0.22014194694802813">}</span><span>
</span><span></span><span ne="0.8137702501935457">}</span></code></p>
```

Let's see the mapping in action when returning DTO models in the asp.net core minimal APIs:

```
<p><code id="code-lang-csharp"><span>app</span><span ne="0.5693097606911759">.</span><span ne="0.19794892044305978">MapGet</span><span ne="0.3960582916231362">(</span><span ne="0.938158145620594">"/api/blogs"</span><span ne="0.8915650923295076">,</span><span> </span><span ne="0.46275412523664405">async</span><span> </span><span ne="0.9802104810785135">(</span><span ne="0.8466833960203889">ApplicationDbContext</span><span> dbContext</span><span ne="0.722372251678982">)</span><span> </span><span ne="0.1031242812725689">=&gt;</span><span>
</span><span></span><span ne="0.2312759725440855">{</span><span>
</span><span>    </span><span ne="0.8604472425396184">var</span><span> blogPosts </span><span ne="0.2920714392985626">=</span><span> </span><span ne="0.2799671670233175">await</span><span> dbContext</span><span ne="0.06620950399314629">.</span><span>BlogPosts
</span><span>        </span><span ne="0.4388608167042102">.</span><span ne="0.5596417702113741">Include</span><span ne="0.5904512366065134">(</span><span>b </span><span ne="0.8239219887408594">=&gt;</span><span> b</span><span ne="0.46033234272685697">.</span><span>Publisher</span><span ne="0.7113727726453973">)</span><span>
</span><span>        </span><span ne="0.5664803175030421">.</span><span ne="0.9555280576320927">Include</span><span ne="0.1589160038692492">(</span><span>b </span><span ne="0.1962531148798634">=&gt;</span><span> b</span><span ne="0.12219508312787153">.</span><span>BlogHistoryRecords</span><span ne="0.24265707003411807">)</span><span>
</span><span>        </span><span ne="0.16493261393041736">.</span><span ne="0.9965519432340826">ToListAsync</span><span ne="0.3711257330829947">(</span><span ne="0.0738531834561994">)</span><span ne="0.6062757777378281">;</span><span>
</span>
<span>    </span><span ne="0.8485006726743906">var</span><span> blogPostDtos </span><span ne="0.6797213125535735">=</span><span> blogPosts
</span><span>        </span><span ne="0.8361341207352032">.</span><span ne="0.5875939770746502">Select</span><span ne="0.7610786631378988">(</span><span>x </span><span ne="0.1262902340735822">=&gt;</span><span> x</span><span ne="0.3289298121496492">.</span><span ne="0.07692157416704493">MapToBlogPostDto</span><span ne="0.6324863690103412">(</span><span ne="0.01528131506186814">)</span><span ne="0.7390481378857511">)</span><span>
</span><span>        </span><span ne="0.4680003864154614">.</span><span ne="0.5437846007270417">ToList</span><span ne="0.44980057787843275">(</span><span ne="0.17656662029097592">)</span><span ne="0.2736251466435111">;</span><span>
</span>
<span>    </span><span ne="0.7414803423449743">return</span><span> Results</span><span ne="0.5449341390045402">.</span><span ne="0.06520432259555287">Ok</span><span ne="0.24269949816046887">(</span><span>blogPostDtos</span><span ne="0.36108707348677993">)</span><span ne="0.32263996488660074">;</span><span>
</span><span></span><span ne="0.5959314808247597">}</span><span ne="0.7997217209422901">)</span><span ne="0.04122333169256154">;</span><span>
</span>
<span>app</span><span ne="0.07367597004305537">.</span><span ne="0.1824671103873613">MapGet</span><span ne="0.6005504736318714">(</span><span ne="0.06977021592281962">"/api/publishers"</span><span ne="0.29897961388707506">,</span><span> </span><span ne="0.23338680707499404">async</span><span> </span><span ne="0.924136069428673">(</span><span ne="0.40664761251795556">ApplicationDbContext</span><span> dbContext</span><span ne="0.9319920905593003">)</span><span> </span><span ne="0.34021472601749103">=&gt;</span><span>
</span><span></span><span ne="0.48648339441759814">{</span><span>
</span><span>    </span><span ne="0.1127816540396851">var</span><span> publishers </span><span ne="0.8506848341897487">=</span><span> </span><span ne="0.827120553075414">await</span><span> dbContext</span><span ne="0.9137518983166723">.</span><span>Publishers
</span><span>        </span><span ne="0.7546284591345949">.</span><span ne="0.6395241217299686">Include</span><span ne="0.10363497690416357">(</span><span>b </span><span ne="0.9637994626908711">=&gt;</span><span> b</span><span ne="0.5468057768077709">.</span><span>BlogPosts</span><span ne="0.16316601295297883">)</span><span>
</span><span>        </span><span ne="0.9123955125339216">.</span><span ne="0.15164592876578664">ThenInclude</span><span ne="0.49945363381208474">(</span><span>b </span><span ne="0.9059124319771765">=&gt;</span><span> b</span><span ne="0.5974081822805942">.</span><span>BlogHistoryRecords</span><span ne="0.9713949112313776">)</span><span>
</span><span>        </span><span ne="0.6783802276050582">.</span><span ne="0.29971698669195057">ToListAsync</span><span ne="0.791912510870874">(</span><span ne="0.8824098503966556">)</span><span ne="0.023428134089882646">;</span><span>
</span>
<span>    </span><span ne="0.12356784298415191">var</span><span> publisherDtos </span><span ne="0.9551263348192344">=</span><span> publishers
</span><span>        </span><span ne="0.08873473977631086">.</span><span ne="0.33719873547029533">Select</span><span ne="0.32430449142273754">(</span><span>x </span><span ne="0.8406022547737079">=&gt;</span><span> x</span><span ne="0.7087143589099034">.</span><span ne="0.30811044193760784">MapToPublisherDto</span><span ne="0.09990620611793244">(</span><span ne="0.5801456237550445">)</span><span ne="0.13676138878067323">)</span><span>
</span><span>        </span><span ne="0.6598745730797677">.</span><span ne="0.13851543509016295">ToList</span><span ne="0.8015860649097291">(</span><span ne="0.3555416161502767">)</span><span ne="0.7732724341424084">;</span><span>
</span>
<span>    </span><span ne="0.6624975222501301">return</span><span> Results</span><span ne="0.41608786045455637">.</span><span ne="0.41267575845122617">Ok</span><span ne="0.32204723218533415">(</span><span>publisherDtos</span><span ne="0.8176319495057361">)</span><span ne="0.6120435146428895">;</span><span>
</span><span></span><span ne="0.4849092000469378">}</span><span ne="0.10166907056449714">)</span><span ne="0.5734565206435136">;</span></code></p>
```

As you have noticed, all the properties for entities and DTOs are marked as **required**. This **secret addition** I find as the game changer in the object mapping.

Whenever you create mapping, you're not able to forget to map a property.

Let's see this in practice. We are going to modify the `BlogPost` entity and add two new properties:

```
<p><code id="code-lang-csharp"><span ne="0.029022636640477995">public</span><span> </span><span ne="0.6074389370520747">class</span><span> </span><span ne="0.14286562450706985">BlogPost</span><span>
</span><span></span><span ne="0.13209084857548326">{</span><span>
</span><span>    </span><span ne="0.02788974222668783">// ...</span><span>
</span>    
<span>    </span><span ne="0.6419552839484319">public</span><span> required </span><span ne="0.22363366293981035">string</span><span> Description </span><span ne="0.16700518699455746">{</span><span> </span><span ne="0.04483501230483955">get</span><span ne="0.9261957113488772">;</span><span> </span><span ne="0.15306863124766878">set</span><span ne="0.7634390614315284">;</span><span> </span><span ne="0.6893877527040195">}</span><span>
</span>
<span>    </span><span ne="0.6260303076756233">public</span><span> required </span><span ne="0.6137123614621423">string</span><span> Category </span><span ne="0.16909364995541531">{</span><span> </span><span ne="0.2981948542157483">get</span><span ne="0.23298724023208706">;</span><span> </span><span ne="0.8733047188226982">set</span><span ne="0.6053462671611997">;</span><span> </span><span ne="0.8836006239889852">}</span><span>
</span><span></span><span ne="0.6140615818862898">}</span></code></p>
```

And let's suppose that we forget to update the mapping, let's compile our application:

![Screenshot_1](https://antondevtips.com/media/code_screenshots/aspnetcore/best-mapping/img_aspnet_mapping_1.png)

Our application doesn't compile and we receive a list of compilation errors that are easy to fix.

## Summary

I think that **manual mapping** with **required properties** is the best way to do the object mapping in 2024.

Let's recap why this approach is better than using mapping libraries:

-   Following this approach, while reading the code, you can exactly see what is going on in the mapping. You don't need to search for mapping classes in the entire application to understand how the libraries do the mapping magic.
-   You have code safety. If you forget to update the mapping method - a compiler error is raised.
-   You have entire control over the mapping process, you don't need to spend time learning how to do the fancy mapping stuff in the libraries.
-   This approach is much more performant as no reflection is required during the runtime
-   Debugging is straightforward. Have you ever tried to step into the breakpoint in the mapping profile while debugging a mapping library? This is really hard or almost impossible to do. Forget about this problem and have the stress-less debugging.

Hope you find this newsletter useful. See you next time.
