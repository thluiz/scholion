---
url: "https://blog.dochia.dev/blog/json-isnt-json/"
captured_at: "2025-09-26T19:24:58+01:00"
title: "JSON is not JSON Across Languages | <span class=\"text-terminal-purple\">Dochia</span> CLI Blog"
domain: "blog-dochia-dev"
---

---
## Introduction: These Aren’t the JSONs You’re Looking For

JSON (JavaScript Object Notation) was **designed as a simple, lightweight, and human-readable** data interchange format, often positioned as a more accessible alternative to XML. It has become the de facto standard for web APIs and system integration. However, while the specification itself is straightforward, **different programming languages and libraries can interpret certain aspects of JSON differently**. What appears to be a uniform format can, in practice, lead to **subtle inconsistencies, edge cases, and implementation details** that developers need to be aware of when working across diverse platforms.

It turns out JSON isn’t **quite as universal in practice** as the spec would suggest. Who knew?

## The Promise vs. Reality: The JSON Specification Strikes Back

The JSON specification (RFC 7159/8259) is simple: objects, arrays, strings, numbers, booleans, and null. Six data types. Clean syntax. No namespace nightmares. No schema validation headaches. Just **pure data representation**.

This **simplicity was supposed to be JSON’s superpower**. Unlike XML with its verbose tags and complex parsing rules, JSON promised to be the data format that just worked everywhere. Write once, parse anywhere. But there is always a downside with simple things: **they tend to leave room for interpretation**. And when different languages and libraries start interpreting things differently, your “universal” data format becomes a bit less universal.

Consider this perfectly valid JSON:

```
<span><span ne="0.45672245465181527">{</span></span>
<span><span ne="0.1447987086380088">  "id"</span><span ne="0.6188972962743342">: </span><span ne="0.601005570370656">9007199254740993</span><span ne="0.1136094456270208">,</span></span>
<span><span ne="0.06940741326786237">  "timestamp"</span><span ne="0.6463394955056438">: </span><span ne="0.06202527662861346">"2023-12-25T10:30:00Z"</span><span ne="0.1481178475027778">, </span></span>
<span><span ne="0.3309468620920313">  "temperature"</span><span ne="0.18734733697446782">: </span><span ne="0.9524360339272916">23.1</span><span ne="0.40590116186361735">,</span></span>
<span><span ne="0.774579205756501">  "readings"</span><span ne="0.42423245926669506">: [</span><span ne="0.9823623083882532">null</span><span ne="0.8444354905709617">, </span><span ne="0.1863470137551937">"test"</span><span ne="0.5259197285527906">],</span></span>
<span><span ne="0.41350695528148984">  "metadata"</span><span ne="0.41999596589738386">: {</span></span>
<span><span ne="0.775569053754198">    "sensor"</span><span ne="0.6221263642884218">: </span><span ne="0.8938810513888195">"室温"</span><span ne="0.643270954132428">,</span></span>
<span><span ne="0.9946248228218314">    "location"</span><span ne="0.7995179400891514">: </span><span ne="0.8354086974497147">"café"</span></span>
<span><span ne="0.10634669940379116">  }</span></span>
<span><span ne="0.6932172177222935">}</span></span>
```

Your frontend parses this without complaint. Your backend processes it successfully. Your data pipeline ingests it just fine. But this **harmony is an illusion**. That **integer just lost precision** in JavaScript. The **timestamp means different things** to different parsers, UTC here, local time there, plain string somewhere else. And those Unicode characters in your metadata? Depends on the **normalization strategy**.

What appeared simple at first glance reveals a host of **subtle interoperability pitfalls**. The **JSON specification didn’t break**, it just **left certain details open**. Different **languages and libraries filled in those blanks differently**, and suddenly we’ve got a new Tower of Babel: everyone speaks JSON, but not everyone means the same thing.

## The Number Nightmare: Do Androids Dream of Electric Integers?

### Integer Precision Hell: HAL 9000’s Arithmetic Error

JavaScript represents all numbers as 64-bit floating-point values. This means integers larger than `Number.MAX_SAFE_INTEGER` (2^53 - 1 = 9007199254740991) lose precision:

```
<span><span ne="0.8293511346490123">// JavaScript</span></span>
<span><span ne="0.9905364822042931">console.</span><span ne="0.03910170064122209">log</span><span ne="0.0018061361760931538">(</span><span ne="0.20488813427667918">JSON</span><span ne="0.7442380834903057">.</span><span ne="0.9250338553587123">parse</span><span ne="0.6160217299963573">(</span><span ne="0.5568712949529427">'{"id": 9007199254740992}'</span><span ne="0.16752186132040714">).id </span><span ne="0.8329887917847807">===</span><span ne="0.37703712254284805"> 9007199254740992</span><span ne="0.5568940915027797">); </span><span ne="0.2476782426348647">// true (this is MAX_SAFE_INTEGER + 1, but still representable)</span></span>
<span><span ne="0.051310319976981544">console.</span><span ne="0.14255207960623362">log</span><span ne="0.4672975982469104">(</span><span ne="0.7607271156188162">JSON</span><span ne="0.06056138622712359">.</span><span ne="0.4799490831254022">parse</span><span ne="0.5794364069748312">(</span><span ne="0.928788425075963">'{"id": 9007199254740992}'</span><span ne="0.006646927510287282">).id);                      </span><span ne="0.49121124621886003">// 9007199254740992</span></span>
<span></span>
<span><span ne="0.9399773711441554">// The precision loss happens at larger values</span></span>
<span><span ne="0.4832525015915903">console.</span><span ne="0.8552881392057892">log</span><span ne="0.0482992739985203">(</span><span ne="0.12209889754156411">JSON</span><span ne="0.6293736333066146">.</span><span ne="0.37524245600936224">parse</span><span ne="0.9230946513685869">(</span><span ne="0.1139111003886687">'{"id": 9007199254740993}'</span><span ne="0.5408140994042812">).id </span><span ne="0.5918444399009697">===</span><span ne="0.039107333845393666"> 9007199254740993</span><span ne="0.2743334601311129">); </span><span ne="0.5586122285516151">// true because they bot get downscaled to 9007199254740992!</span></span>
<span><span ne="0.24417919648527286">console.</span><span ne="0.4904517773956325">log</span><span ne="0.8240137780049451">(</span><span ne="0.9700489450076007">JSON</span><span ne="0.5472665609523636">.</span><span ne="0.7365443449281802">parse</span><span ne="0.2267363120863498">(</span><span ne="0.8512146917277651">'{"id": 9007199254740993}'</span><span ne="0.8848243958236383">).id);                      </span><span ne="0.31469096950016817">// 9007199254740992 (wrong!)</span></span>
<span></span>
<span><span ne="0.2637627851422244">// At the limit, adding 1 doesn't change the value</span></span>
<span><span ne="0.00563489089015301">const</span><span ne="0.503888109282681"> parsed</span><span ne="0.947485858111864"> =</span><span ne="0.8571054530836696"> JSON</span><span ne="0.08654776204416981">.</span><span ne="0.17118238220837334">parse</span><span ne="0.8440170166505008">(</span><span ne="0.644752662070683">'{"id": 9007199254740992}'</span><span ne="0.32615234627425316">).id;</span></span>
<span><span ne="0.3509181363724885">console.</span><span ne="0.3715481181545889">log</span><span ne="0.995653114796198">(parsed </span><span ne="0.5591054180968114">+</span><span ne="0.6857992253829258"> 1</span><span ne="0.40566650378027524"> ===</span><span ne="0.20761310934732757"> parsed);     </span><span ne="0.4555944687085417">// true because they both get downscaled to 9007199254740992</span></span>
<span><span ne="0.4989921023532997">console.</span><span ne="0.3488581516433842">log</span><span ne="0.2812090371998398">(parsed </span><span ne="0.42541020472019386">+</span><span ne="0.28075330554129185"> 2</span><span ne="0.5123467035917804">);                </span><span ne="0.1865822192774138">// 9007199254740994 (works but skips odd numbers above MAX_SAFE_INTEGER)</span></span>
```

But in Python, those same JSON values parse perfectly:

```
<span><span ne="0.9370816594577333"># Python</span></span>
<span><span ne="0.8759187323129981">import</span><span ne="0.03680425753353245"> json</span></span>
<span><span ne="0.587829291434413">data </span><span ne="0.12136834860992463">=</span><span ne="0.6575563108778869"> json.loads(</span><span ne="0.544161705318563">'{"id": 9007199254740993}'</span><span ne="0.48931173903141567">)</span></span>
<span><span ne="0.991682415746679">print</span><span ne="0.6403858826624472">(data[</span><span ne="0.8736580021333141">'id'</span><span ne="0.7278916565983082">] </span><span ne="0.4349858810384737">==</span><span ne="0.30659957017816586"> 9007199254740993</span><span ne="0.3742786045019909">)  </span><span ne="0.03516337701757433"># True</span></span>
<span><span ne="0.7899071538182124">print</span><span ne="0.5428872915964835">(data[</span><span ne="0.29925382711773774">'id'</span><span ne="0.5039204691452349">])                      </span><span ne="0.3312731618839345"># 9007199254740993</span></span>
```

And in Go, it depends on what type you unmarshal into:

```
<span><span ne="0.7928444851310357">// Go - loses precision with interface{}</span></span>
<span><span ne="0.8073923456891992">package</span><span ne="0.14731298886372546"> main</span></span>
<span><span ne="0.21431110699345002">import</span><span ne="0.8472159856618635"> (</span></span>
<span><span ne="0.7005001741595133">    "</span><span ne="0.4950968125163011">encoding/json</span><span ne="0.7961655884222726">"</span></span>
<span><span ne="0.8841838050696825">    "</span><span ne="0.017936489135905842">fmt</span><span ne="0.67688003719163">"</span></span>
<span><span ne="0.22670073240832644">)</span></span>
<span></span>
<span><span ne="0.686681177720064">func</span><span ne="0.017391868723000914"> main</span><span ne="0.7801491525280136">() {</span></span>
<span><span ne="0.10556862911286369">    var</span><span ne="0.8902670440033182"> data </span><span ne="0.9106294000257522">map</span><span ne="0.28724101348630593">[</span><span ne="0.354897258012848">string</span><span ne="0.23264052386450806">]</span><span ne="0.34531274121131217">interface</span><span ne="0.9200478235148837">{}</span></span>
<span><span ne="0.7966172061886166">    json.</span><span ne="0.04336108802634231">Unmarshal</span><span ne="0.7040309496093937">([]</span><span ne="0.3712555813458306">byte</span><span ne="0.7531538214516438">(</span><span ne="0.5326792111624082">`{"id": 9007199254740993}`</span><span ne="0.08425144712008614">), </span><span ne="0.41660272675310916">&amp;</span><span ne="0.6273670046009088">data)</span></span>
<span><span ne="0.11806092598316409">    fmt.</span><span ne="0.16415674455550122">Printf</span><span ne="0.468010218785921">(</span><span ne="0.440490505211493">"</span><span ne="0.06768227665426285">%.0f\n</span><span ne="0.32966365942544096">"</span><span ne="0.6522616016696435">, data[</span><span ne="0.9942455348078938">"id"</span><span ne="0.6125431976760206">].(</span><span ne="0.16743866008654607">float64</span><span ne="0.7971470924156628">)) </span><span ne="0.950911811245886">// 9007199254740992 - precision lost!</span></span>
<span><span ne="0.5923696864435032">    </span></span>
<span><span ne="0.1866349086021526">    // But correct with explicit int64</span></span>
<span><span ne="0.9590984640024064">    var</span><span ne="0.5880929294155993"> typed </span><span ne="0.2989416343870771">struct</span><span ne="0.6404034467325745"> {</span></span>
<span><span ne="0.081947443797594">        ID </span><span ne="0.8685079111549522">int64</span><span ne="0.6670642348050572"> `json:"id"`</span></span>
<span><span ne="0.5731276153427965">    }</span></span>
<span><span ne="0.2336034791981736">    json.</span><span ne="0.6793741009281536">Unmarshal</span><span ne="0.6187310257289848">([]</span><span ne="0.275063927235927">byte</span><span ne="0.49066634735866643">(</span><span ne="0.16475392219504947">`{"id": 9007199254740993}`</span><span ne="0.7198826000004416">), </span><span ne="0.7737697756145272">&amp;</span><span ne="0.5959478499422178">typed)</span></span>
<span><span ne="0.006455346539828599">    fmt.</span><span ne="0.03745216905597304">Println</span><span ne="0.21892549853326593">(typed.ID) </span><span ne="0.00291989561548478">// 9007199254740993 - correct!</span></span>
<span><span ne="0.5474820050827263">}</span></span>
```

In Java with Jackson:

```
<span><span ne="0.5459299854593622">// Java with Jackson - precision is generally preserved</span></span>
<span></span>
<span><span ne="0.4727154812371508">import</span><span ne="0.05848295796503922"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.16583947723679981">import</span><span ne="0.5132572240691541"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span></span>
<span><span ne="0.11922296489790218">import</span><span ne="0.04038615139012314"> java.util.Map;</span></span>
<span><span ne="0.44330768551899435">import</span><span ne="0.6307390752808988"> java.util.HashMap;</span></span>
<span></span>
<span><span ne="0.529078524307536">public</span><span ne="0.7950190219851542"> class</span><span ne="0.6197122122734882"> JsonPrecisionDemo</span><span ne="0.9060556529152682"> {</span></span>
<span><span ne="0.5127226086765663">    static</span><span ne="0.5405498663090015"> class</span><span ne="0.9732475206365867"> Data</span><span ne="0.47469771409343553"> {</span></span>
<span><span ne="0.8353135983709952">        public</span><span ne="0.05816789097769892"> long</span><span ne="0.4284405668964737"> id;</span></span>
<span><span ne="0.2423523133974489">    }</span></span>
<span></span>
<span><span ne="0.6554763263155278">    public</span><span ne="0.6480741781123972"> static</span><span ne="0.47331267365096863"> void</span><span ne="0.8206063577965276"> main</span><span ne="0.08552250213118551">(</span><span ne="0.894521014315109">String</span><span ne="0.9265908134092321">[] </span><span ne="0.03249359205778024">args</span><span ne="0.2922191245782232">) </span><span ne="0.13114313923488485">throws</span><span ne="0.5757281744128718"> Exception {</span></span>
<span><span ne="0.9131099410328208">        ObjectMapper mapper </span><span ne="0.46665740657334853">=</span><span ne="0.6765251399624613"> new</span><span ne="0.12950789713270083"> ObjectMapper</span><span ne="0.3249893035491892">();</span></span>
<span></span>
<span><span ne="0.7062307892893291">        // Jackson handles long integers correctly within Java's long range</span></span>
<span><span ne="0.35855563331498697">        JsonNode node </span><span ne="0.9692201671962184">=</span><span ne="0.34244715631633516"> mapper.</span><span ne="0.26011716441112676">readTree</span><span ne="0.04449190123395752">(</span><span ne="0.6110247176127551">"{</span><span ne="0.6489088763798941">\"</span><span ne="0.3611572263874342">id</span><span ne="0.32721944604227005">\"</span><span ne="0.2687906378398194">: 9007199254740993}"</span><span ne="0.45471243718170185">);</span></span>
<span><span ne="0.2850633228055054">        System.out.</span><span ne="0.18143869325872886">println</span><span ne="0.8429234853297982">(node.</span><span ne="0.7526977327863865">get</span><span ne="0.5421146888713056">(</span><span ne="0.8485764950830901">"id"</span><span ne="0.06620267174509797">).</span><span ne="0.5477589694627183">longValue</span><span ne="0.4497759267388487">()); </span><span ne="0.07811762996062133">// 9007199254740993 (correct)</span></span>
<span></span>
<span><span ne="0.869736132014362">        // Map also preserves precision for this value</span></span>
<span><span ne="0.2573102783097908">        Map&lt;</span><span ne="0.4694767253077382">String</span><span ne="0.2642564151154003">, </span><span ne="0.32381122253123074">Object</span><span ne="0.38997440905643865">&gt; map </span><span ne="0.6901264794217902">=</span><span ne="0.8106337920701655"> mapper.</span><span ne="0.31717993975889236">readValue</span><span ne="0.30385468317787845">(</span><span ne="0.7506925895990134">"{</span><span ne="0.15602906517923665">\"</span><span ne="0.6399134714407317">id</span><span ne="0.040272421406960524">\"</span><span ne="0.15331882919717732">: 9007199254740993}"</span><span ne="0.35685914297144705">, HashMap.class);</span></span>
<span><span ne="0.7515041511620998">        System.out.</span><span ne="0.8612354133514138">println</span><span ne="0.7282185137591348">(map.</span><span ne="0.6937320044038648">get</span><span ne="0.45245629182458746">(</span><span ne="0.8061263617463118">"id"</span><span ne="0.4486255419090064">));              </span><span ne="0.3689929932274302">// 9007199254740993 (correct)</span></span>
<span></span>
<span><span ne="0.015821041942762015">        // Even very large numbers within long range are handled correctly</span></span>
<span><span ne="0.0722279717462021">        Map&lt;</span><span ne="0.7744475832652349">String</span><span ne="0.00896583053012745">, </span><span ne="0.6024448118116045">Object</span><span ne="0.7311382458318241">&gt; bigMap </span><span ne="0.7073891852148183">=</span><span ne="0.8537382877876066"> mapper.</span><span ne="0.5488631590771912">readValue</span><span ne="0.6661868079240825">(</span><span ne="0.9520847600410656">"{</span><span ne="0.7514640807334826">\"</span><span ne="0.39113370691018157">id</span><span ne="0.4373116248995087">\"</span><span ne="0.7244537708597368">: 9223372036854775807}"</span><span ne="0.9366640119391713">, HashMap.class);</span></span>
<span><span ne="0.37736346858983516">        System.out.</span><span ne="0.000211782459620391">println</span><span ne="0.5904316863483446">(bigMap.</span><span ne="0.2921244939271259">get</span><span ne="0.054871538599947756">(</span><span ne="0.8064929892768007">"id"</span><span ne="0.07923136101951711">));           </span><span ne="0.9365007531671699">// 9223372036854775807 (Long.MAX_VALUE)</span></span>
<span></span>
<span><span ne="0.413787306460737">        // Using specific type also works</span></span>
<span><span ne="0.747306024139403">        Data data </span><span ne="0.5554684401101072">=</span><span ne="0.1902445563166142"> mapper.</span><span ne="0.1875501342654382">readValue</span><span ne="0.26156333194609116">(</span><span ne="0.506947034595037">"{</span><span ne="0.7576870931175027">\"</span><span ne="0.7218092647250545">id</span><span ne="0.7789227656775368">\"</span><span ne="0.11237602095131416">: 9007199254740993}"</span><span ne="0.47910423624336695">, Data.class);</span></span>
<span><span ne="0.1563039190978387">        System.out.</span><span ne="0.8702172694679405">println</span><span ne="0.6021862537265579">(data.id);                    </span><span ne="0.7371083772160685">// 9007199254740993</span></span>
<span></span>
<span><span ne="0.9907251787346185">        // Jackson only has issues with numbers beyond Java's native ranges</span></span>
<span><span ne="0.6942030119905769">        // For numbers larger than Long.MAX_VALUE, you'd need BigInteger handling</span></span>
<span><span ne="0.09328503854750547">    }</span></span>
<span><span ne="0.4328155335974825">}</span></span>
```

This inconsistency has **real-world consequences**. Database IDs, timestamps, and financial calculations can all be silently corrupted when crossing language boundaries.

### Decimal Precision Variations: The Floating Point Mentat Problem

While this is fundamentally an IEEE 754 floating-point issue rather than a JSON parsing inconsistency, it’s critical for developers to understand when working with **financial data, measurements, or any calculations** requiring exact decimal precision:

```
<span><span ne="0.26937852922731853">{</span></span>
<span><span ne="0.5887857968448748">  "price"</span><span ne="0.8949347992116602">: </span><span ne="0.5121877122407603">0.1</span></span>
<span><span ne="0.26808263484766504">}</span></span>
```

```
<span><span ne="0.6225088626596871">// JavaScript</span></span>
<span><span ne="0.7544397756736554">console.</span><span ne="0.3142734592692519">log</span><span ne="0.8941537689857237">(</span><span ne="0.7639418202499098">JSON</span><span ne="0.6640377708399723">.</span><span ne="0.4613343609778925">parse</span><span ne="0.9564528666634587">(</span><span ne="0.7920631505639735">'{"price": 0.1}'</span><span ne="0.27962320742474156">).price </span><span ne="0.8660835404409999">===</span><span ne="0.6526018570021359"> 0.1</span><span ne="0.024706197164079402">);  </span><span ne="0.37693647229215466">// true</span></span>
<span><span ne="0.3426493672805402">console.</span><span ne="0.04431822346117653">log</span><span ne="0.36500406340821046">(</span><span ne="0.2939398424188604">JSON</span><span ne="0.7632531920313045">.</span><span ne="0.9245759718659007">parse</span><span ne="0.90344164174605">(</span><span ne="0.02924967396049638">'{"price": 0.1}'</span><span ne="0.9404434044764521">).price);          </span><span ne="0.6477799839172037">// 0.1</span></span>
<span></span>
<span><span ne="0.4493639127538367">// The floating-point precision issue becomes apparent with arithmetic:</span></span>
<span><span ne="0.9908875567835392">const</span><span ne="0.09713899319001607"> price</span><span ne="0.9133441507079418"> =</span><span ne="0.23603007820744093"> JSON</span><span ne="0.8604674385777091">.</span><span ne="0.10117089459852724">parse</span><span ne="0.3326384502113632">(</span><span ne="0.41728247984928335">'{"price": 0.1}'</span><span ne="0.864239440667186">).price;</span></span>
<span><span ne="0.9715420377241119">console.</span><span ne="0.688676903848336">log</span><span ne="0.11005095617965777">(price </span><span ne="0.912638577522708">+</span><span ne="0.6660821880409769"> 0.2</span><span ne="0.4148279619784735">);                                 </span><span ne="0.21576653508504795">// 0.30000000000000004</span></span>
```

```
<span><span ne="0.8452740443576197"># Python (default json module)</span></span>
<span><span ne="0.7294630453952307">import</span><span ne="0.34624723027134374"> json</span></span>
<span><span ne="0.3736141611459791">data </span><span ne="0.2744726246552388">=</span><span ne="0.06635237164038466"> json.loads(</span><span ne="0.6304192505133567">'{"price": 0.1}'</span><span ne="0.6182217820838735">)</span></span>
<span><span ne="0.955580090871234">print</span><span ne="0.5963058407731365">(data[</span><span ne="0.06115941874947284">'price'</span><span ne="0.5265818916978057">])                    </span><span ne="0.41303319059696564"># 0.1</span></span>
<span><span ne="0.7530758483495303">print</span><span ne="0.015173265311424489">(data[</span><span ne="0.13624475979940598">'price'</span><span ne="0.7106168963517182">] </span><span ne="0.6644410179334785">+</span><span ne="0.5437539316504403"> 0.2</span><span ne="0.3704168200347986">)              </span><span ne="0.5232628826847521"># 0.30000000000000004</span></span>
<span></span>
<span><span ne="0.7647344095418108"># Python with Decimal for precision</span></span>
<span><span ne="0.8992331131187041">import</span><span ne="0.9404523290969976"> json</span></span>
<span><span ne="0.6831531189787637">from</span><span ne="0.6765720784052891"> decimal </span><span ne="0.9087630414660204">import</span><span ne="0.4133645502243055"> Decimal</span></span>
<span><span ne="0.8423508809992022">data </span><span ne="0.3482797031147712">=</span><span ne="0.5912847639167609"> json.loads(</span><span ne="0.8253336088962218">'{"price": 0.1}'</span><span ne="0.7243625848421757">, </span><span ne="0.7489150755312612">parse_float</span><span ne="0.9005493970422759">=</span><span ne="0.720637903216068">Decimal)</span></span>
<span><span ne="0.141663966099995">print</span><span ne="0.24667902435199374">(data[</span><span ne="0.9872373230061111">'price'</span><span ne="0.9960696983103148">])                    </span><span ne="0.7523279817134925"># 0.1</span></span>
<span><span ne="0.3095782133434991">print</span><span ne="0.6009527602156711">(</span><span ne="0.3030616767020331">type</span><span ne="0.6136036260726585">(data[</span><span ne="0.9000860708405417">'price'</span><span ne="0.0700842638182001">]))              </span><span ne="0.4916322820475769"># &lt;class 'decimal.Decimal'&gt;</span></span>
<span><span ne="0.8792910961001407">print</span><span ne="0.935800632849029">(data[</span><span ne="0.8275219040549986">'price'</span><span ne="0.34361653576984097">] </span><span ne="0.26501331104477455">+</span><span ne="0.28032855125502454"> Decimal(</span><span ne="0.6555541324306834">'0.2'</span><span ne="0.7436233006002445">))   </span><span ne="0.07908268714811661"># 0.3</span></span>
```

```
<span><span ne="0.9360443978911258">// Java with Jackson - decimal precision</span></span>
<span></span>
<span><span ne="0.02083579601204677">import</span><span ne="0.8816652632631339"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.011352884601092739">import</span><span ne="0.9675372936401542"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span><span ne="0.07187365332850049">import</span><span ne="0.6815626973627759"> com.fasterxml.jackson.databind.DeserializationFeature;</span></span>
<span></span>
<span><span ne="0.2567882526785362">public</span><span ne="0.22541461440148103"> class</span><span ne="0.42715896168815315"> JsonDecimalDemo</span><span ne="0.912936418012738"> {</span></span>
<span><span ne="0.7580337854501207">    public</span><span ne="0.8535517385371063"> static</span><span ne="0.5712297608566532"> void</span><span ne="0.7011291961013588"> main</span><span ne="0.26989893817726796">(</span><span ne="0.004930849722696973">String</span><span ne="0.3176866867742456">[] </span><span ne="0.46919514613872715">args</span><span ne="0.7104411854264467">) </span><span ne="0.12185035038355352">throws</span><span ne="0.44313035701319126"> Exception {</span></span>
<span><span ne="0.792112903914517">        ObjectMapper mapper </span><span ne="0.36721442905862645">=</span><span ne="0.3305755557502824"> new</span><span ne="0.017532117136646708"> ObjectMapper</span><span ne="0.07444694816281194">();</span></span>
<span><span ne="0.01706016956459422">        JsonNode node </span><span ne="0.34775582623563805">=</span><span ne="0.3865745364131107"> mapper.</span><span ne="0.8778054543214232">readTree</span><span ne="0.10157389578246434">(</span><span ne="0.1802004373576298">"{</span><span ne="0.19257772221680036">\"</span><span ne="0.18591978445536816">price</span><span ne="0.7056912977652016">\"</span><span ne="0.2311023027170318">: 0.1}"</span><span ne="0.41368119111536183">);</span></span>
<span></span>
<span><span ne="0.16652855114604614">        System.out.</span><span ne="0.9377898812895255">println</span><span ne="0.4928196243024714">(node.</span><span ne="0.9062510012804941">get</span><span ne="0.36440238886336285">(</span><span ne="0.5987155642585527">"price"</span><span ne="0.40129764504495324">).</span><span ne="0.39895887387008444">doubleValue</span><span ne="0.4296470197805531">());      </span><span ne="0.9181401806801655">// 0.1</span></span>
<span><span ne="0.6967114774224888">        System.out.</span><span ne="0.7259807200305963">println</span><span ne="0.08713091807341644">(node.</span><span ne="0.024478633807163308">get</span><span ne="0.27564803818469663">(</span><span ne="0.8626499902500536">"price"</span><span ne="0.3305507669443494">).</span><span ne="0.09653145866165647">doubleValue</span><span ne="0.09661356572766533">() </span><span ne="0.7151506799746051">+</span><span ne="0.7004841701074015"> 0.2</span><span ne="0.21147217713220268">); </span><span ne="0.8687398260483331">// 0.30000000000000004</span></span>
<span></span>
<span><span ne="0.2128319754605532">        // Using BigDecimal for precision - need to enable the feature</span></span>
<span><span ne="0.08317002580239774">        mapper.</span><span ne="0.27507713365912567">configure</span><span ne="0.7611450636679509">(DeserializationFeature.USE_BIG_DECIMAL_FOR_FLOATS, </span><span ne="0.2660338583729832">true</span><span ne="0.15397282022272352">);</span></span>
<span><span ne="0.521210420000349">        JsonNode preciseNode </span><span ne="0.3151234326350354">=</span><span ne="0.9334717072734737"> mapper.</span><span ne="0.6314875036379756">readTree</span><span ne="0.1872338507082747">(</span><span ne="0.5089547690245112">"{</span><span ne="0.39123401488892084">\"</span><span ne="0.5032196523357471">price</span><span ne="0.011658775635700502">\"</span><span ne="0.0407349505745388">: 0.1}"</span><span ne="0.7992912251790408">);</span></span>
<span><span ne="0.9647218212697033">        System.out.</span><span ne="0.92102120149921">println</span><span ne="0.3566389412093821">(preciseNode.</span><span ne="0.19289118139876726">get</span><span ne="0.2893732936236889">(</span><span ne="0.7841488960126067">"price"</span><span ne="0.6224255701502874">).</span><span ne="0.7148394440686111">decimalValue</span><span ne="0.30138199243758224">()); </span><span ne="0.09798275728191408">// 0.1 (as BigDecimal)</span></span>
<span><span ne="0.8637680082307644">        System.out.</span><span ne="0.2946520145598345">println</span><span ne="0.5590090870005403">(preciseNode.</span><span ne="0.006716343481712239">get</span><span ne="0.08643813082672014">(</span><span ne="0.1976367407491979">"price"</span><span ne="0.5992036749919856">).</span><span ne="0.83936124905641">decimalValue</span><span ne="0.5594305697376992">().</span><span ne="0.44454349954868544">add</span><span ne="0.12031684825734201">(</span></span>
<span><span ne="0.5308033120272865">                new</span><span ne="0.9712939716579881"> java.math.</span><span ne="0.9949834196444123">BigDecimal</span><span ne="0.8914947489332163">(</span><span ne="0.0683001335489104">"0.2"</span><span ne="0.6982606982449922">))); </span><span ne="0.13240552625949165">// 0.3 (exact)</span></span>
<span><span ne="0.2210668158457918">    }</span></span>
<span><span ne="0.3036005661658223">}</span></span>
```

```
<span><span ne="0.37023787489992266">// C# with System.Text.Json</span></span>
<span><span ne="0.5822677016082082">using</span><span ne="0.8592019953401169"> System</span><span ne="0.6980650407778286">;</span></span>
<span><span ne="0.7005085768550551">using</span><span ne="0.4636875946687161"> System</span><span ne="0.7378665772340388">.</span><span ne="0.5572129809098638">Text</span><span ne="0.8161147696331222">.</span><span ne="0.24221234036833017">Json</span><span ne="0.33770164503709343">;</span></span>
<span></span>
<span><span ne="0.12414329858043116">class</span><span ne="0.04499366981479913"> JsonPrecisionDemo</span><span ne="0.16354206093547097"> </span></span>
<span><span ne="0.25784091667558395">{</span></span>
<span><span ne="0.19190566008313636">    static</span><span ne="0.42865134711115493"> void</span><span ne="0.1204839061329348"> Main</span><span ne="0.22654966013761846">() </span></span>
<span><span ne="0.013098733727501366">    {</span></span>
<span><span ne="0.12571967884002588">        var</span><span ne="0.6896582338817645"> json</span><span ne="0.3983795593342202"> =</span><span ne="0.4981946549242424"> """{"price": 0.1}"""</span><span ne="0.6912597019762984">;</span></span>
<span><span ne="0.7931665202838445">        var</span><span ne="0.7134816410763636"> doc</span><span ne="0.3795995845121305"> =</span><span ne="0.012249449576130389"> JsonDocument.</span><span ne="0.9825572490360176">Parse</span><span ne="0.48159772338767903">(json);</span></span>
<span><span ne="0.037999097947571725">        double</span><span ne="0.6907299468878627"> price</span><span ne="0.45702002085270677"> =</span><span ne="0.7921902010574942"> doc.RootElement.</span><span ne="0.19831616290184473">GetProperty</span><span ne="0.652359887508863">(</span><span ne="0.33362254532008906">"price"</span><span ne="0.10641418831946081">).</span><span ne="0.759260481244371">GetDouble</span><span ne="0.03940246415228843">();</span></span>
<span><span ne="0.21943556535583375">        Console.</span><span ne="0.6340205150001484">WriteLine</span><span ne="0.4252231077859975">(price);           </span><span ne="0.1747112663495325">// 0.1</span></span>
<span><span ne="0.135067138543136">        Console.</span><span ne="0.5342475937076299">WriteLine</span><span ne="0.01542123111222482">(price </span><span ne="0.8487790015042773">+</span><span ne="0.04649827692642272"> 0.2</span><span ne="0.46748133236980816">);     </span><span ne="0.3889463031369863">// 0.30000000000000004</span></span>
<span></span>
<span><span ne="0.3009324083719992">        // Using decimal for precision would require custom converter</span></span>
<span><span ne="0.8096449472091016">        doc.</span><span ne="0.99908772501567">Dispose</span><span ne="0.6053700545850096">();</span></span>
<span><span ne="0.3307671149910204">    }</span></span>
<span><span ne="0.5591080493568139">}</span></span>
```

I think it’s important to underly it again: **it’s critical for financial applications**. It can cause serious issues where exact decimal precision is required. Always use dedicated decimal types (Python’s `Decimal`, Java’s `BigDecimal`, JavaScript’s decimal libraries) for monetary calculations, never rely on JSON’s default number parsing for currency values.

## String Encoding Chaos: The Babel Fish Encoding Protocol

### Unicode Normalization: Ghost in the Shell Character Set

JSON strings can contain Unicode, but different languages handle normalization differently:

```
<span><span ne="0.9294292900620883">{</span></span>
<span><span ne="0.24368244281369056">  "name"</span><span ne="0.8140430468695481">: </span><span ne="0.7592216936626923">"José"</span></span>
<span><span ne="0.8062164617535983">}</span></span>
```

The character “é” can be represented as:

-   A single codepoint: U+00E9 (é)
-   Composed form: U+0065 U+0301 (e + ́)

```
<span><span ne="0.19234074635685705"># Python</span></span>
<span><span ne="0.23985607645089824">import</span><span ne="0.885038758690849"> json</span></span>
<span><span ne="0.324212736001126">import</span><span ne="0.4847740886980517"> unicodedata</span></span>
<span></span>
<span><span ne="0.04264705947936953"># These are different byte sequences but visually identical</span></span>
<span><span ne="0.3909614065338617">name1 </span><span ne="0.5967081931233303">=</span><span ne="0.5919993423648244"> "José"</span><span ne="0.7436316635165396">                    # Single codepoint é (U+00E9)</span></span>
<span><span ne="0.12614564552046814">name2 </span><span ne="0.9820790532414729">=</span><span ne="0.6064116061301942"> "Jose</span><span ne="0.5428289075546732">\u0301</span><span ne="0.656680432073947">"</span><span ne="0.20290059189823217">             # e (U+0065) + combining acute accent (U+0301)</span></span>
<span></span>
<span><span ne="0.5760852616314582">print</span><span ne="0.44971081057339934">(name1 </span><span ne="0.9316051072231744">==</span><span ne="0.19454785276365327"> name2)            </span><span ne="0.8225977864247822"># False</span></span>
<span><span ne="0.8950282066108795">print</span><span ne="0.8923373313439665">(</span><span ne="0.7612429576410643">len</span><span ne="0.8784148424441677">(name1), </span><span ne="0.44515518275644816">len</span><span ne="0.4079461066377541">(name2))    </span><span ne="0.5458827516304714"># 4 5</span></span>
<span></span>
<span><span ne="0.607414953503234">json_str1 </span><span ne="0.44429706497024346">=</span><span ne="0.4007471261244314"> json.dumps({</span><span ne="0.6977278765779008">"name"</span><span ne="0.043961867356143824">: name1})</span></span>
<span><span ne="0.12386520505722365">json_str2 </span><span ne="0.944067227353779">=</span><span ne="0.9841448170689063"> json.dumps({</span><span ne="0.6524228664850658">"name"</span><span ne="0.4136501797785377">: name2})</span></span>
<span><span ne="0.4491468351825114">print</span><span ne="0.8430918216679621">(json_str1 </span><span ne="0.2137578220992068">==</span><span ne="0.16767618595744382"> json_str2)   </span><span ne="0.014156640118301866"># False!</span></span>
<span></span>
<span><span ne="0.965129462123791"># But after normalization:</span></span>
<span><span ne="0.946215934402359">normalized1 </span><span ne="0.18517323107721184">=</span><span ne="0.8635045291493593"> unicodedata.normalize(</span><span ne="0.3594281293519762">'NFC'</span><span ne="0.5872171033957292">, name1)</span></span>
<span><span ne="0.7473679133750194">normalized2 </span><span ne="0.7503036153860714">=</span><span ne="0.8792020819732441"> unicodedata.normalize(</span><span ne="0.0070302183190172896">'NFC'</span><span ne="0.13583279929544279">, name2)</span></span>
<span><span ne="0.3675845251770954">print</span><span ne="0.09287457684952738">(normalized1 </span><span ne="0.9848376166825238">==</span><span ne="0.9499768134722498"> normalized2) </span><span ne="0.284067003153918"># True</span></span>
```

```
<span><span ne="0.8607315290475771">// JavaScript</span></span>
<span><span ne="0.28466703773009616">const</span><span ne="0.8495228828790593"> name1</span><span ne="0.010386654665803019"> =</span><span ne="0.3783436692495695"> "José"</span><span ne="0.9891805198445546">;           </span><span ne="0.15706762524067486">// Single codepoint</span></span>
<span><span ne="0.5423246861289658">const</span><span ne="0.06992004789016071"> name2</span><span ne="0.8906523581573162"> =</span><span ne="0.04830693906501771"> "Jose</span><span ne="0.376246515686661">\u0301</span><span ne="0.5536404707076005">"</span><span ne="0.8650456893247195">;     </span><span ne="0.9869481365998038">// Composed form</span></span>
<span></span>
<span><span ne="0.5262333555895553">console.</span><span ne="0.0350601094016455">log</span><span ne="0.38980721566742693">(name1 </span><span ne="0.9609113479048714">===</span><span ne="0.26619515664282567"> name2);   </span><span ne="0.7693367080903302">// false</span></span>
<span><span ne="0.05580075976212728">console.</span><span ne="0.4257865669346277">log</span><span ne="0.3893325332970926">(name1.</span><span ne="0.6885460312180315">length</span><span ne="0.846109276384984">, name2.</span><span ne="0.5414553742211222">length</span><span ne="0.41826250827061884">); </span><span ne="0.7932612836754471">// 4 5</span></span>
<span></span>
<span><span ne="0.6597029977768925">console.</span><span ne="0.3016278736311777">log</span><span ne="0.5978905543926792">(</span><span ne="0.2370813975741649">JSON</span><span ne="0.7574242820716903">.</span><span ne="0.4933176651206602">stringify</span><span ne="0.5992605866738663">({name: name1}) </span><span ne="0.20138202080581868">===</span><span ne="0.49724278863863836"> JSON</span><span ne="0.2959233555139664">.</span><span ne="0.08868838951228286">stringify</span><span ne="0.9032402906141606">({name: name2})); </span><span ne="0.3633270649650955">// false</span></span>
<span></span>
<span><span ne="0.5139492850326978">// Normalization required for comparison</span></span>
<span><span ne="0.5674001532057633">console.</span><span ne="0.11816152561613558">log</span><span ne="0.508664375770225">(name1.</span><span ne="0.944802931435032">normalize</span><span ne="0.6945166299749456">(</span><span ne="0.17712383589708924">'NFC'</span><span ne="0.24625285136795838">) </span><span ne="0.9495107984671128">===</span><span ne="0.5298816318381379"> name2.</span><span ne="0.6922538008125275">normalize</span><span ne="0.9185423691312007">(</span><span ne="0.394189267877035">'NFC'</span><span ne="0.5081040201521555">)); </span><span ne="0.45521350675266126">// true</span></span>
```

```
<span><span ne="0.9888759899121238">// Java</span></span>
<span></span>
<span><span ne="0.2905850536427157">import</span><span ne="0.7404966854299327"> java.text.Normalizer;</span></span>
<span></span>
<span><span ne="0.6702959967843153">public</span><span ne="0.13780775168357562"> class</span><span ne="0.7987097821453534"> UnicodeDemo</span><span ne="0.7637139767136111"> {</span></span>
<span><span ne="0.5178423577084035">    public</span><span ne="0.2555635005686334"> static</span><span ne="0.10819290499631706"> void</span><span ne="0.18332033799403424"> main</span><span ne="0.6233099302293442">(</span><span ne="0.034145918563299404">String</span><span ne="0.9283699367753774">[] </span><span ne="0.3921549922967543">args</span><span ne="0.8780315411478046">) {</span></span>
<span><span ne="0.31466696605758715">        String name1 </span><span ne="0.5344890619684379">=</span><span ne="0.03568349102104984"> "José"</span><span ne="0.19469865417578291">;                    </span><span ne="0.8687893560974872">// Single codepoint</span></span>
<span><span ne="0.7809083836277259">        String name2 </span><span ne="0.47393311230036694">=</span><span ne="0.8227804210542973"> "Jose</span><span ne="0.3626671988268326">\u</span><span ne="0.2150661616918328">0301"</span><span ne="0.5394862749428934">;             </span><span ne="0.557146987847307">// Composed form</span></span>
<span></span>
<span><span ne="0.42081150860693395">        System.out.</span><span ne="0.6996432471200968">println</span><span ne="0.46572383474333856">(name1.</span><span ne="0.9752251196373776">equals</span><span ne="0.6201242284474122">(name2)); </span><span ne="0.6554957586475635">// false</span></span>
<span><span ne="0.5647157076149616">        System.out.</span><span ne="0.9798731616605624">println</span><span ne="0.8767220425528192">(name1.</span><span ne="0.21119823154225192">length</span><span ne="0.1462824284451868">() </span><span ne="0.8683066131389666">+</span><span ne="0.683000127732054"> " "</span><span ne="0.37768901145373546"> +</span><span ne="0.34903855212146007"> name2.</span><span ne="0.8952183559444388">length</span><span ne="0.29370402883774793">()); </span><span ne="0.290769623127367">// 4 5</span></span>
<span></span>
<span><span ne="0.056593405020750054">        // Normalization required</span></span>
<span><span ne="0.45782702490897564">        String norm1 </span><span ne="0.03262084226585693">=</span><span ne="0.31387414653682477"> Normalizer.</span><span ne="0.2473989014224316">normalize</span><span ne="0.6956021623287444">(name1, Normalizer.Form.NFC);</span></span>
<span><span ne="0.8615895890799787">        String norm2 </span><span ne="0.39372706892142495">=</span><span ne="0.7958840671439901"> Normalizer.</span><span ne="0.5180046762977865">normalize</span><span ne="0.2658957295159544">(name2, Normalizer.Form.NFC);</span></span>
<span><span ne="0.5121132450075305">        System.out.</span><span ne="0.5292531552061469">println</span><span ne="0.21997156562602826">(norm1.</span><span ne="0.9093952701955389">equals</span><span ne="0.06929412111935707">(norm2)); </span><span ne="0.6689959686781665">// true</span></span>
<span><span ne="0.1568294472934687">    }</span></span>
<span><span ne="0.8243824258125414">}</span></span>
```

## Object Key Ordering: The Minority Report Hash Collision

JSON specification states that object key order is not significant, but real applications often depend on it. This becomes critical when using JSON for cryptographic operations like HMAC calculations, digital signatures, or content hashing where byte-for-byte consistency is required:

```
<span><span ne="0.2358422644902226">{</span></span>
<span><span ne="0.25603255913874234">  "z"</span><span ne="0.22653952431063462">: </span><span ne="0.38200832612044877">1</span><span ne="0.801193187566025">,</span></span>
<span><span ne="0.8979928834364288">  "a"</span><span ne="0.5846984076033303">: </span><span ne="0.9346853043164659">2</span><span ne="0.24737301735633466">,</span></span>
<span><span ne="0.8743161036529278">  "m"</span><span ne="0.056269041683075005">: </span><span ne="0.23606716741419653">3</span></span>
<span><span ne="0.6863621015731113">}</span></span>
```

```
<span><span ne="0.08449848770093948">// JavaScript (ES2015+)</span></span>
<span><span ne="0.035746782427914514">const</span><span ne="0.7965758684796185"> obj</span><span ne="0.8164393993949617"> =</span><span ne="0.7607321554407043"> JSON</span><span ne="0.10963524117775869">.</span><span ne="0.33961147459730456">parse</span><span ne="0.6242201128862899">(</span><span ne="0.5129033673763571">'{"z": 1, "a": 2, "m": 3}'</span><span ne="0.9086190406707054">);</span></span>
<span><span ne="0.5010448599108448">console.</span><span ne="0.23049918742426334">log</span><span ne="0.4963960369752082">(Object.</span><span ne="0.853325083097957">keys</span><span ne="0.4719109375423154">(obj)); </span><span ne="0.704412107688582">// ['z', 'a', 'm'] - insertion order preserved</span></span>
<span></span>
<span><span ne="0.6708207178441207">// Round trip maintains order</span></span>
<span><span ne="0.4758835362279936">console.</span><span ne="0.31934716160482046">log</span><span ne="0.5017143079957256">(</span><span ne="0.04725168536266977">JSON</span><span ne="0.3738404306872203">.</span><span ne="0.610471941493218">stringify</span><span ne="0.25911444502492664">(obj)); </span><span ne="0.7968960795257976">// {"z":1,"a":2,"m":3}</span></span>
```

```
<span><span ne="0.026497767050760568"># Python 3.7+</span></span>
<span><span ne="0.3328530781169534">import</span><span ne="0.31755102561341375"> json</span></span>
<span></span>
<span><span ne="0.07513226162156073">data </span><span ne="0.053720272932691104">=</span><span ne="0.9260984603015754"> json.loads(</span><span ne="0.0913939437335981">'{"z": 1, "a": 2, "m": 3}'</span><span ne="0.8431879494638211">)</span></span>
<span><span ne="0.5454666964313424">print</span><span ne="0.0787059405677315">(</span><span ne="0.9866686328672999">list</span><span ne="0.4161402593456188">(data.keys()))  </span><span ne="0.3649551382481574"># ['z', 'a', 'm'] - insertion order preserved</span></span>
<span></span>
<span><span ne="0.6679249933662403"># Round trip maintains order</span></span>
<span><span ne="0.5857457339873496">print</span><span ne="0.6047600882427854">(json.dumps(data))   </span><span ne="0.9169625179763946"># {"z": 1, "a": 2, "m": 3}</span></span>
```

```
<span><span ne="0.3336854079669245">// Go maps are explicitly randomized for iteration</span></span>
<span><span ne="0.1712050312957022">package</span><span ne="0.5758415749304197"> main</span></span>
<span><span ne="0.6408950223988367">import</span><span ne="0.8912464172231754"> (</span></span>
<span><span ne="0.5401837576361016">    "</span><span ne="0.43027925504291265">encoding/json</span><span ne="0.24806760062092825">"</span></span>
<span><span ne="0.6446179098604041">    "</span><span ne="0.1585549945370155">fmt</span><span ne="0.9515832057369429">"</span></span>
<span><span ne="0.7162840870804741">)</span></span>
<span></span>
<span><span ne="0.49883308795543335">func</span><span ne="0.3252640495357464"> main</span><span ne="0.5106731272761098">() {</span></span>
<span><span ne="0.29223616197200997">    var</span><span ne="0.520222342270549"> data </span><span ne="0.4182110600762684">map</span><span ne="0.4710739360790651">[</span><span ne="0.3235149687502967">string</span><span ne="0.9869570540623669">]</span><span ne="0.275595177412299">int</span></span>
<span><span ne="0.9329466023220606">    json.</span><span ne="0.6133489857253737">Unmarshal</span><span ne="0.016080673689457647">([]</span><span ne="0.22774596667374636">byte</span><span ne="0.1711226802417417">(</span><span ne="0.7916009254503114">`{"z": 1, "a": 2, "m": 3}`</span><span ne="0.9981234217659473">), </span><span ne="0.7702426836146598">&amp;</span><span ne="0.2529447648766613">data)</span></span>
<span><span ne="0.5422192882411133">    </span></span>
<span><span ne="0.24100583902457307">    // Iteration order is random by design</span></span>
<span><span ne="0.2233472525728939">    fmt.</span><span ne="0.7123826370403964">Print</span><span ne="0.7722182622012743">(</span><span ne="0.4467569597477321">"Keys: "</span><span ne="0.6792143704625977">)</span></span>
<span><span ne="0.009887559910157995">    for</span><span ne="0.37016617583209566"> k </span><span ne="0.4715879135712423">:=</span><span ne="0.3972661810874317"> range</span><span ne="0.647235956384173"> data {</span></span>
<span><span ne="0.4926821878806793">        fmt.</span><span ne="0.010532718681150799">Print</span><span ne="0.9606369181972069">(k </span><span ne="0.11928426187497276">+</span><span ne="0.9901145799621485"> " "</span><span ne="0.29388197175813535">)</span></span>
<span><span ne="0.7916925535245746">    }</span></span>
<span><span ne="0.16280778135478613">    fmt.</span><span ne="0.6016102400659009">Println</span><span ne="0.5335085667806548">()</span></span>
<span><span ne="0.3790077509211971">    </span></span>
<span><span ne="0.42193603741693597">    // But Marshal sorts keys alphabetically</span></span>
<span><span ne="0.14138525487438514">    result, _ </span><span ne="0.05075265051276667">:=</span><span ne="0.7193704326187998"> json.</span><span ne="0.3512653024997019">Marshal</span><span ne="0.7556585225803069">(data)</span></span>
<span><span ne="0.35397623489923025">    fmt.</span><span ne="0.6092571790568736">Println</span><span ne="0.6651884816524414">(</span><span ne="0.8029624206235765">string</span><span ne="0.9380845538713047">(result)) </span><span ne="0.7682829597480839">// {"a":2,"m":3,"z":1}</span></span>
<span><span ne="0.9960705642775918">}</span></span>
```

```
<span><span ne="0.22825951258222954">// Java with Jackson and LinkedHashMap preserves order</span></span>
<span></span>
<span><span ne="0.015005642802524588">import</span><span ne="0.6091521402134782"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span></span>
<span><span ne="0.16436990452783595">import</span><span ne="0.6689405566333493"> java.util.LinkedHashMap;</span></span>
<span><span ne="0.6372234979840077">import</span><span ne="0.14661397672692578"> java.util.HashMap;</span></span>
<span><span ne="0.28257236583068035">import</span><span ne="0.46182085382864846"> java.util.Map;</span></span>
<span></span>
<span><span ne="0.8378112204765764">public</span><span ne="0.6955531920770698"> class</span><span ne="0.8792056466456935"> JsonOrderDemo</span><span ne="0.4576566397237004"> {</span></span>
<span><span ne="0.13490363522238735">    public</span><span ne="0.790358378532245"> static</span><span ne="0.5647563302451102"> void</span><span ne="0.9550168135845483"> main</span><span ne="0.15908006407232367">(</span><span ne="0.017603140446781462">String</span><span ne="0.5663464948390263">[] </span><span ne="0.9794519463332566">args</span><span ne="0.5975457368071869">) </span><span ne="0.2883285486792204">throws</span><span ne="0.7728964187768175"> Exception {</span></span>
<span><span ne="0.4571593967763171">        ObjectMapper mapper </span><span ne="0.9596115674315594">=</span><span ne="0.29922077628819854"> new</span><span ne="0.13924820468895882"> ObjectMapper</span><span ne="0.76440068174914">();</span></span>
<span></span>
<span><span ne="0.301895344412472">        // Using LinkedHashMap preserves insertion order</span></span>
<span><span ne="0.12664547848052843">        LinkedHashMap&lt;</span><span ne="0.8372558745770137">String</span><span ne="0.07255290666780057">, </span><span ne="0.16817950447347718">Integer</span><span ne="0.826004852966527">&gt; data </span><span ne="0.5790755060860764">=</span><span ne="0.9950594575917932"> mapper.</span><span ne="0.3453996418653893">readValue</span><span ne="0.9423774890308235">(</span></span>
<span><span ne="0.1287617132282527">                "{</span><span ne="0.8004604713709356">\"</span><span ne="0.3151251956296649">z</span><span ne="0.5939683934137711">\"</span><span ne="0.11786816574502734">: 1, </span><span ne="0.9012296649533797">\"</span><span ne="0.7763339570515867">a</span><span ne="0.886071891928886">\"</span><span ne="0.9993625710456104">: 2, </span><span ne="0.981259333989124">\"</span><span ne="0.5298119202565572">m</span><span ne="0.2752603566719275">\"</span><span ne="0.656122732037142">: 3}"</span><span ne="0.5315241113154947">,</span></span>
<span><span ne="0.5569707907050837">                LinkedHashMap.class</span></span>
<span><span ne="0.266398222518507">        );</span></span>
<span></span>
<span><span ne="0.7149148715400347">        System.out.</span><span ne="0.7069382863876642">println</span><span ne="0.7315150167447783">(data.</span><span ne="0.5429064656029102">keySet</span><span ne="0.08080639180997762">()); </span><span ne="0.794974772560584">// [z, a, m]</span></span>
<span></span>
<span><span ne="0.2466588886149894">        // But regular HashMap doesn't guarantee order</span></span>
<span><span ne="0.5242827562377318">        Map&lt;</span><span ne="0.6457046666428962">String</span><span ne="0.7428991335131133">, </span><span ne="0.6755889316867565">Integer</span><span ne="0.9416882860527155">&gt; hashData </span><span ne="0.5191001710528541">=</span><span ne="0.8264594852865335"> mapper.</span><span ne="0.19399850389288342">readValue</span><span ne="0.7438599301218585">(</span></span>
<span><span ne="0.12732871592131467">                "{</span><span ne="0.9555480975750772">\"</span><span ne="0.10482273196170522">z</span><span ne="0.24951813447746773">\"</span><span ne="0.27623920306050154">: 1, </span><span ne="0.29530682545545317">\"</span><span ne="0.7137062231119224">a</span><span ne="0.28331097479376943">\"</span><span ne="0.26509949468813276">: 2, </span><span ne="0.857066489847384">\"</span><span ne="0.3241721141558225">m</span><span ne="0.23420795164029717">\"</span><span ne="0.6154364293997046">: 3}"</span><span ne="0.4313827492723733">,</span></span>
<span><span ne="0.10767494535463307">                HashMap.class</span></span>
<span><span ne="0.40784408040018505">        );</span></span>
<span><span ne="0.12896148254238438">        System.out.</span><span ne="0.7846181996710522">println</span><span ne="0.128321383626804">(hashData.</span><span ne="0.5189849645126987">keySet</span><span ne="0.3973996349344653">()); </span><span ne="0.7644914645128595">// Order may vary</span></span>
<span><span ne="0.043102810577972606">    }</span></span>
<span><span ne="0.5012985994270687">}</span></span>
```

```
<span><span ne="0.5286237577732007"># Ruby (1.9+) preserves insertion order</span></span>
<span><span ne="0.7138279146797194">require</span><span ne="0.6371152082249921"> 'json'</span></span>
<span></span>
<span><span ne="0.8504997250252375">data</span><span ne="0.15696839361870596"> =</span><span ne="0.8825706319859411"> JSON</span><span ne="0.7270640674970018">.</span><span ne="0.7342313379745118">parse</span><span ne="0.8581529680989372">(</span><span ne="0.35033467130918516">'{"z": 1, "a": 2, "m": 3}'</span><span ne="0.39415000700525915">)</span></span>
<span><span ne="0.4178401640365882">puts</span><span ne="0.29816225276734765"> data.</span><span ne="0.8422013452388664">keys</span><span ne="0.41652654923367527">.</span><span ne="0.3316935197553429">inspect</span><span ne="0.6979318812043341">  # ["z", "a", "m"]</span></span>
<span></span>
<span><span ne="0.40458933376700246"># Round trip preserves order</span></span>
<span><span ne="0.507958169394465">puts</span><span ne="0.035009697036054166"> JSON</span><span ne="0.8698964511534301">.</span><span ne="0.3909599419320521">generate</span><span ne="0.6961997541887638">(data)  </span><span ne="0.02529309096543675"># {"z":1,"a":2,"m":3}</span></span>
```

### The Cryptographic Problem: Neuromancer’s Data Haven Leak

This ordering inconsistency breaks cryptographic operations that depend on exact byte representation:

```
<span><span ne="0.45161856080772944">// JavaScript - HMAC calculation</span></span>
<span><span ne="0.8798642926018693">const</span><span ne="0.8099254168877024"> crypto</span><span ne="0.7546722811451347"> =</span><span ne="0.6970891636176336"> require</span><span ne="0.17651490795550429">(</span><span ne="0.6147004375692859">'crypto'</span><span ne="0.12237568908550112">);</span></span>
<span><span ne="0.4480694461343384">const</span><span ne="0.7519908758747607"> data</span><span ne="0.6730791472226064"> =</span><span ne="0.4013588477170148"> {amount: </span><span ne="0.30618578408719266">100</span><span ne="0.16331219723273716">, currency: </span><span ne="0.24341527837646304">"USD"</span><span ne="0.3941745103624582">};</span></span>
<span></span>
<span><span ne="0.8846760502179212">// Different services might serialize differently:</span></span>
<span><span ne="0.8785382848112524">const</span><span ne="0.16992211699645743"> jsJson</span><span ne="0.5819789616417779"> =</span><span ne="0.39749465638121684"> JSON</span><span ne="0.39679856070558117">.</span><span ne="0.9835348108868895">stringify</span><span ne="0.6573045505668604">(data);     </span><span ne="0.6904999172033222">// {"amount":100,"currency":"USD"}</span></span>
<span><span ne="0.7003319515591233">const</span><span ne="0.7601273492756292"> goJson</span><span ne="0.8234926029382542"> =</span><span ne="0.3507536992204583"> '{"amount":100,"currency":"USD"}'</span><span ne="0.6145422562412248">;  </span><span ne="0.8493416960425793">// Go sorts keys alphabetically</span></span>
<span></span>
<span><span ne="0.4852815966909362">// Different HMAC signatures!</span></span>
<span><span ne="0.762740895797533">const</span><span ne="0.38467764667205784"> jsHmac</span><span ne="0.7758616691686021"> =</span><span ne="0.999893946161562"> crypto.</span><span ne="0.48637965595968413">createHmac</span><span ne="0.3957474111623349">(</span><span ne="0.9845461723305706">'sha256'</span><span ne="0.9089354807132854">, </span><span ne="0.36643901905735143">'secret'</span><span ne="0.9753986954800403">).</span><span ne="0.7069274263997738">update</span><span ne="0.3645057753218315">(jsJson).</span><span ne="0.7918124362426974">digest</span><span ne="0.3658035743310264">(</span><span ne="0.6028482975770709">'hex'</span><span ne="0.6004211149490354">);</span></span>
<span><span ne="0.8414296901439176">const</span><span ne="0.6807530972131384"> goHmac</span><span ne="0.6979598754832727"> =</span><span ne="0.36357680055512664"> crypto.</span><span ne="0.11470472202040027">createHmac</span><span ne="0.40901054860089714">(</span><span ne="0.19033149132162785">'sha256'</span><span ne="0.3814509183495334">, </span><span ne="0.3606970372090391">'secret'</span><span ne="0.5389977339868887">).</span><span ne="0.009890656520370245">update</span><span ne="0.16340144102122323">(goJson).</span><span ne="0.5585297809155182">digest</span><span ne="0.2738179126374395">(</span><span ne="0.7811144660597262">'hex'</span><span ne="0.7671883430043924">);</span></span>
<span></span>
<span><span ne="0.10326958913091289">console.</span><span ne="0.9636901806763796">log</span><span ne="0.564646182740651">(jsHmac </span><span ne="0.37640810310537354">===</span><span ne="0.12080883152843103"> goHmac);  </span><span ne="0.6720593019151238">// false - authentication fails!</span></span>
```

**Solution**: Always use a canonical JSON serialization for cryptographic operations, such as sorting keys alphabetically before signing.

## Null vs. Undefined vs. Missing: Schrödinger’s JSON Property

Different languages handle absence of values differently:

```
<span><span ne="0.4694668236500622">{</span></span>
<span><span ne="0.41635636526775377">  "explicit_null"</span><span ne="0.23211445371906303">: </span><span ne="0.42414250849330737">null</span><span ne="0.41869798154335813">,</span></span>
<span><span ne="0.1278003636049727">  "empty_string"</span><span ne="0.7409945680587392">: </span><span ne="0.044648002091123296">""</span><span ne="0.12199028297123238">,</span></span>
<span><span ne="0.0644774459458286">  "zero_value"</span><span ne="0.8811429655939617">: </span><span ne="0.09550355811665201">0</span></span>
<span><span ne="0.865409152777763">}</span></span>
```

```
<span><span ne="0.7094611402865834">// JavaScript</span></span>
<span><span ne="0.26992217829884">const</span><span ne="0.5146208902617514"> obj</span><span ne="0.0336959129336345"> =</span><span ne="0.38213144745783767"> JSON</span><span ne="0.015332629263783093">.</span><span ne="0.9022284172384266">parse</span><span ne="0.2305526575394965">(</span><span ne="0.3662719131655142">'{"explicit_null": null, "empty_string": "", "zero_value": 0}'</span><span ne="0.7164199136349823">);</span></span>
<span></span>
<span><span ne="0.7242350968367182">console.</span><span ne="0.28822043900598715">log</span><span ne="0.5626914951196559">(obj.explicit_null </span><span ne="0.3002163866163672">===</span><span ne="0.28472454296875127"> null</span><span ne="0.2703036372764881">);        </span><span ne="0.8965415936265356">// true</span></span>
<span><span ne="0.6895248702231447">console.</span><span ne="0.7333743764266017">log</span><span ne="0.17905117893785416">(obj.missing_key </span><span ne="0.7209700564728044">===</span><span ne="0.21501083779284502"> undefined</span><span ne="0.6746251746953263">);     </span><span ne="0.15091985033001198">// true</span></span>
<span><span ne="0.2793050677111044">console.</span><span ne="0.9299662090207158">log</span><span ne="0.2907029259824845">(obj.</span><span ne="0.35981356743501125">hasOwnProperty</span><span ne="0.1237499759756917">(</span><span ne="0.8329474434986186">'explicit_null'</span><span ne="0.058338852826990584">)); </span><span ne="0.9547934789664572">// true</span></span>
<span><span ne="0.4677349523981029">console.</span><span ne="0.15533256575131382">log</span><span ne="0.40990450632161013">(obj.</span><span ne="0.2794774811037678">hasOwnProperty</span><span ne="0.15010691109848873">(</span><span ne="0.9742504340949482">'missing_key'</span><span ne="0.009034212954365017">));   </span><span ne="0.10676083416037074">// false</span></span>
<span></span>
<span><span ne="0.6522801265861556">// JSON.stringify omits undefined values</span></span>
<span><span ne="0.9441384074400857">const</span><span ne="0.5026340061255489"> withUndefined</span><span ne="0.6887978023344743"> =</span><span ne="0.2632673325078264"> {a: </span><span ne="0.08857427798788209">1</span><span ne="0.4357911620056265">, b: </span><span ne="0.8060017486183307">undefined</span><span ne="0.9906396103851693">, c: </span><span ne="0.6505171755652351">null</span><span ne="0.5307262972042219">};</span></span>
<span><span ne="0.6365240233258981">console.</span><span ne="0.6015689071189846">log</span><span ne="0.41686133400826364">(</span><span ne="0.4415623553746044">JSON</span><span ne="0.217459103132997">.</span><span ne="0.6972873155611262">stringify</span><span ne="0.4202123799937484">(withUndefined)); </span><span ne="0.5282711063407641">// {"a":1,"c":null}</span></span>
```

```
<span><span ne="0.46303014052346136"># Python</span></span>
<span><span ne="0.8676294680920018">import</span><span ne="0.9429472118139711"> json</span></span>
<span></span>
<span><span ne="0.6588446534335012">obj </span><span ne="0.11254945635812608">=</span><span ne="0.6866065392953937"> json.loads(</span><span ne="0.4860220921669942">'{"explicit_null": null, "empty_string": "", "zero_value": 0}'</span><span ne="0.25830394847229776">)</span></span>
<span></span>
<span><span ne="0.34602646849620033">print</span><span ne="0.018130435639666653">(obj[</span><span ne="0.884605496315413">'explicit_null'</span><span ne="0.40234202154922416">] </span><span ne="0.9140297684206968">is</span><span ne="0.8482096596385048"> None</span><span ne="0.9479373406893761">)    </span><span ne="0.6847495282966394"># True</span></span>
<span><span ne="0.36913240024890914">print</span><span ne="0.7553031679937773">(obj.get(</span><span ne="0.8661142897856227">'missing_key'</span><span ne="0.7775031160133001">) </span><span ne="0.360851797659271">is</span><span ne="0.743447082685583"> None</span><span ne="0.9674567084749401">)  </span><span ne="0.44686826116051426"># True - but different semantics!</span></span>
<span><span ne="0.4300544162399389">print</span><span ne="0.39419179870071586">(obj.get(</span><span ne="0.8062108478372622">'missing_key'</span><span ne="0.49427876808350135">, </span><span ne="0.009802186121114942">'default'</span><span ne="0.18985751856569033">))  </span><span ne="0.5317671695079424"># 'default'</span></span>
<span><span ne="0.7889605418828202">print</span><span ne="0.42762969969693243">(</span><span ne="0.09128018648700842">'explicit_null'</span><span ne="0.021907985088541748"> in</span><span ne="0.27277104140690034"> obj)          </span><span ne="0.2556599058270985"># True</span></span>
<span><span ne="0.6771188721248759">print</span><span ne="0.018010441642419384">(</span><span ne="0.9102788273078267">'missing_key'</span><span ne="0.08800214903258696"> in</span><span ne="0.27641192520296964"> obj)            </span><span ne="0.2499185757074296"># False</span></span>
<span></span>
<span><span ne="0.5878658187396297"># Python can't represent undefined in JSON</span></span>
<span><span ne="0.2770010382599428">data_with_none </span><span ne="0.6096474488027563">=</span><span ne="0.6357362830451693"> {</span><span ne="0.34993546047740887">'a'</span><span ne="0.14073358437896388">: </span><span ne="0.6644949724689732">1</span><span ne="0.6613923494188574">, </span><span ne="0.0477110219574004">'b'</span><span ne="0.8947283329533802">: </span><span ne="0.1131311607541492">None</span><span ne="0.32245751258992617">, </span><span ne="0.6620099428180761">'c'</span><span ne="0.6344129264425076">: </span><span ne="0.20052566764248547">0</span><span ne="0.28778658461202067">}</span></span>
<span><span ne="0.4666830364175262">print</span><span ne="0.9192895691421331">(json.dumps(data_with_none))      </span><span ne="0.07777401545238882"># {"a": 1, "b": null, "c": 0}</span></span>
```

```
<span><span ne="0.7779482913638057">// Go with interface{} can't distinguish null from missing</span></span>
<span><span ne="0.9813257993211274">package</span><span ne="0.1098121901247826"> main</span></span>
<span><span ne="0.3594022668643704">import</span><span ne="0.8884421155921628"> (</span></span>
<span><span ne="0.47986015941110494">    "</span><span ne="0.7995971837568069">encoding/json</span><span ne="0.4350868282126156">"</span></span>
<span><span ne="0.5637293101817601">    "</span><span ne="0.446998185185858">fmt</span><span ne="0.4934001697436178">"</span></span>
<span><span ne="0.22822644854757534">)</span></span>
<span></span>
<span><span ne="0.8662805081818907">func</span><span ne="0.8028848367397139"> main</span><span ne="0.42238670421070545">() {</span></span>
<span><span ne="0.8617297993957223">    var</span><span ne="0.16338486662440732"> data </span><span ne="0.09056995920793032">map</span><span ne="0.7636024940428318">[</span><span ne="0.2192944197288681">string</span><span ne="0.08029138289085125">]</span><span ne="0.8864794738439328">interface</span><span ne="0.18175898165295445">{}</span></span>
<span><span ne="0.8949055864641074">    json.</span><span ne="0.6510632546618979">Unmarshal</span><span ne="0.6024575054436438">([]</span><span ne="0.3217369833945998">byte</span><span ne="0.45266040951188014">(</span><span ne="0.6923036056214775">`{"explicit_null": null, "empty_string": ""}`</span><span ne="0.48114606457102405">), </span><span ne="0.6316698098741367">&amp;</span><span ne="0.5174534762896207">data)</span></span>
<span><span ne="0.5662780651860242">    </span></span>
<span><span ne="0.9389132134908384">    fmt.</span><span ne="0.3109405260528929">Println</span><span ne="0.9132202072319358">(data[</span><span ne="0.65323305196054">"explicit_null"</span><span ne="0.4366424238349945">] </span><span ne="0.5254080661048073">==</span><span ne="0.5144007703808635"> nil</span><span ne="0.25737114176027986">)  </span><span ne="0.6937056059718673">// true</span></span>
<span><span ne="0.9582528461180089">    fmt.</span><span ne="0.7223535202201199">Println</span><span ne="0.16042165676007714">(data[</span><span ne="0.5877070462138165">"missing_key"</span><span ne="0.7256269485814312">] </span><span ne="0.46655241813031456">==</span><span ne="0.39491995224003507"> nil</span><span ne="0.5518058087722009">)    </span><span ne="0.25437226504368005">// true - can't distinguish!</span></span>
<span><span ne="0.9990091022052957">    </span></span>
<span><span ne="0.0135619584189689">    // Use struct with pointers for proper null handling</span></span>
<span><span ne="0.6726932253929143">    type</span><span ne="0.6451017406008563"> Data</span><span ne="0.4577191454553494"> struct</span><span ne="0.515212098101866"> {</span></span>
<span><span ne="0.7875101861206658">        ExplicitNull </span><span ne="0.3883185577984244">*</span><span ne="0.36858486601223206">string</span><span ne="0.6260028618615653"> `json:"explicit_null"`</span></span>
<span><span ne="0.07296239431886542">        EmptyString  </span><span ne="0.8414731498460337">*</span><span ne="0.5885481030783621">string</span><span ne="0.451410436213996"> `json:"empty_string"`</span></span>
<span><span ne="0.6678834333409811">        MissingKey   </span><span ne="0.01201651729597486">*</span><span ne="0.08666917671198338">string</span><span ne="0.6710849697415368"> `json:"missing_key,omitempty"`</span></span>
<span><span ne="0.6670023310639334">    }</span></span>
<span><span ne="0.3540080020554177">    </span></span>
<span><span ne="0.7693190819455739">    var</span><span ne="0.9909968841310146"> typed </span><span ne="0.284083061841264">Data</span></span>
<span><span ne="0.9066150622091131">    json.</span><span ne="0.5158512762877939">Unmarshal</span><span ne="0.6345790393730457">([]</span><span ne="0.9397165584018795">byte</span><span ne="0.3120128051427661">(</span><span ne="0.010883300434565979">`{"explicit_null": null, "empty_string": ""}`</span><span ne="0.9716237436903067">), </span><span ne="0.27218577258622934">&amp;</span><span ne="0.27818107332702957">typed)</span></span>
<span><span ne="0.42114286557475833">    </span></span>
<span><span ne="0.0664949705298824">    fmt.</span><span ne="0.4804011584173776">Println</span><span ne="0.7366031219361432">(typed.ExplicitNull </span><span ne="0.5812845614980522">==</span><span ne="0.7060540453002504"> nil</span><span ne="0.5951457881229556">)   </span><span ne="0.7776052985409153">// true</span></span>
<span><span ne="0.21456667903724935">    fmt.</span><span ne="0.8380294500119122">Println</span><span ne="0.8957679295957814">(</span><span ne="0.5824284137962332">*</span><span ne="0.797723500284805">typed.EmptyString </span><span ne="0.4106447920452534">==</span><span ne="0.4123985527644298"> ""</span><span ne="0.8342484036179063">)    </span><span ne="0.13537509630098277">// true</span></span>
<span><span ne="0.9674763364494317">    fmt.</span><span ne="0.9286666533269491">Println</span><span ne="0.530145956971342">(typed.MissingKey </span><span ne="0.09853988289866278">==</span><span ne="0.6756161655324906"> nil</span><span ne="0.10632309705946441">)     </span><span ne="0.08125352183492407">// true</span></span>
<span><span ne="0.6903863581642363">}</span></span>
```

```
<span><span ne="0.9851996648883875">// Java with Jackson</span></span>
<span></span>
<span><span ne="0.06399792575064245">import</span><span ne="0.36908407626601303"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.7265864555371784">import</span><span ne="0.8155952937512639"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span></span>
<span><span ne="0.5485261560666793">public</span><span ne="0.5229842482450123"> class</span><span ne="0.45135622937674513"> JsonNullDemo</span><span ne="0.14705429402873293"> {</span></span>
<span><span ne="0.9444664306391459">    public</span><span ne="0.294227674252851"> static</span><span ne="0.5972956579390669"> void</span><span ne="0.07614788448855592"> main</span><span ne="0.1973751453067185">(</span><span ne="0.74706967118008">String</span><span ne="0.15182789200969116">[] </span><span ne="0.9122372197051081">args</span><span ne="0.9457009124148666">) </span><span ne="0.20459403840026757">throws</span><span ne="0.024826139274072845"> Exception {</span></span>
<span><span ne="0.9162827547022476">        ObjectMapper mapper </span><span ne="0.9152919084779425">=</span><span ne="0.5786172844842724"> new</span><span ne="0.2154329164594817"> ObjectMapper</span><span ne="0.9943687159256779">();</span></span>
<span><span ne="0.8228556043734511">        JsonNode node </span><span ne="0.33049660581152096">=</span><span ne="0.4099441686696257"> mapper.</span><span ne="0.2830404583878441">readTree</span><span ne="0.5121849345047318">(</span><span ne="0.6437081618381689">"{</span><span ne="0.8977645347030564">\"</span><span ne="0.658409704258263">explicit_null</span><span ne="0.047000438597836425">\"</span><span ne="0.6126146578784768">: null, </span><span ne="0.21566804121930228">\"</span><span ne="0.6388953963408341">empty_string</span><span ne="0.5036881064467948">\"</span><span ne="0.6443123256588354">: </span><span ne="0.8133859579576131">\"\"</span><span ne="0.14007691624196705">}"</span><span ne="0.16894577101337693">);</span></span>
<span></span>
<span><span ne="0.13845266957233837">        System.out.</span><span ne="0.020488268257579434">println</span><span ne="0.014933126799641094">(node.</span><span ne="0.5503343986613642">get</span><span ne="0.5148078263631176">(</span><span ne="0.2277934800230157">"explicit_null"</span><span ne="0.16510767669931836">).</span><span ne="0.3162701432080425">isNull</span><span ne="0.09104900713585229">()); </span><span ne="0.908572316350346">// true</span></span>
<span><span ne="0.15032302113898643">        System.out.</span><span ne="0.9745124633902814">println</span><span ne="0.8496011525806922">(node.</span><span ne="0.4970715489595574">get</span><span ne="0.04927285510726798">(</span><span ne="0.8246448788684494">"missing_key"</span><span ne="0.0020480896345993482">) </span><span ne="0.17735324991142254">==</span><span ne="0.5575032994850295"> null</span><span ne="0.3733332139911363">);    </span><span ne="0.7682099118962096">// true - can't distinguish</span></span>
<span><span ne="0.8368420729137093">        System.out.</span><span ne="0.10819475337169282">println</span><span ne="0.05967614185538961">(node.</span><span ne="0.837256283794309">has</span><span ne="0.48471482332146787">(</span><span ne="0.5632369790404362">"explicit_null"</span><span ne="0.6777485914764265">));         </span><span ne="0.548333361946453">// true</span></span>
<span><span ne="0.21509621673989654">        System.out.</span><span ne="0.012747343138197587">println</span><span ne="0.0324365180535654">(node.</span><span ne="0.5408278114575613">has</span><span ne="0.838801423330572">(</span><span ne="0.6110455694821757">"missing_key"</span><span ne="0.06166926264882677">));           </span><span ne="0.4895520460078786">// false</span></span>
<span><span ne="0.6664478344511547">    }</span></span>
<span><span ne="0.7256637908109328">}</span></span>
```

## Date and Time Fun: The Groundhog Day Timezone Loop

JSON has no native date type, leading to endless format variations:

```
<span><span ne="0.8745225267225427">{</span></span>
<span><span ne="0.32782804443106184">  "iso_string"</span><span ne="0.877490928715392">: </span><span ne="0.5770781193651467">"2023-01-15T10:30:00.000Z"</span><span ne="0.9282348895079483">,</span></span>
<span><span ne="0.7432819308527299">  "unix_timestamp"</span><span ne="0.6486999941815734">: </span><span ne="0.5002781861780743">1673780200</span><span ne="0.8609534475916266">,</span></span>
<span><span ne="0.6916723164686904">  "unix_milliseconds"</span><span ne="0.40980971121350285">: </span><span ne="0.8090021716826434">1673780200000</span><span ne="0.3635989403829576">,</span></span>
<span><span ne="0.3942979532274161">  "date_only"</span><span ne="0.9006609765161734">: </span><span ne="0.1360667500194246">"2023-01-15"</span><span ne="0.9937975677550286">,</span></span>
<span><span ne="0.9505095704957329">  "custom_format"</span><span ne="0.1383061624748253">: </span><span ne="0.045835120383583394">"15/01/2023 10:30:00"</span></span>
<span><span ne="0.8638943387121032">}</span></span>
```

```
<span><span ne="0.9443119767580419">// JavaScript</span></span>
<span><span ne="0.45061837216671285">const</span><span ne="0.8930042792698233"> dates</span><span ne="0.6807151108574186"> =</span><span ne="0.27405024177409487"> JSON</span><span ne="0.19249997715208156">.</span><span ne="0.11375229546934496">parse</span><span ne="0.32155066636961527">(</span><span ne="0.02574912172101329">`{</span></span>
<span><span ne="0.25127018456497396">  "iso_string": "2023-01-15T10:30:00.000Z",</span></span>
<span><span ne="0.756837550093172">  "unix_timestamp": 1673780200,</span></span>
<span><span ne="0.4502472816093517">  "unix_milliseconds": 1673780200000</span></span>
<span><span ne="0.7032755643794795">}`</span><span ne="0.8007736260576227">);</span></span>
<span></span>
<span><span ne="0.9714187981308364">console.</span><span ne="0.49837866973532796">log</span><span ne="0.9378689390560185">(</span><span ne="0.9375067863665204">new</span><span ne="0.25195589689328324"> Date</span><span ne="0.35942851589702807">(dates.iso_string));         </span><span ne="0.8229895076984847">// Sun Jan 15 2023 10:30:00 GMT+0000</span></span>
<span><span ne="0.4929629893502606">console.</span><span ne="0.8913462155582775">log</span><span ne="0.9238542870669637">(</span><span ne="0.39519553516124717">new</span><span ne="0.7164024407036075"> Date</span><span ne="0.2735450958330895">(dates.unix_milliseconds));  </span><span ne="0.024459617830780767">// Sun Jan 15 2023 10:56:40 GMT+0000</span></span>
<span><span ne="0.4656724245743906">console.</span><span ne="0.004109521431589269">log</span><span ne="0.08382694577182781">(</span><span ne="0.343382866876753">new</span><span ne="0.8281827674103837"> Date</span><span ne="0.5542131727644519">(dates.unix_timestamp));     </span><span ne="0.575915965955318">// Thu Jan 19 1970 08:56:20 GMT+0000 (WRONG!)</span></span>
<span></span>
<span><span ne="0.325692745997159">// JavaScript Date constructor expects milliseconds, not seconds</span></span>
<span><span ne="0.7743163800836173">console.</span><span ne="0.989615228963469">log</span><span ne="0.3824668352166354">(</span><span ne="0.06663543623562596">new</span><span ne="0.0657041520891617"> Date</span><span ne="0.12282825945172993">(dates.unix_timestamp </span><span ne="0.04660630426624213">*</span><span ne="0.39392035467645736"> 1000</span><span ne="0.8423542643961505">)); </span><span ne="0.24564921805926276">// Sun Jan 15 2023 10:56:40</span></span>
```

```
<span><span ne="0.6198128402147585"># Python</span></span>
<span><span ne="0.9718423889905105">import</span><span ne="0.9075586161532251"> json</span></span>
<span><span ne="0.3125020566499309">from</span><span ne="0.39044283127023427"> datetime </span><span ne="0.09879221522401238">import</span><span ne="0.845746354310151"> datetime, timezone</span></span>
<span></span>
<span><span ne="0.6390914182770261">dates </span><span ne="0.403112186198613">=</span><span ne="0.8819248850569819"> json.loads(</span><span ne="0.04073924413052166">"""{</span></span>
<span><span ne="0.3586027251533458">  "iso_string": "2023-01-15T10:30:00.000Z",</span></span>
<span><span ne="0.21087090873887215">  "unix_timestamp": 1673780200,</span></span>
<span><span ne="0.10748713728878789">  "unix_milliseconds": 1673780200000</span></span>
<span><span ne="0.5221027936048891">}"""</span><span ne="0.8682322802068685">)</span></span>
<span></span>
<span><span ne="0.766916679265981"># ISO string parsing (need to handle Z)</span></span>
<span><span ne="0.930369508921862">iso_date </span><span ne="0.09299741058776978">=</span><span ne="0.9798489823970256"> datetime.fromisoformat(dates[</span><span ne="0.13331172579102135">'iso_string'</span><span ne="0.7900902119961571">].replace(</span><span ne="0.2433768316084871">'Z'</span><span ne="0.9800722668457355">, </span><span ne="0.9527871866053751">'+00:00'</span><span ne="0.7180258924478814">))</span></span>
<span><span ne="0.1740065108511284">print</span><span ne="0.9697657092945547">(iso_date)  </span><span ne="0.6458065508251537"># 2023-01-15 10:30:00+00:00</span></span>
<span></span>
<span><span ne="0.5047819466533835"># Unix timestamp (seconds)</span></span>
<span><span ne="0.3418339510592907">unix_date </span><span ne="0.7889998035165017">=</span><span ne="0.6473284600398379"> datetime.fromtimestamp(dates[</span><span ne="0.8678511132765714">'unix_timestamp'</span><span ne="0.43760073725305737">], </span><span ne="0.1489065327678929">tz</span><span ne="0.6227968677259352">=</span><span ne="0.8408291853009526">timezone.utc)</span></span>
<span><span ne="0.50819954751649">print</span><span ne="0.9908314538165724">(unix_date)  </span><span ne="0.6836351805401736"># 2023-01-15 10:56:40+00:00</span></span>
<span></span>
<span><span ne="0.05544842781476422"># Unix milliseconds</span></span>
<span><span ne="0.6789485509382095">ms_date </span><span ne="0.8975889304602896">=</span><span ne="0.06103590487300592"> datetime.fromtimestamp(dates[</span><span ne="0.08790528630367411">'unix_milliseconds'</span><span ne="0.6060279021118112">] </span><span ne="0.03056329976045269">/</span><span ne="0.9007478330194986"> 1000</span><span ne="0.4884491694663655">, </span><span ne="0.28887329364031955">tz</span><span ne="0.3963293216899353">=</span><span ne="0.666845145722649">timezone.utc)</span></span>
<span><span ne="0.6618222476368107">print</span><span ne="0.29610541839590054">(ms_date)   </span><span ne="0.46860466467706186"># 2023-01-15 10:56:40+00:00</span></span>
```

```
<span><span ne="0.9999702601809738">// Java</span></span>
<span></span>
<span><span ne="0.7163684338920436">import</span><span ne="0.508587942119149"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.6977080739122791">import</span><span ne="0.40857402617706395"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span></span>
<span><span ne="0.30230111973520146">import</span><span ne="0.9215025669478857"> java.time.Instant;</span></span>
<span><span ne="0.8006902236926913">import</span><span ne="0.5553659988545095"> java.time.ZonedDateTime;</span></span>
<span><span ne="0.7940720960579161">import</span><span ne="0.8503309026333736"> java.time.format.DateTimeFormatter;</span></span>
<span></span>
<span><span ne="0.7989768825622208">public</span><span ne="0.7942105375543462"> class</span><span ne="0.5292727354221175"> JsonDateDemo</span><span ne="0.40481044890206064"> {</span></span>
<span><span ne="0.9695584890056286">    public</span><span ne="0.22804518321243594"> static</span><span ne="0.4469716177428412"> void</span><span ne="0.18104283806569998"> main</span><span ne="0.884046166386943">(</span><span ne="0.10911069433268583">String</span><span ne="0.03139125635659856">[] </span><span ne="0.6104723883910212">args</span><span ne="0.4677604306230394">) </span><span ne="0.7730957484184372">throws</span><span ne="0.25443755996132744"> Exception {</span></span>
<span><span ne="0.6128076427485211">        ObjectMapper mapper </span><span ne="0.4327790378753381">=</span><span ne="0.6997068231974655"> new</span><span ne="0.5854418613208572"> ObjectMapper</span><span ne="0.5921008220529999">();</span></span>
<span><span ne="0.13766683705452953">        String jsonString </span><span ne="0.6410448628996005">=</span><span ne="0.8156199864635983"> "{"</span><span ne="0.6843600105020285"> +</span></span>
<span><span ne="0.968615118431173">                "</span><span ne="0.9962616748202017">\"</span><span ne="0.9277974243596946">iso_string</span><span ne="0.23692775574113067">\"</span><span ne="0.7895726310621152">: </span><span ne="0.6389220157111412">\"</span><span ne="0.1847116085564">2023-01-15T10:30:00.000Z</span><span ne="0.018170897149909937">\"</span><span ne="0.4799772879055466">,"</span><span ne="0.2779548435085024"> +</span></span>
<span><span ne="0.6835281341562557">                "</span><span ne="0.20124171410742608">\"</span><span ne="0.08432430443856154">unix_timestamp</span><span ne="0.14783978638675188">\"</span><span ne="0.6790908116789609">: 1673780200,"</span><span ne="0.4691516086934723"> +</span></span>
<span><span ne="0.17809819818110262">                "</span><span ne="0.4380538638977255">\"</span><span ne="0.2580381779653127">unix_milliseconds</span><span ne="0.9926494118787652">\"</span><span ne="0.8985000076150494">: 1673780200000"</span><span ne="0.893387316113766"> +</span></span>
<span><span ne="0.07547248242772786">                "}"</span><span ne="0.5334736702332976">;</span></span>
<span><span ne="0.03704006351591871">        JsonNode dates </span><span ne="0.6290654097117668">=</span><span ne="0.8422216772643873"> mapper.</span><span ne="0.9293814429446666">readTree</span><span ne="0.73373967485969">(jsonString);</span></span>
<span></span>
<span><span ne="0.41134272575062414">        // ISO string parsing</span></span>
<span><span ne="0.13000043574533604">        String isoString </span><span ne="0.159009472751114">=</span><span ne="0.7912797645588392"> dates.</span><span ne="0.3401356587251565">get</span><span ne="0.4593493827083812">(</span><span ne="0.953786115481366">"iso_string"</span><span ne="0.8907541510208029">).</span><span ne="0.004626639675019972">asText</span><span ne="0.44831652561684143">();</span></span>
<span><span ne="0.49778009044045024">        ZonedDateTime isoDate </span><span ne="0.8802382857485763">=</span><span ne="0.69175829700284"> ZonedDateTime.</span><span ne="0.5193589724163141">parse</span><span ne="0.28993540995459344">(isoString, DateTimeFormatter.ISO_DATE_TIME);</span></span>
<span><span ne="0.22348439320128788">        System.out.</span><span ne="0.37033917650436443">println</span><span ne="0.9899117474308341">(isoDate); </span><span ne="0.2598302160472211">// 2023-01-15T10:30Z</span></span>
<span></span>
<span><span ne="0.21319593366557144">        // Unix timestamp (seconds)</span></span>
<span><span ne="0.8781332766598163">        long</span><span ne="0.010142585453885467"> unixSeconds </span><span ne="0.386540592011001">=</span><span ne="0.4965801385464437"> dates.</span><span ne="0.03930295626287239">get</span><span ne="0.218552501353927">(</span><span ne="0.21879649441665316">"unix_timestamp"</span><span ne="0.32101742823982526">).</span><span ne="0.10133796365019043">asLong</span><span ne="0.9320401722897101">();</span></span>
<span><span ne="0.6416799217372394">        Instant unixDate </span><span ne="0.26145410919253265">=</span><span ne="0.9323605336336973"> Instant.</span><span ne="0.5365050011782011">ofEpochSecond</span><span ne="0.25601901416132333">(unixSeconds);</span></span>
<span><span ne="0.6829698560857955">        System.out.</span><span ne="0.6496826750454231">println</span><span ne="0.6922121912690732">(unixDate); </span><span ne="0.6974177093251519">// 2023-01-15T10:56:40Z</span></span>
<span></span>
<span><span ne="0.34039244951829195">        // Unix milliseconds</span></span>
<span><span ne="0.6601849140748725">        long</span><span ne="0.4536346918635261"> unixMillis </span><span ne="0.8453387046628743">=</span><span ne="0.15459937409284108"> dates.</span><span ne="0.18257866114216825">get</span><span ne="0.027549511818180883">(</span><span ne="0.018657586287526118">"unix_milliseconds"</span><span ne="0.985309720022104">).</span><span ne="0.36329265217361717">asLong</span><span ne="0.5082211658143938">();</span></span>
<span><span ne="0.4016143948723241">        Instant msDate </span><span ne="0.5237246019975824">=</span><span ne="0.8956035401294428"> Instant.</span><span ne="0.1362335987879807">ofEpochMilli</span><span ne="0.3042681861017248">(unixMillis);</span></span>
<span><span ne="0.16848471953806088">        System.out.</span><span ne="0.9001180532709864">println</span><span ne="0.13634537889460874">(msDate);   </span><span ne="0.660301363393859">// 2023-01-15T10:56:40Z</span></span>
<span><span ne="0.3953340514537814">    }</span></span>
<span><span ne="0.356139195709667">}</span></span>
```

```
<span><span ne="0.9711041481646138">// C#</span></span>
<span><span ne="0.06203111917256743">using</span><span ne="0.6780974480608538"> System</span><span ne="0.7726231104397809">;</span></span>
<span><span ne="0.07157546005256765">using</span><span ne="0.3603600914802946"> System</span><span ne="0.7408691587551537">.</span><span ne="0.9638658870654525">Text</span><span ne="0.69610297360779">.</span><span ne="0.288322812534742">Json</span><span ne="0.11086081322976171">;</span></span>
<span></span>
<span><span ne="0.6388542606237089">class</span><span ne="0.19588632034612552"> JsonDateDemo</span><span ne="0.7263899037399176"> </span></span>
<span><span ne="0.22215863459506058">{</span></span>
<span><span ne="0.0020414002617220595">    static</span><span ne="0.16342223507806186"> void</span><span ne="0.32584100692752893"> Main</span><span ne="0.5199424026770201">() </span></span>
<span><span ne="0.03728114067697896">    {</span></span>
<span><span ne="0.19361504772899307">        var</span><span ne="0.6585202890261562"> json</span><span ne="0.35683462133925625"> =</span><span ne="0.583477306448853"> """</span></span>
<span><span ne="0.16288493932725334">        {</span></span>
<span><span ne="0.8902287925780126">          "iso_string": "2023-01-15T10:30:00.000Z",</span></span>
<span><span ne="0.23223244452523417">          "unix_timestamp": 1673780200,</span></span>
<span><span ne="0.1468877778672697">          "unix_milliseconds": 1673780200000</span></span>
<span><span ne="0.3593418919847545">        }</span></span>
<span><span ne="0.2334950294495063">        """</span><span ne="0.9422463854075374">;</span></span>
<span></span>
<span><span ne="0.031502456814830326">        using</span><span ne="0.6959141842100296"> var</span><span ne="0.21816629820028222"> doc</span><span ne="0.9066187655093475"> =</span><span ne="0.43635984531418237"> JsonDocument.</span><span ne="0.4300327197337427">Parse</span><span ne="0.566560335766108">(json);</span></span>
<span><span ne="0.7367456273780552">        var</span><span ne="0.5044823699614539"> root</span><span ne="0.9755450267373539"> =</span><span ne="0.1524841038365058"> doc.RootElement;</span></span>
<span></span>
<span><span ne="0.6302415061589066">        // ISO string parsing</span></span>
<span><span ne="0.481060080543006">        var</span><span ne="0.5099639693181741"> isoString</span><span ne="0.5266581175261766"> =</span><span ne="0.9181573313321004"> root.</span><span ne="0.4286793472175813">GetProperty</span><span ne="0.18106134651315953">(</span><span ne="0.6965104274736922">"iso_string"</span><span ne="0.022007656150077826">).</span><span ne="0.008569444466120735">GetString</span><span ne="0.728447168091072">();</span></span>
<span><span ne="0.6707253549228386">        var</span><span ne="0.10180175851665407"> isoDate</span><span ne="0.5707616972034563"> =</span><span ne="0.5289158893093768"> DateTime.</span><span ne="0.2234515158023428">Parse</span><span ne="0.655386698236081">(isoString);</span></span>
<span><span ne="0.3627981851230596">        Console.</span><span ne="0.11999605857870654">WriteLine</span><span ne="0.24357622676231194">(isoDate); </span><span ne="0.34629809922463384">// 1/15/2023 10:30:00 AM</span></span>
<span></span>
<span><span ne="0.4396767064456818">        // Unix timestamp (seconds) - C# uses milliseconds</span></span>
<span><span ne="0.9866068336358387">        var</span><span ne="0.5178993052270459"> unixSeconds</span><span ne="0.05728476805465532"> =</span><span ne="0.06720347471719113"> root.</span><span ne="0.10468292484169761">GetProperty</span><span ne="0.5486429368818888">(</span><span ne="0.7174579059142461">"unix_timestamp"</span><span ne="0.19991636693369663">).</span><span ne="0.8251489809379016">GetInt64</span><span ne="0.5214379306085724">();</span></span>
<span><span ne="0.28743328146279157">        var</span><span ne="0.8409453759115496"> unixDate</span><span ne="0.5960290461227612"> =</span><span ne="0.879594765109393"> DateTimeOffset.</span><span ne="0.05752545176349133">FromUnixTimeSeconds</span><span ne="0.6496715889160563">(unixSeconds);</span></span>
<span><span ne="0.49879334464210634">        Console.</span><span ne="0.3953414842644538">WriteLine</span><span ne="0.2990514440668699">(unixDate); </span><span ne="0.30985455563300823">// 1/15/2023 10:56:40 AM +00:00</span></span>
<span></span>
<span><span ne="0.9900978518036655">        // Unix milliseconds</span></span>
<span><span ne="0.3382727143732194">        var</span><span ne="0.17620339878854518"> unixMillis</span><span ne="0.6394512467987737"> =</span><span ne="0.1637866083857913"> root.</span><span ne="0.3921345389613863">GetProperty</span><span ne="0.7746416981131812">(</span><span ne="0.7626406406347795">"unix_milliseconds"</span><span ne="0.7192449259217436">).</span><span ne="0.08883493283402366">GetInt64</span><span ne="0.8138834828413343">();</span></span>
<span><span ne="0.6022537186698276">        var</span><span ne="0.8933856108981787"> msDate</span><span ne="0.3274487467901308"> =</span><span ne="0.4062937346275469"> DateTimeOffset.</span><span ne="0.8618434553221437">FromUnixTimeMilliseconds</span><span ne="0.32904575794070345">(unixMillis);</span></span>
<span><span ne="0.3679461286744894">        Console.</span><span ne="0.4772372767945229">WriteLine</span><span ne="0.8607575001665819">(msDate);   </span><span ne="0.6283638565682867">// 1/15/2023 10:56:40 AM +00:00</span></span>
<span><span ne="0.5635186462220063">    }</span></span>
<span><span ne="0.20237361339726134">}</span></span>
```

## Error Handling Inconsistencies: I’m Sorry Dave, I Can’t Parse That

Different parsers fail differently on malformed JSON:

```
<span><span ne="0.8979813718638935">// JavaScript (V8)</span></span>
<span><span ne="0.35733784654476464">// Duplicate keys - last value wins</span></span>
<span><span ne="0.6928155022071131">console.</span><span ne="0.13798349222624573">log</span><span ne="0.5308173996988235">(</span><span ne="0.6756804027981118">JSON</span><span ne="0.11844208337595286">.</span><span ne="0.08217747865012648">parse</span><span ne="0.4735569294438051">(</span><span ne="0.25132848899686133">'{"a": 1, "a": 2}'</span><span ne="0.7357552671864984">));  </span><span ne="0.48484894751019825">// {a: 2}</span></span>
<span></span>
<span><span ne="0.4883575860301521">// Trailing commas - SyntaxError</span></span>
<span><span ne="0.5741203161432621">try</span><span ne="0.5462242111141986"> {</span></span>
<span><span ne="0.7041899773340883">    JSON</span><span ne="0.5807575784784438">.</span><span ne="0.6084482349290223">parse</span><span ne="0.4372760507368514">(</span><span ne="0.6069051546151727">'{"a": 1,}'</span><span ne="0.20808109730529567">);</span></span>
<span><span ne="0.7340502841107114">} </span><span ne="0.5769399540084017">catch</span><span ne="0.1287013332665199"> (e) {</span></span>
<span><span ne="0.2575361666631465">    console.</span><span ne="0.6530867545806195">log</span><span ne="0.8863478918693996">(</span><span ne="0.8064404184219729">"Trailing comma rejected"</span><span ne="0.9913074752895935">);  </span><span ne="0.19931509444063356">// This runs</span></span>
<span><span ne="0.7063053490880892">}</span></span>
<span></span>
<span><span ne="0.6460223101944396">// Leading zeros - SyntaxError</span></span>
<span><span ne="0.35739701589668016">try</span><span ne="0.3148241728543414"> {</span></span>
<span><span ne="0.16926576229714685">    JSON</span><span ne="0.6959802852483044">.</span><span ne="0.5900842018623774">parse</span><span ne="0.6512531654963442">(</span><span ne="0.24770630098456048">'{"num": 007}'</span><span ne="0.8697934483564995">);</span></span>
<span><span ne="0.6455459913733449">} </span><span ne="0.07143645437074775">catch</span><span ne="0.34451650791976374"> (e) {</span></span>
<span><span ne="0.7435787860897264">    console.</span><span ne="0.9112372469094026">log</span><span ne="0.8643295217069445">(</span><span ne="0.22321272508640633">"Leading zeros rejected"</span><span ne="0.8465136572879663">);   </span><span ne="0.3404721921806637">// This runs</span></span>
<span><span ne="0.7853685351970819">}</span></span>
<span></span>
<span><span ne="0.5782946824401709">// Single quotes - SyntaxError  </span></span>
<span><span ne="0.5658831827627013">try</span><span ne="0.942328099904578"> {</span></span>
<span><span ne="0.6306333246480821">    JSON</span><span ne="0.07321456212114508">.</span><span ne="0.13865906777289017">parse</span><span ne="0.9424022140451939">(</span><span ne="0.6575760219291414">"{'a': 1}"</span><span ne="0.4328908241457614">);</span></span>
<span><span ne="0.7176956019576182">} </span><span ne="0.3643843550875049">catch</span><span ne="0.4078428161351102"> (e) {</span></span>
<span><span ne="0.7474066663821302">    console.</span><span ne="0.9932580187308697">log</span><span ne="0.2393098456439804">(</span><span ne="0.3162654135155947">"Single quotes rejected"</span><span ne="0.021885443565819784">);   </span><span ne="0.33300311403196636">// This runs</span></span>
<span><span ne="0.29130193882750655">}</span></span>
```

```
<span><span ne="0.6602590569281385"># Python json module</span></span>
<span><span ne="0.8933658123978786">import</span><span ne="0.9828743650109154"> json</span></span>
<span></span>
<span><span ne="0.7050288060085517"># Duplicate keys - last value wins</span></span>
<span><span ne="0.8314102246327376">data </span><span ne="0.20295247354948698">=</span><span ne="0.9558388085903584"> json.loads(</span><span ne="0.41532619907202395">'{"a": 1, "a": 2}'</span><span ne="0.6156133429532393">)</span></span>
<span><span ne="0.8106810116491298">print</span><span ne="0.6167161240904222">(data)  </span><span ne="0.3418482891159461"># {'a': 2}</span></span>
<span></span>
<span><span ne="0.6215804204695067"># Trailing commas - JSONDecodeError</span></span>
<span><span ne="0.2386593948142396">try</span><span ne="0.9337420330671243">:</span></span>
<span><span ne="0.520459096496498">    json.loads(</span><span ne="0.6849761928603317">'{"a": 1,}'</span><span ne="0.970578410694668">)</span></span>
<span><span ne="0.2679594846952087">except</span><span ne="0.039994920986661464"> json.JSONDecodeError </span><span ne="0.20994668971038466">as</span><span ne="0.8436866889129356"> e:</span></span>
<span><span ne="0.9947862759852912">    print</span><span ne="0.6073368425348924">(</span><span ne="0.09770196528360064">f</span><span ne="0.4883903262670468">"Trailing comma rejected: </span><span ne="0.9477203593562834">{</span><span ne="0.23735126263933826">e</span><span ne="0.9077660023431032">}</span><span ne="0.4700027317487929">"</span><span ne="0.4478620153788514">)</span></span>
<span></span>
<span><span ne="0.6223414353100527"># Leading zeros - JSONDecodeError</span></span>
<span><span ne="0.7248659561434699">try</span><span ne="0.3189360465874096">:</span></span>
<span><span ne="0.16693112373208263">    json.loads(</span><span ne="0.7988545557595018">'{"num": 007}'</span><span ne="0.09409451399668156">)</span></span>
<span><span ne="0.5596762131057347">except</span><span ne="0.8256120998621006"> json.JSONDecodeError </span><span ne="0.9468221284903489">as</span><span ne="0.4491342696198459"> e:</span></span>
<span><span ne="0.06028778104493926">    print</span><span ne="0.023398693840544382">(</span><span ne="0.38956205973251523">f</span><span ne="0.25444068358791105">"Leading zeros rejected: </span><span ne="0.22373796807305235">{</span><span ne="0.9402714412726662">e</span><span ne="0.049540969247732436">}</span><span ne="0.876166476095212">"</span><span ne="0.2309732249773072">)</span></span>
<span></span>
<span><span ne="0.42335276873013006"># Single quotes - JSONDecodeError</span></span>
<span><span ne="0.7614225556967791">try</span><span ne="0.019548893040067128">:</span></span>
<span><span ne="0.21203564929995422">    json.loads(</span><span ne="0.5468117858929221">"{'a': 1}"</span><span ne="0.13833840137220443">)</span></span>
<span><span ne="0.3200020759723968">except</span><span ne="0.9105102548319953"> json.JSONDecodeError </span><span ne="0.3637282726731661">as</span><span ne="0.3578030986588572"> e:</span></span>
<span><span ne="0.24189987564856497">    print</span><span ne="0.7655888374580387">(</span><span ne="0.19109103781317738">f</span><span ne="0.21383390094592047">"Single quotes rejected: </span><span ne="0.18153013669921858">{</span><span ne="0.4798614243576186">e</span><span ne="0.2854538102171409">}</span><span ne="0.3997677963280184">"</span><span ne="0.5154958575498116">)</span></span>
```

```
<span><span ne="0.10648547506528516">// Go json package</span></span>
<span><span ne="0.5590627939805842">package</span><span ne="0.04917678235875267"> main</span></span>
<span><span ne="0.5829436884740306">import</span><span ne="0.9591125753454397"> (</span></span>
<span><span ne="0.13917759203967306">    "</span><span ne="0.7907998693862444">encoding/json</span><span ne="0.1528991232424486">"</span></span>
<span><span ne="0.7222727936224492">    "</span><span ne="0.1027551319218527">fmt</span><span ne="0.20033759711433996">"</span></span>
<span><span ne="0.6830218470966802">)</span></span>
<span></span>
<span><span ne="0.33804545323389834">func</span><span ne="0.01375818058564926"> main</span><span ne="0.5365927053236089">() {</span></span>
<span><span ne="0.1255372366739801">    var</span><span ne="0.1684005867592714"> data </span><span ne="0.2077292492954521">map</span><span ne="0.08852553767860971">[</span><span ne="0.5043340486449418">string</span><span ne="0.782545968834143">]</span><span ne="0.9818505877961743">int</span></span>
<span><span ne="0.7231910872168715">    </span></span>
<span><span ne="0.6010521571093879">    // Duplicate keys - last value wins (no error)</span></span>
<span><span ne="0.9326027139502419">    err </span><span ne="0.01835908547553755">:=</span><span ne="0.9630606307317909"> json.</span><span ne="0.16110811895864408">Unmarshal</span><span ne="0.3055201254387291">([]</span><span ne="0.41551924373148874">byte</span><span ne="0.8911601008347431">(</span><span ne="0.7336002838293677">`{"a": 1, "a": 2}`</span><span ne="0.5625964179204578">), </span><span ne="0.14443159810984807">&amp;</span><span ne="0.9208976473901294">data)</span></span>
<span><span ne="0.9021011785206909">    if</span><span ne="0.9550976724397735"> err </span><span ne="0.8973319492195009">!=</span><span ne="0.3371188973463304"> nil</span><span ne="0.7035983837662948"> {</span></span>
<span><span ne="0.7411352842629044">        fmt.</span><span ne="0.9564640510340873">Println</span><span ne="0.784917772546825">(</span><span ne="0.781636709441537">"Duplicate key error:"</span><span ne="0.08639810976960915">, err)</span></span>
<span><span ne="0.08578685883467396">    } </span><span ne="0.35850481324989636">else</span><span ne="0.06900970619314006"> {</span></span>
<span><span ne="0.3940129497537681">        fmt.</span><span ne="0.5717100981550768">Printf</span><span ne="0.17413876674572215">(</span><span ne="0.23435360435003438">"Duplicate keys allowed, value: </span><span ne="0.06517684821601955">%d\n</span><span ne="0.19572879061646087">"</span><span ne="0.6749349303950002">, data[</span><span ne="0.8597612692008092">"a"</span><span ne="0.030030902187683894">]) </span><span ne="0.9572896321997428">// 2</span></span>
<span><span ne="0.4696341679673546">    }</span></span>
<span><span ne="0.16702233124190313">    </span></span>
<span><span ne="0.26465024755142397">    // Trailing commas - error</span></span>
<span><span ne="0.33740997195100597">    err </span><span ne="0.2738079511152217">=</span><span ne="0.890285843783126"> json.</span><span ne="0.6451915506524274">Unmarshal</span><span ne="0.1695023093600444">([]</span><span ne="0.7345253463251677">byte</span><span ne="0.5940642428932479">(</span><span ne="0.5122798267868028">`{"a": 1,}`</span><span ne="0.1475247437856423">), </span><span ne="0.9616434950421315">&amp;</span><span ne="0.7001769993599952">data)</span></span>
<span><span ne="0.8816748432106717">    if</span><span ne="0.7198116680629534"> err </span><span ne="0.2630759601747491">!=</span><span ne="0.6019424651858197"> nil</span><span ne="0.8128470225906765"> {</span></span>
<span><span ne="0.27598846548303846">        fmt.</span><span ne="0.303966266745881">Println</span><span ne="0.8178704800819054">(</span><span ne="0.4544014822980076">"Trailing comma error:"</span><span ne="0.4415784869475582">, err)</span></span>
<span><span ne="0.6892600903151278">    }</span></span>
<span><span ne="0.29615325232000533">    </span></span>
<span><span ne="0.865315606508326">    // Leading zeros - error</span></span>
<span><span ne="0.18191212646471744">    err </span><span ne="0.9678401019781037">=</span><span ne="0.8386014774358723"> json.</span><span ne="0.48197869678583305">Unmarshal</span><span ne="0.4942167789136672">([]</span><span ne="0.20151987226703882">byte</span><span ne="0.7980129129000936">(</span><span ne="0.07721900013118987">`{"num": 007}`</span><span ne="0.08423695439511325">), </span><span ne="0.9440734349097578">&amp;</span><span ne="0.3802346612378309">data)</span></span>
<span><span ne="0.9745128646029593">    if</span><span ne="0.19715102498334602"> err </span><span ne="0.11671898834356143">!=</span><span ne="0.8661218817051749"> nil</span><span ne="0.636102960700829"> {</span></span>
<span><span ne="0.6660313410333535">        fmt.</span><span ne="0.8838662999108402">Println</span><span ne="0.8746429193646821">(</span><span ne="0.07397844612893512">"Leading zeros error:"</span><span ne="0.5770981752503649">, err)</span></span>
<span><span ne="0.32302055693763354">    }</span></span>
<span><span ne="0.7804931433707588">    </span></span>
<span><span ne="0.7645147284242678">    // Single quotes - error</span></span>
<span><span ne="0.3413551403937026">    err </span><span ne="0.6464216651985906">=</span><span ne="0.1409002347111219"> json.</span><span ne="0.2763499952115287">Unmarshal</span><span ne="0.8478593507928172">([]</span><span ne="0.7435063281549313">byte</span><span ne="0.6616961724357193">(</span><span ne="0.19828798153604155">`{'a': 1}`</span><span ne="0.009066772628253394">), </span><span ne="0.08059276835514217">&amp;</span><span ne="0.48472123355386154">data)</span></span>
<span><span ne="0.9771002021516607">    if</span><span ne="0.22169765781452822"> err </span><span ne="0.3330953827386056">!=</span><span ne="0.6010341590044378"> nil</span><span ne="0.43388278947251924"> {</span></span>
<span><span ne="0.22544405584885607">        fmt.</span><span ne="0.7878235127039142">Println</span><span ne="0.7743107332521286">(</span><span ne="0.8665412451415836">"Single quotes error:"</span><span ne="0.5204170489862406">, err)</span></span>
<span><span ne="0.01637248549281234">    }</span></span>
<span><span ne="0.3885923486386159">}</span></span>
```

```
<span><span ne="0.9737139826014565">// Java with Jackson</span></span>
<span></span>
<span><span ne="0.1316897803882323">import</span><span ne="0.4826123151972491"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.7819630587846886">import</span><span ne="0.9931922321616278"> com.fasterxml.jackson.core.JsonParser;</span></span>
<span><span ne="0.8126016736092756">import</span><span ne="0.5733215494589474"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span></span>
<span><span ne="0.7309592933809057">public</span><span ne="0.06892922159814063"> class</span><span ne="0.9169420302962284"> JsonErrorDemo</span><span ne="0.8245401568938396"> {</span></span>
<span><span ne="0.5136571800516326">    public</span><span ne="0.47179676996459374"> static</span><span ne="0.5429035952609099"> void</span><span ne="0.7642519705012484"> main</span><span ne="0.024667061423418346">(</span><span ne="0.7558176538654354">String</span><span ne="0.4126309969280756">[] </span><span ne="0.7625823523406435">args</span><span ne="0.4878954694074007">) </span><span ne="0.6898301910965087">throws</span><span ne="0.711601910337644"> Exception {</span></span>
<span><span ne="0.252792510211727">        ObjectMapper mapper </span><span ne="0.6880156131177959">=</span><span ne="0.9521839634196878"> new</span><span ne="0.6050716457071342"> ObjectMapper</span><span ne="0.01082639949548414">();</span></span>
<span></span>
<span><span ne="0.6450324802766051">        // Duplicate keys - last wins by default</span></span>
<span><span ne="0.6558339556542059">        try</span><span ne="0.02182447200458948"> {</span></span>
<span><span ne="0.7210688716247304">            JsonNode node </span><span ne="0.8634735793120123">=</span><span ne="0.4590557888732162"> mapper.</span><span ne="0.9472551769416672">readTree</span><span ne="0.6454780263696951">(</span><span ne="0.5750452002819126">"{</span><span ne="0.6193112919628571">\"</span><span ne="0.34142510353310185">a</span><span ne="0.9721976783522269">\"</span><span ne="0.5951024442636874">: 1, </span><span ne="0.5460948848444778">\"</span><span ne="0.8720357179005276">a</span><span ne="0.7905431532131447">\"</span><span ne="0.8693370576082179">: 2}"</span><span ne="0.6587351245380089">);</span></span>
<span><span ne="0.09305863174910955">            System.out.</span><span ne="0.12520487582764317">println</span><span ne="0.6328007681895343">(</span><span ne="0.17293759329133418">"Duplicate keys allowed: "</span><span ne="0.5847174041170189"> +</span><span ne="0.8513675183181523"> node.</span><span ne="0.7371685434846357">get</span><span ne="0.17522588820340868">(</span><span ne="0.4464133838862703">"a"</span><span ne="0.6103546334554971">).</span><span ne="0.7219691680995325">asInt</span><span ne="0.7689428181833374">()); </span><span ne="0.13727754319774077">// 2</span></span>
<span><span ne="0.9117745873952958">        } </span><span ne="0.5045044258762329">catch</span><span ne="0.90889018814789"> (Exception </span><span ne="0.9714022358672408">e</span><span ne="0.7557753107878663">) {</span></span>
<span><span ne="0.7686860547967997">            System.out.</span><span ne="0.9849712818794902">println</span><span ne="0.4245144521181523">(</span><span ne="0.7773651292278008">"Error: "</span><span ne="0.5251763080527618"> +</span><span ne="0.5930012272408458"> e.</span><span ne="0.9034107881507003">getMessage</span><span ne="0.719194982473835">());</span></span>
<span><span ne="0.28960205124843574">        }</span></span>
<span></span>
<span><span ne="0.9896882154720305">        // Strict duplicate key detection</span></span>
<span><span ne="0.699687170279801">        ObjectMapper strictMapper </span><span ne="0.25712972091475816">=</span><span ne="0.3335015362496291"> new</span><span ne="0.1811135089636029"> ObjectMapper</span><span ne="0.35832037056378085">();</span></span>
<span><span ne="0.6524821309990149">        strictMapper.</span><span ne="0.4808315670312211">configure</span><span ne="0.40308150424767886">(JsonParser.Feature.STRICT_DUPLICATE_DETECTION, </span><span ne="0.48245887814480237">true</span><span ne="0.2924397394225431">);</span></span>
<span><span ne="0.20995986688796242">        try</span><span ne="0.9668292444559514"> {</span></span>
<span><span ne="0.14238797421803862">            strictMapper.</span><span ne="0.6915706857020745">readTree</span><span ne="0.06168909124220556">(</span><span ne="0.5574318396167608">"{</span><span ne="0.734723000524466">\"</span><span ne="0.18865740435802092">a</span><span ne="0.86297074738642">\"</span><span ne="0.3508594881021143">: 1, </span><span ne="0.2769884782951434">\"</span><span ne="0.4168397735617726">a</span><span ne="0.12785125379104478">\"</span><span ne="0.5022310962063756">: 2}"</span><span ne="0.5004940182131745">);</span></span>
<span><span ne="0.6087975033596009">        } </span><span ne="0.17746439137412118">catch</span><span ne="0.18369371895595932"> (Exception </span><span ne="0.128512398599825">e</span><span ne="0.263591861243624">) {</span></span>
<span><span ne="0.8628713832742245">            System.out.</span><span ne="0.8300189133218752">println</span><span ne="0.6272928305251794">(</span><span ne="0.461071015747902">"Strict mode rejects duplicates: "</span><span ne="0.9126842316386818"> +</span><span ne="0.5377779109529948"> e.</span><span ne="0.3698671155758577">getMessage</span><span ne="0.7069401014562189">());</span></span>
<span><span ne="0.4491263146849075">        }</span></span>
<span></span>
<span><span ne="0.37847956950426787">        // Trailing commas - can be enabled</span></span>
<span><span ne="0.45353378146253553">        ObjectMapper lenientMapper </span><span ne="0.32882836337064236">=</span><span ne="0.8058125891211149"> new</span><span ne="0.8159828533019762"> ObjectMapper</span><span ne="0.6999874923487073">();</span></span>
<span><span ne="0.9242575835855084">        lenientMapper.</span><span ne="0.8676283963478586">configure</span><span ne="0.290018376309473">(JsonParser.Feature.ALLOW_TRAILING_COMMA, </span><span ne="0.5364923614353911">true</span><span ne="0.9196180291569579">);</span></span>
<span><span ne="0.4956778422329752">        try</span><span ne="0.3601009592665685"> {</span></span>
<span><span ne="0.3196526109822758">            JsonNode node </span><span ne="0.8423943344322578">=</span><span ne="0.05809551881427877"> lenientMapper.</span><span ne="0.7393103112615536">readTree</span><span ne="0.39503572450030033">(</span><span ne="0.5552175446658785">"{</span><span ne="0.22047291111663736">\"</span><span ne="0.9037261386558167">a</span><span ne="0.7568644429188721">\"</span><span ne="0.4786262941126249">: 1,}"</span><span ne="0.8076315473412294">);</span></span>
<span><span ne="0.6949197080132896">            System.out.</span><span ne="0.8267103044886711">println</span><span ne="0.45817459703508523">(</span><span ne="0.6676100548384768">"Trailing comma allowed: "</span><span ne="0.33460027447042395"> +</span><span ne="0.21610364693842965"> node.</span><span ne="0.9168737569175455">get</span><span ne="0.1251084794891547">(</span><span ne="0.6129964992034407">"a"</span><span ne="0.6849434467483713">).</span><span ne="0.5189147849498715">asInt</span><span ne="0.6128409762984415">()); </span><span ne="0.4734781852706541">// 1</span></span>
<span><span ne="0.17783852129712419">        } </span><span ne="0.48559895381025064">catch</span><span ne="0.6742333161169028"> (Exception </span><span ne="0.5657511056047307">e</span><span ne="0.10893608987088899">) {</span></span>
<span><span ne="0.9628776895284521">            System.out.</span><span ne="0.1342226042179806">println</span><span ne="0.28850920403891867">(</span><span ne="0.4498990889032318">"Trailing comma error: "</span><span ne="0.3135347863224547"> +</span><span ne="0.5133465081562038"> e.</span><span ne="0.43127950898134304">getMessage</span><span ne="0.30507035698174356">());</span></span>
<span><span ne="0.946917393289366">        }</span></span>
<span><span ne="0.9159945650298644">    }</span></span>
<span><span ne="0.7472366873941528">}</span></span>
```

## Real-World War Stories: When Code Becomes Skynet

### The Twitter ID Problem: The Matrix Integer Overflow

Twitter’s tweet IDs exceed JavaScript’s safe integer range. Their API returns:

```
<span><span ne="0.6374626259177946">{</span></span>
<span><span ne="0.47524071770990794">  "id"</span><span ne="0.22042428094656374">: </span><span ne="0.3664689194776062">1234567890123456789</span><span ne="0.16673413620894206">,</span></span>
<span><span ne="0.7047390654152151">  "id_str"</span><span ne="0.5999758277877898">: </span><span ne="0.38823083721727714">"1234567890123456789"</span></span>
<span><span ne="0.6237702841536449">}</span></span>
```

```
<span><span ne="0.7974520725911838">// JavaScript clients lose precision</span></span>
<span><span ne="0.3964629294353792">const</span><span ne="0.821685625885379"> tweet</span><span ne="0.5402516412629041"> =</span><span ne="0.5286850776826159"> {</span></span>
<span><span ne="0.8133679466026167">  "id"</span><span ne="0.3998397817864251">: </span><span ne="0.19210392577024027">1234567890123456789</span><span ne="0.8405129315173088">,</span></span>
<span><span ne="0.7665356557076811">  "id_str"</span><span ne="0.3922409375547464">: </span><span ne="0.40606543777175175">"1234567890123456789"</span></span>
<span><span ne="0.04361272262795979">};</span></span>
<span></span>
<span><span ne="0.055764482646631586">console.</span><span ne="0.5106075442664592">log</span><span ne="0.8891373199576215">(tweet.id);     </span><span ne="0.30689227371507266">// 1234567890123456768 (wrong!)</span></span>
<span><span ne="0.7972364746466818">console.</span><span ne="0.9154907824260727">log</span><span ne="0.3621981716482734">(tweet.id_str); </span><span ne="0.7363159376229242">// "1234567890123456789" (correct)</span></span>
<span></span>
<span><span ne="0.360408899571495">// Must use id_str in JavaScript</span></span>
<span><span ne="0.19557590340693232">const</span><span ne="0.04762202628622392"> tweetFromAPI</span><span ne="0.23970937891170674"> =</span><span ne="0.962122175436592"> JSON</span><span ne="0.7870103132042645">.</span><span ne="0.322369388164496">parse</span><span ne="0.2460437589392831">(</span><span ne="0.08291941566943217">`{</span></span>
<span><span ne="0.0507471744119532">  "id": 1234567890123456789,</span></span>
<span><span ne="0.3324847579247373">  "id_str": "1234567890123456789"</span></span>
<span><span ne="0.9618751629552905">}`</span><span ne="0.0581632469608393">);</span></span>
<span></span>
<span><span ne="0.4194234104390041">console.</span><span ne="0.3309351434082035">log</span><span ne="0.43932119736605724">(tweetFromAPI.id </span><span ne="0.4282011135109377">===</span><span ne="0.3169159054680539"> 1234567890123456789</span><span ne="0.32424943882128765">);  </span><span ne="0.20087216203837854">// false!</span></span>
<span><span ne="0.617800504940515">console.</span><span ne="0.5940507096314329">log</span><span ne="0.07281626231187854">(tweetFromAPI.id_str </span><span ne="0.023324794746226507">===</span><span ne="0.3988229563797352"> "1234567890123456789"</span><span ne="0.42013132964407884">);  </span><span ne="0.12281673418925121">// true</span></span>
```

```
<span><span ne="0.6775659925339163"># Python handles large integers correctly</span></span>
<span><span ne="0.3377607695618442">import</span><span ne="0.05948405384213484"> json</span></span>
<span></span>
<span><span ne="0.19732265222826573">tweet_json </span><span ne="0.5587598917538347">=</span><span ne="0.0073793811800173525"> '{"id": 1234567890123456789, "id_str": "1234567890123456789"}'</span></span>
<span><span ne="0.03199512085470524">tweet </span><span ne="0.8827782758427055">=</span><span ne="0.016917816177467015"> json.loads(tweet_json)</span></span>
<span></span>
<span><span ne="0.5155295610033197">print</span><span ne="0.7792724672820155">(tweet[</span><span ne="0.9321546154794007">'id'</span><span ne="0.9230556215961949">] </span><span ne="0.515284121511915">==</span><span ne="0.22537903026149186"> 1234567890123456789</span><span ne="0.8933792556327105">)      </span><span ne="0.46792981298946223"># True</span></span>
<span><span ne="0.09781408282508008">print</span><span ne="0.9021159397322713">(tweet[</span><span ne="0.8533671077120568">'id_str'</span><span ne="0.9744161097116709">] </span><span ne="0.13464868138060015">==</span><span ne="0.15201079746705648"> "1234567890123456789"</span><span ne="0.9400639479181216">) </span><span ne="0.23657582988128933"># True</span></span>
<span></span>
<span><span ne="0.09518400720818398"># Python clients can use either field safely</span></span>
```

### The PostgreSQL JSON Type: Foundation’s Psychohistory Database

PostgreSQL’s JSON type preserves exact text representation, while JSONB normalizes it:

```
<span><span ne="0.9856097514806998">-- Create test table</span></span>
<span><span ne="0.45829577914597586">CREATE</span><span ne="0.7407504632440315"> TABLE</span><span ne="0.8907470912589147"> json_test</span><span ne="0.739539729888804"> (</span></span>
<span><span ne="0.10060408739699911">    id </span><span ne="0.9876307660129392">SERIAL</span><span ne="0.8048433266197521"> PRIMARY KEY</span><span ne="0.4108728598540029">,</span></span>
<span><span ne="0.6756016071024752">    data_json </span><span ne="0.6687373439361914">JSON</span><span ne="0.9723352189986584">,</span></span>
<span><span ne="0.41288771965537674">    data_jsonb JSONB</span></span>
<span><span ne="0.5775796186753526">);</span></span>
<span></span>
<span><span ne="0.9001134645090272">-- Insert identical data</span></span>
<span><span ne="0.1450896660097858">INSERT INTO</span><span ne="0.44779011060328267"> json_test (data_json, data_jsonb) </span></span>
<span><span ne="0.10896531324359071">VALUES</span><span ne="0.060051131107340394"> (</span><span ne="0.9920745982130359">'{"b": 1, "a": 2}'</span><span ne="0.2227109426839312">, </span><span ne="0.37203700643794235">'{"b": 1, "a": 2}'</span><span ne="0.8324384331442104">);</span></span>
<span></span>
<span><span ne="0.6442014867631366">-- JSON preserves original formatting</span></span>
<span><span ne="0.592837632194045">SELECT</span><span ne="0.20589117735201146"> data_json </span><span ne="0.6489695335402706">FROM</span><span ne="0.09081453348381263"> json_test;</span></span>
<span><span ne="0.42960705584333636">-- Returns: {"b": 1, "a": 2}</span></span>
<span></span>
<span><span ne="0.41914720943446293">-- JSONB normalizes and sorts keys  </span></span>
<span><span ne="0.613777632635073">SELECT</span><span ne="0.42820455377603506"> data_jsonb </span><span ne="0.5275987944016338">FROM</span><span ne="0.03750024879910552"> json_test;</span></span>
<span><span ne="0.6636750322379116">-- Returns: {"a": 2, "b": 1}</span></span>
<span></span>
<span><span ne="0.5512059105969198">-- This affects application behavior</span></span>
<span><span ne="0.6901020753847514">INSERT INTO</span><span ne="0.47977836718189637"> json_test (data_json, data_jsonb) </span></span>
<span><span ne="0.9438156732190768">VALUES</span><span ne="0.5131540962813648"> (</span><span ne="0.007130795654332278">'{"price": 19.99}'</span><span ne="0.07254058873337221">, </span><span ne="0.08525634117906422">'{"price": 19.99}'</span><span ne="0.38586180169395057">);</span></span>
<span></span>
<span><span ne="0.3508689986480348">-- Extracting values may behave differently</span></span>
<span><span ne="0.10914019053680857">SELECT</span><span ne="0.29720823855001943"> data_json</span><span ne="0.13415580510156622">-&gt;&gt;</span><span ne="0.011242678703906939">'price'</span><span ne="0.2881676449861653"> as</span><span ne="0.97958096204163"> json_price, </span></span>
<span><span ne="0.45642134912638355">       data_jsonb</span><span ne="0.29929885385223876">-&gt;&gt;</span><span ne="0.11794723871395585">'price'</span><span ne="0.5151618501670272"> as</span><span ne="0.13066169462975352"> jsonb_price </span></span>
<span><span ne="0.207680534441257">FROM</span><span ne="0.49652247655754866"> json_test </span><span ne="0.12167612699086539">WHERE</span><span ne="0.30773260397394764"> id </span><span ne="0.9858196590780558">=</span><span ne="0.2637482812213362"> 2</span><span ne="0.8925757834880126">;</span></span>
<span><span ne="0.6427480505118478">-- Both return: "19.99"</span></span>
<span></span>
<span><span ne="0.7125293366580225">-- But binary operations only work on JSONB</span></span>
<span><span ne="0.3141272088233281">SELECT</span><span ne="0.6703675820362438"> *</span><span ne="0.28593333939534926"> FROM</span><span ne="0.989950433262135"> json_test </span><span ne="0.33015261630352577">WHERE</span><span ne="0.32657944897690716"> data_jsonb @</span><span ne="0.4245603586053581">&gt;</span><span ne="0.16636360699266484"> '{"a": 2}'</span><span ne="0.9099655965302468">;  </span><span ne="0.5381342894985587">-- Works</span></span>
<span><span ne="0.3195614136741407">-- SELECT * FROM json_test WHERE data_json @&gt; '{"a": 2}';  -- Error!</span></span>
```

### The MongoDB Extended JSON Problem: The Hitchhiker’s Guide to NoSQL

MongoDB uses Extended JSON which includes additional types:

```
<span><span ne="0.019978864614730085">// Standard JSON</span></span>
<span><span ne="0.3462675874796203">{</span></span>
<span><span ne="0.24590057120207753">  "date"</span><span ne="0.8095415427406363">: </span><span ne="0.7423754109793484">"2023-01-15T10:30:00.000Z"</span><span ne="0.010025316680992158">,</span></span>
<span><span ne="0.034427011526072415">  "id"</span><span ne="0.7705359230765452">: </span><span ne="0.391756136835549">"507f1f77bcf86cd799439011"</span></span>
<span><span ne="0.5216093233386097">}</span></span>
<span></span>
<span><span ne="0.13658743637800708">// MongoDB Extended JSON</span></span>
<span><span ne="0.7736744534111962">{</span></span>
<span><span ne="0.4130247056609859">  "date"</span><span ne="0.9440837344651857">: {</span><span ne="0.5919454170461061">"$date"</span><span ne="0.6194843019774395">: {</span><span ne="0.09478343341566664">"$numberLong"</span><span ne="0.08484751890851494">: </span><span ne="0.047365785509157265">"1673780200000"</span><span ne="0.21963323728657014">}},</span></span>
<span><span ne="0.34551887792303115">  "id"</span><span ne="0.4492074338295179">: {</span><span ne="0.23231078030223895">"$oid"</span><span ne="0.36211420092941804">: </span><span ne="0.8544918110448834">"507f1f77bcf86cd799439011"</span><span ne="0.42920088387655986">}</span></span>
<span><span ne="0.657476082007433">}</span></span>
```

```
<span><span ne="0.5793445946870847">// JavaScript with MongoDB driver</span></span>
<span><span ne="0.4914607750981188">const</span><span ne="0.1879897268769608"> { </span><span ne="0.4896267879090548">MongoClient</span><span ne="0.8692002985553248">, </span><span ne="0.5789982340696507">ObjectId</span><span ne="0.34215213227024344"> } </span><span ne="0.09960256275665902">=</span><span ne="0.2730224183982195"> require</span><span ne="0.9081188090514628">(</span><span ne="0.5869401972146732">'mongodb'</span><span ne="0.4884536281183225">);</span></span>
<span></span>
<span><span ne="0.2568207937435084">// Data going into MongoDB</span></span>
<span><span ne="0.10464444611142276">const</span><span ne="0.024982962551685195"> document</span><span ne="0.3578955266633995"> =</span><span ne="0.4380063032063126"> {</span></span>
<span><span ne="0.8220237464667327">  _id: </span><span ne="0.05558617991437076">new</span><span ne="0.9749065813845502"> ObjectId</span><span ne="0.5188540757998944">(</span><span ne="0.4156272519145858">"507f1f77bcf86cd799439011"</span><span ne="0.9563862208176469">),</span></span>
<span><span ne="0.6148238199937273">  created_at: </span><span ne="0.38627958825178754">new</span><span ne="0.0998042701005063"> Date</span><span ne="0.10234777692806074">(</span><span ne="0.675136886265076">"2023-01-15T10:30:00.000Z"</span><span ne="0.581502930369485">),</span></span>
<span><span ne="0.35973958863063116">  count: </span><span ne="0.5195955400392221">42</span></span>
<span><span ne="0.3816460038655374">};</span></span>
<span></span>
<span><span ne="0.7451345227630434">// When exported as Extended JSON (using MongoDB's EJSON)</span></span>
<span><span ne="0.5035940236427798">const</span><span ne="0.6130207955680848"> EJSON</span><span ne="0.1808557744552226"> =</span><span ne="0.10188468206475054"> require</span><span ne="0.3312864753364114">(</span><span ne="0.7770697512678593">'bson'</span><span ne="0.25273380548307023">).</span><span ne="0.9582441388958886">EJSON</span><span ne="0.6774524564708151">;</span></span>
<span><span ne="0.5197301940931945">const</span><span ne="0.26451938405637987"> extendedJson</span><span ne="0.48098131902855346"> =</span><span ne="0.5733134347586505"> EJSON</span><span ne="0.921481967909976">.</span><span ne="0.17587737187003905">stringify</span><span ne="0.813720594480287">(document, </span><span ne="0.9907033447369719">null</span><span ne="0.002962252626208972">, </span><span ne="0.25657078481617324">2</span><span ne="0.3689674283818627">);</span></span>
<span><span ne="0.5749822319053212">console.</span><span ne="0.5405028197431901">log</span><span ne="0.9905738704735454">(extendedJson);</span></span>
<span><span ne="0.30275186290869127">/*</span></span>
<span><span ne="0.0005383432785058817">{</span></span>
<span><span ne="0.30097150834305575">  "_id": {"$oid": "507f1f77bcf86cd799439011"},</span></span>
<span><span ne="0.7988554843156122">  "created_at": {"$date": "2023-01-15T10:30:00.000Z"},</span></span>
<span><span ne="0.16011961244006045">  "count": 42</span></span>
<span><span ne="0.5753166038699826">}</span></span>
<span><span ne="0.04359253522641737">*/</span></span>
<span></span>
<span><span ne="0.7591233673642183">// Other languages can't parse this directly</span></span>
```

```
<span><span ne="0.5819725233619399"># Python needs special handling</span></span>
<span><span ne="0.4403092052693024">import</span><span ne="0.1717988359611815"> json</span></span>
<span><span ne="0.42610838559316233">from</span><span ne="0.057283911978584956"> bson </span><span ne="0.016709852949943538">import</span><span ne="0.14542510353136218"> ObjectId</span></span>
<span><span ne="0.7529501774057216">from</span><span ne="0.3727324877706063"> datetime </span><span ne="0.021260452855459633">import</span><span ne="0.3961234388157435"> datetime</span></span>
<span></span>
<span><span ne="0.1331254787463051"># Standard JSON from MongoDB export</span></span>
<span><span ne="0.6413857801170071">extended_json </span><span ne="0.6026400467140756">=</span><span ne="0.6416677954604056"> '''{</span></span>
<span><span ne="0.059262537006377625">  "_id": {"$oid": "507f1f77bcf86cd799439011"},</span></span>
<span><span ne="0.09236690252610624">  "created_at": {"$date": "2023-01-15T10:30:00.000Z"}</span></span>
<span><span ne="0.7550231040362612">}'''</span></span>
<span></span>
<span><span ne="0.8934827234256171"># Custom parser needed</span></span>
<span><span ne="0.08754753204803623">def</span><span ne="0.5855612428003484"> parse_extended_json</span><span ne="0.5675296870889882">(obj):</span></span>
<span><span ne="0.206356309582029">    if</span><span ne="0.12404128646288326"> isinstance</span><span ne="0.8246244155023945">(obj, </span><span ne="0.004013991850735477">dict</span><span ne="0.1776878830878601">):</span></span>
<span><span ne="0.6825441730922913">        if</span><span ne="0.9109527370669063"> '$oid'</span><span ne="0.5755692519444972"> in</span><span ne="0.7415097689938355"> obj:</span></span>
<span><span ne="0.39919844676272376">            return</span><span ne="0.5208191120586909"> ObjectId(obj[</span><span ne="0.4108309197654212">'$oid'</span><span ne="0.8689840073013493">])</span></span>
<span><span ne="0.8559489754382539">        elif</span><span ne="0.6144040339337596"> '$date'</span><span ne="0.40215672582678963"> in</span><span ne="0.13863275608895986"> obj:</span></span>
<span><span ne="0.11616663271692251">            return</span><span ne="0.08321001173527653"> datetime.fromisoformat(obj[</span><span ne="0.8740893412396901">'$date'</span><span ne="0.3151889565511804">].replace(</span><span ne="0.27759775910188467">'Z'</span><span ne="0.8433435858565509">, </span><span ne="0.67028882886686">'+00:00'</span><span ne="0.42260933681484225">))</span></span>
<span><span ne="0.8193529948645285">        else</span><span ne="0.08561213692119596">:</span></span>
<span><span ne="0.23223900765846794">            return</span><span ne="0.5271471331027778"> {k: parse_extended_json(v) </span><span ne="0.8407329817946916">for</span><span ne="0.12234953726010489"> k, v </span><span ne="0.8824196055323779">in</span><span ne="0.3138085225977174"> obj.items()}</span></span>
<span><span ne="0.303295968142409">    elif</span><span ne="0.25211612763028024"> isinstance</span><span ne="0.6170167390784987">(obj, </span><span ne="0.6730909496718305">list</span><span ne="0.9830035912409032">):</span></span>
<span><span ne="0.5366060578790526">        return</span><span ne="0.8045029337713603"> [parse_extended_json(item) </span><span ne="0.47630062571636855">for</span><span ne="0.7221015751252725"> item </span><span ne="0.832180747873032">in</span><span ne="0.5764665595508167"> obj]</span></span>
<span><span ne="0.7245661019833936">    return</span><span ne="0.45581214053966257"> obj</span></span>
<span></span>
<span><span ne="0.9641852654050197">data </span><span ne="0.3630531870686473">=</span><span ne="0.06754025604426572"> json.loads(extended_json, </span><span ne="0.9396159337808385">object_hook</span><span ne="0.30204268385228894">=</span><span ne="0.5666969031068626">parse_extended_json)</span></span>
```

## Mitigation Strategies: The Dune Survival Manual for JSON

### Use Schema Validation: The First Law of JSON Robotics

Define and validate schemas across all services:

```
<span><span ne="0.7166877323023879">// JavaScript validation example</span></span>
<span><span ne="0.9226816353969892">const</span><span ne="0.7327294633255342"> Ajv</span><span ne="0.5592716748591554"> =</span><span ne="0.7931053637015302"> require</span><span ne="0.13847200914161295">(</span><span ne="0.9637228393929378">'ajv'</span><span ne="0.24931227140572765">);</span></span>
<span><span ne="0.33842916776353893">const</span><span ne="0.9062810546958763"> addFormats</span><span ne="0.9315239567536647"> =</span><span ne="0.10875595997867016"> require</span><span ne="0.9411625887137678">(</span><span ne="0.0053299565231432755">'ajv-formats'</span><span ne="0.738522446079426">);</span></span>
<span></span>
<span><span ne="0.43055508398179343">const</span><span ne="0.23775850977609547"> ajv</span><span ne="0.0972136603808278"> =</span><span ne="0.33375804932162856"> new</span><span ne="0.8801912873891946"> Ajv</span><span ne="0.0793435128482316">();</span></span>
<span><span ne="0.659462972444133">addFormats</span><span ne="0.9780766102452323">(ajv);</span></span>
<span></span>
<span><span ne="0.7835975411150741">const</span><span ne="0.7462392514343316"> schema</span><span ne="0.8068695930404226"> =</span><span ne="0.6482610499713188"> {</span></span>
<span><span ne="0.19663528780424133">  type: </span><span ne="0.46008347087367696">'object'</span><span ne="0.5026629898640149">,</span></span>
<span><span ne="0.9125001565542226">  properties: {</span></span>
<span><span ne="0.036047861004162685">    id: { type: </span><span ne="0.5618211549881412">'string'</span><span ne="0.8971642718045242">, pattern: </span><span ne="0.15247432024574092">'^[0-9]+$'</span><span ne="0.37354130903990945"> },</span></span>
<span><span ne="0.2929277654430217">    price: { type: </span><span ne="0.43423729877225326">'number'</span><span ne="0.5831093418269759">, multipleOf: </span><span ne="0.09518216652427647">0.01</span><span ne="0.8691853674132839"> }</span></span>
<span><span ne="0.749839600717982">  },</span></span>
<span><span ne="0.7810709059774691">  required: [</span><span ne="0.9240705466634199">'id'</span><span ne="0.12997341632994586">, </span><span ne="0.011927810588088339">'price'</span><span ne="0.7377377369274205">]</span></span>
<span><span ne="0.1563200465554555">};</span></span>
<span></span>
<span><span ne="0.4035700501570001">const</span><span ne="0.8395463944042254"> validate</span><span ne="0.7019933471625579"> =</span><span ne="0.0036210295296078554"> ajv.</span><span ne="0.16289193691688075">compile</span><span ne="0.9764488714983981">(schema);</span></span>
<span></span>
<span><span ne="0.9912076210392003">const</span><span ne="0.6595075934059959"> data</span><span ne="0.8014798873470473"> =</span><span ne="0.4717518227339256"> { id: </span><span ne="0.9569003885231195">"9007199254740992"</span><span ne="0.3876745621913873">, price: </span><span ne="0.9345292416197304">19.99</span><span ne="0.8651160381188397"> };</span></span>
<span><span ne="0.33978466909554716">const</span><span ne="0.7801730987798062"> valid</span><span ne="0.12740942176767778"> =</span><span ne="0.8167653336194011"> validate</span><span ne="0.5516058787399986">(data);</span></span>
<span></span>
<span><span ne="0.9584718539841074">if</span><span ne="0.10172860435475706"> (</span><span ne="0.8108076009774157">!</span><span ne="0.43043073810107335">valid) {</span></span>
<span><span ne="0.026208597738166528">  console.</span><span ne="0.4581749578063512">log</span><span ne="0.9184329029544475">(</span><span ne="0.5539708228422472">'Validation errors:'</span><span ne="0.26067353992550646">, validate.errors);</span></span>
<span><span ne="0.4769538293827127">}</span></span>
```

```
<span><span ne="0.36043203600092666"># Python validation with jsonschema</span></span>
<span><span ne="0.09263847796079128">import</span><span ne="0.35570407088099"> json</span></span>
<span><span ne="0.7805438690881246">import</span><span ne="0.0314769245747214"> jsonschema</span></span>
<span></span>
<span><span ne="0.9545363464922022">schema </span><span ne="0.01642191056253295">=</span><span ne="0.38583833849124416"> {</span></span>
<span><span ne="0.9687685514571778">    "type"</span><span ne="0.8770219656939111">: </span><span ne="0.006530773436178805">"object"</span><span ne="0.5453516741778835">,</span></span>
<span><span ne="0.9683759798482693">    "properties"</span><span ne="0.6454243479564611">: {</span></span>
<span><span ne="0.6361998245123454">        "id"</span><span ne="0.08358598617381341">: {</span><span ne="0.33385156225820256">"type"</span><span ne="0.6586350093398478">: </span><span ne="0.8606724896207008">"string"</span><span ne="0.4829080176253048">, </span><span ne="0.8131641707750623">"pattern"</span><span ne="0.9290291398662416">: </span><span ne="0.3170645743746724">"^[0-9]+$"</span><span ne="0.7754626844454775">},</span></span>
<span><span ne="0.7727210905847771">        "price"</span><span ne="0.5414260075473354">: {</span><span ne="0.8510220752056846">"type"</span><span ne="0.29501975735220465">: </span><span ne="0.007569977858430943">"number"</span><span ne="0.06912629109153978">, </span><span ne="0.7904445428153927">"multipleOf"</span><span ne="0.5607639269746">: </span><span ne="0.27998483296255194">0.01</span><span ne="0.2184318303051106">}</span></span>
<span><span ne="0.5294978580407148">    },</span></span>
<span><span ne="0.45754608757837567">    "required"</span><span ne="0.6288924600593726">: [</span><span ne="0.5168081901852395">"id"</span><span ne="0.1690270975084074">, </span><span ne="0.16382211771404964">"price"</span><span ne="0.6511969137967883">]</span></span>
<span><span ne="0.2788818814449482">}</span></span>
<span></span>
<span><span ne="0.7177493974705168">data </span><span ne="0.4315289997656908">=</span><span ne="0.822293286807504"> {</span><span ne="0.9236456530873891">"id"</span><span ne="0.9849308444275411">: </span><span ne="0.9753025667687529">"9007199254740992"</span><span ne="0.3178548015856394">, </span><span ne="0.2736951033061159">"price"</span><span ne="0.31838527638994873">: </span><span ne="0.6602905684150495">19.99</span><span ne="0.9490031052716683">}</span></span>
<span></span>
<span><span ne="0.9372048024481057">try</span><span ne="0.6003430507505723">:</span></span>
<span><span ne="0.22571436296291802">    jsonschema.validate(</span><span ne="0.757820771295239">instance</span><span ne="0.22476443753603825">=</span><span ne="0.9881844555265397">data, </span><span ne="0.06739185201050646">schema</span><span ne="0.9618572124837732">=</span><span ne="0.9172719780744104">schema)</span></span>
<span><span ne="0.8415446036986648">    print</span><span ne="0.9244817276920313">(</span><span ne="0.583722911155538">"Data is valid"</span><span ne="0.5518709367668024">)</span></span>
<span><span ne="0.049618372974596925">except</span><span ne="0.18697710994701133"> jsonschema.ValidationError </span><span ne="0.6317490948498502">as</span><span ne="0.2586992738609897"> e:</span></span>
<span><span ne="0.6492644873034249">    print</span><span ne="0.3204104555956513">(</span><span ne="0.004904980511696522">f</span><span ne="0.4375486538119828">"Validation error: </span><span ne="0.3989796747372568">{</span><span ne="0.22372677149288644">e.message</span><span ne="0.6863299537633208">}</span><span ne="0.7048515242133011">"</span><span ne="0.09511649776678455">)</span></span>
```

### Normalize Data Types: Ender’s Data Normalization Game

Establish conventions for your organization:

```
<span><span ne="0.6986055792844735">// JavaScript - safe serialization helpers</span></span>
<span><span ne="0.4676236569484824">function</span><span ne="0.4788576539223979"> safeJSONStringify</span><span ne="0.21122529879107543">(</span><span ne="0.6540233995374624">obj</span><span ne="0.9605877867826677">) {</span></span>
<span><span ne="0.005092898287179293">  return</span><span ne="0.6711562124333916"> JSON</span><span ne="0.8573085600035569">.</span><span ne="0.20460477694124324">stringify</span><span ne="0.31182344294886843">(obj, (</span><span ne="0.6581665071698214">key</span><span ne="0.06740903432356726">, </span><span ne="0.37659213318316753">value</span><span ne="0.9990971373695156">) </span><span ne="0.5102729932651481">=&gt;</span><span ne="0.5300639843770735"> {</span></span>
<span><span ne="0.04675947381937817">    // Convert large numbers to strings</span></span>
<span><span ne="0.11561346434088338">    if</span><span ne="0.8593500053493014"> (</span><span ne="0.26968139569942706">typeof</span><span ne="0.41239988403104033"> value </span><span ne="0.7804410361281058">===</span><span ne="0.036259490563512076"> 'number'</span><span ne="0.007750846200254569"> &amp;&amp;</span><span ne="0.17505909706790668"> Math.</span><span ne="0.10727288870375518">abs</span><span ne="0.7807056831567825">(value) </span><span ne="0.6070839500823367">&gt;</span><span ne="0.6624772498284768"> Number.MAX_SAFE_INTEGER) {</span></span>
<span><span ne="0.6959639195618564">      return</span><span ne="0.6475050144077015"> value.</span><span ne="0.3574066518764967">toString</span><span ne="0.7179762467000489">();</span></span>
<span><span ne="0.11447178664861901">    }</span></span>
<span><span ne="0.7745013743526877">    </span></span>
<span><span ne="0.940797840230072">    // Convert BigInt to string</span></span>
<span><span ne="0.5753906054160063">    if</span><span ne="0.770039111003188"> (</span><span ne="0.45721985557238487">typeof</span><span ne="0.5077609055766907"> value </span><span ne="0.06144845266622334">===</span><span ne="0.7564580812485258"> 'bigint'</span><span ne="0.12480745554637418">) {</span></span>
<span><span ne="0.11237749576860934">      return</span><span ne="0.9606749968833009"> value.</span><span ne="0.7992712434924025">toString</span><span ne="0.9041772922718434">();</span></span>
<span><span ne="0.1421732974709906">    }</span></span>
<span><span ne="0.6093509611152724">    </span></span>
<span><span ne="0.5785716097988438">    // Normalize dates to ISO 8601</span></span>
<span><span ne="0.7486795311193435">    if</span><span ne="0.7883712391030793"> (value </span><span ne="0.8957910030902706">instanceof</span><span ne="0.17697095954977582"> Date</span><span ne="0.3548778978990016">) {</span></span>
<span><span ne="0.7512982747313229">      return</span><span ne="0.09440940742052972"> value.</span><span ne="0.17122685335161025">toISOString</span><span ne="0.8418730369200408">();</span></span>
<span><span ne="0.8295903393028423">    }</span></span>
<span><span ne="0.03705561654452283">    </span></span>
<span><span ne="0.17459308434306675">    return</span><span ne="0.289683870925627"> value;</span></span>
<span><span ne="0.7692056458618249">  });</span></span>
<span><span ne="0.4124147777153341">}</span></span>
<span></span>
<span><span ne="0.4915715235572232">const</span><span ne="0.2843246890882434"> data</span><span ne="0.8836307335507467"> =</span><span ne="0.1415501305617347"> {</span></span>
<span><span ne="0.4596811177415592">  id: </span><span ne="0.7371579320884042">BigInt</span><span ne="0.9492045919846419">(</span><span ne="0.05891254607866048">"9007199254740992"</span><span ne="0.9592796603552789">),</span></span>
<span><span ne="0.1495123937524051">  created_at: </span><span ne="0.5244826476868871">new</span><span ne="0.10722357289649442"> Date</span><span ne="0.46641905830278896">(),</span></span>
<span><span ne="0.42898309313361216">  price: </span><span ne="0.97543512424633">19.99</span></span>
<span><span ne="0.3960738112265727">};</span></span>
<span></span>
<span><span ne="0.6425761248330711">console.</span><span ne="0.3463184357151051">log</span><span ne="0.7386068411918084">(</span><span ne="0.8234721680389979">safeJSONStringify</span><span ne="0.031041909082318075">(data));</span></span>
<span><span ne="0.7553487595212065">// {"id":"9007199254740992","created_at":"2023-01-15T10:30:00.000Z","price":19.99}</span></span>
```

### Library Selection Matters: Choose Your JSON Parser, Neo

Choose JSON libraries carefully based on your needs:

```
<span><span ne="0.4203279311068078">// JavaScript - handling large integers safely</span></span>
<span><span ne="0.6188528782975321">// Using json-bigint library</span></span>
<span><span ne="0.7019897311575064">const</span><span ne="0.09119108053642855"> JSONbig</span><span ne="0.0744702480696744"> =</span><span ne="0.9476686673340057"> require</span><span ne="0.281842310761385">(</span><span ne="0.9740588981204145">'json-bigint'</span><span ne="0.45190760623758885">);</span></span>
<span></span>
<span><span ne="0.4190794968727257">// Configure JSONbig to handle large numbers</span></span>
<span><span ne="0.7055045052026901">const</span><span ne="0.9126533449464871"> JSONbigConfig</span><span ne="0.538968781361534"> =</span><span ne="0.9866566196138451"> JSONbig</span><span ne="0.3747210700564544">({</span></span>
<span><span ne="0.8777311163913897">  alwaysParseAsBig: </span><span ne="0.4576889027157649">false</span><span ne="0.9733074217565665">,</span></span>
<span><span ne="0.4786374524811138">  useNativeBigInt: </span><span ne="0.03742772816948947">true</span><span ne="0.9482209094231027">,</span></span>
<span><span ne="0.5466390181585677">  storeAsString: </span><span ne="0.1995935786230798">false</span></span>
<span><span ne="0.3695121884522745">});</span></span>
<span></span>
<span><span ne="0.8644479144359914">const</span><span ne="0.9759851070380529"> data</span><span ne="0.9537313956278854"> =</span><span ne="0.16221560746525554"> '{"smallNumber": 123, "largeNumber": 9007199254740993}'</span><span ne="0.5142116984393791">;</span></span>
<span></span>
<span><span ne="0.7776197428893548">// Standard JSON loses precision on this larger number</span></span>
<span><span ne="0.9189425548508187">const</span><span ne="0.924273931770983"> standard</span><span ne="0.6831806494265634"> =</span><span ne="0.7788668298638453"> JSON</span><span ne="0.33847776014854125">.</span><span ne="0.9258740529257314">parse</span><span ne="0.026709525595578598">(data);</span></span>
<span><span ne="0.7666236383692834">console.</span><span ne="0.20737301907702266">log</span><span ne="0.23574087631809382">(standard.largeNumber </span><span ne="0.4974413468002168">===</span><span ne="0.26748824468074084"> 9007199254740993</span><span ne="0.48616543754002295">); </span><span ne="0.9845821039472887">// false (precision lost)</span></span>
<span><span ne="0.4765067702228456">console.</span><span ne="0.17275307396607353">log</span><span ne="0.05431393912747473">(standard.largeNumber); </span><span ne="0.01754644484473311">// 9007199254740992</span></span>
<span></span>
<span><span ne="0.8331018896827284">// JSONbig preserves precision</span></span>
<span><span ne="0.021464783699740586">const</span><span ne="0.6364648976539968"> safe</span><span ne="0.8033060374385342"> =</span><span ne="0.7326394809561213"> JSONbigConfig.</span><span ne="0.9532192359568088">parse</span><span ne="0.730719084196947">(data);</span></span>
<span><span ne="0.3782996161868587">console.</span><span ne="0.140466567241061">log</span><span ne="0.9112743932724171">(safe.largeNumber </span><span ne="0.15512537073473776">===</span><span ne="0.12600599915917698"> 9007199254740993</span><span ne="0.6662611576752132">n</span><span ne="0.8804698492017953">); </span><span ne="0.42452749497621733">// true (BigInt)</span></span>
<span><span ne="0.6946084148708167">console.</span><span ne="0.19109337276299398">log</span><span ne="0.5904412372579849">(safe.largeNumber); </span><span ne="0.35864220659341606">// 9007199254740993n</span></span>
```

```
<span><span ne="0.7836713790831659">// Java - Jackson configuration for safety</span></span>
<span></span>
<span><span ne="0.5826580174656818">import</span><span ne="0.8139118412221158"> com.fasterxml.jackson.databind.ObjectMapper;</span></span>
<span><span ne="0.8483274711148433">import</span><span ne="0.21861186554006218"> com.fasterxml.jackson.databind.DeserializationFeature;</span></span>
<span><span ne="0.5558038207606223">import</span><span ne="0.9256047407614638"> com.fasterxml.jackson.databind.JsonNode;</span></span>
<span><span ne="0.8072586860907217">import</span><span ne="0.9500739357407987"> com.fasterxml.jackson.core.JsonParser;</span></span>
<span></span>
<span><span ne="0.7561963778107522">import</span><span ne="0.1026038121967291"> java.math.BigDecimal;</span></span>
<span><span ne="0.6157212584761196">import</span><span ne="0.6715656724703599"> java.math.BigInteger;</span></span>
<span></span>
<span><span ne="0.21862876487335658">public</span><span ne="0.971676158100753"> class</span><span ne="0.46760520010744344"> JsonSafeParsingDemo</span><span ne="0.30278441427843206"> {</span></span>
<span><span ne="0.9586504471330839">    public</span><span ne="0.8981906608802668"> static</span><span ne="0.203647630593928"> void</span><span ne="0.19108055585705475"> main</span><span ne="0.5243121995330774">(</span><span ne="0.1321800458338389">String</span><span ne="0.21784193076735614">[] </span><span ne="0.19386507929425012">args</span><span ne="0.5471766639795935">) </span><span ne="0.02526756924147">throws</span><span ne="0.021027154766488088"> Exception {</span></span>
<span><span ne="0.41426711207997746">        ObjectMapper safeMapper </span><span ne="0.30906738361292785">=</span><span ne="0.03203966335002173"> new</span><span ne="0.4036387356322265"> ObjectMapper</span><span ne="0.5133987572211283">();</span></span>
<span></span>
<span><span ne="0.91159635505664">        // Configure for precision and safety</span></span>
<span><span ne="0.09689155949860606">        safeMapper.</span><span ne="0.6843320596840268">configure</span><span ne="0.5644341891222222">(DeserializationFeature.USE_BIG_DECIMAL_FOR_FLOATS, </span><span ne="0.14270795684977056">true</span><span ne="0.7231471602976147">);</span></span>
<span><span ne="0.38489317853369553">        safeMapper.</span><span ne="0.7657178787886499">configure</span><span ne="0.8892749870021265">(DeserializationFeature.USE_BIG_INTEGER_FOR_INTS, </span><span ne="0.3157454093256127">true</span><span ne="0.7234668779534549">);</span></span>
<span><span ne="0.33906111082854795">        safeMapper.</span><span ne="0.7842756692546743">configure</span><span ne="0.2970207848030473">(JsonParser.Feature.STRICT_DUPLICATE_DETECTION, </span><span ne="0.8573735748889276">true</span><span ne="0.6437241079948536">);</span></span>
<span></span>
<span><span ne="0.6222756956604342">        String json </span><span ne="0.23064422633241755">=</span><span ne="0.1358544260765262"> """{"price": 19.99, "id": 9007199254740992}"""</span><span ne="0.31922594106456925">;</span></span>
<span><span ne="0.7590273251702607">        JsonNode node </span><span ne="0.4707610511483574">=</span><span ne="0.16320998362092287"> safeMapper.</span><span ne="0.0005787990197417825">readTree</span><span ne="0.21589256760744957">(json);</span></span>
<span></span>
<span><span ne="0.14306640875451992">        // Now we get BigDecimal and BigInteger types</span></span>
<span><span ne="0.3899508376445803">        System.out.</span><span ne="0.5453994327804194">println</span><span ne="0.07727849274747123">(</span><span ne="0.8806425897170075">"Price type: "</span><span ne="0.5257409159962843"> +</span><span ne="0.0669086532577775"> node.</span><span ne="0.20394678577492165">get</span><span ne="0.47284297463393143">(</span><span ne="0.05825856506233129">"price"</span><span ne="0.7914226937512204">).</span><span ne="0.7366030779135359">numberValue</span><span ne="0.7298867464147152">().</span><span ne="0.9626916573491364">getClass</span><span ne="0.4925834176592222">().</span><span ne="0.39191853080324146">getSimpleName</span><span ne="0.3325804841856844">());  </span><span ne="0.5651267009418652">// BigDecimal</span></span>
<span><span ne="0.6235465839663791">        System.out.</span><span ne="0.242401208714215">println</span><span ne="0.17409462353607152">(</span><span ne="0.4423271881590122">"ID type: "</span><span ne="0.9594603368062896"> +</span><span ne="0.8068641769597166"> node.</span><span ne="0.07339074176017968">get</span><span ne="0.8313218395177766">(</span><span ne="0.26832884674046287">"id"</span><span ne="0.8469740490903891">).</span><span ne="0.4487862505512815">numberValue</span><span ne="0.0882757588579266">().</span><span ne="0.8364103671125773">getClass</span><span ne="0.24397218178516467">().</span><span ne="0.6288916210568671">getSimpleName</span><span ne="0.750899478184257">());       </span><span ne="0.2970983944885388">// BigInteger</span></span>
<span></span>
<span><span ne="0.5820541724741133">        // Values are preserved with full precision</span></span>
<span><span ne="0.2662088847097651">        System.out.</span><span ne="0.4351957379217676">println</span><span ne="0.03061380078887732">(</span><span ne="0.32206859942664734">"Price value: "</span><span ne="0.15376084436442772"> +</span><span ne="0.09752028335223051"> node.</span><span ne="0.4806369862650498">get</span><span ne="0.30722191061472803">(</span><span ne="0.1504427283915546">"price"</span><span ne="0.9095404748566366">).</span><span ne="0.8359010348380309">decimalValue</span><span ne="0.363539144503657">()); </span><span ne="0.47080202472207944">// 19.99</span></span>
<span><span ne="0.7773728673428182">        System.out.</span><span ne="0.6290415213953323">println</span><span ne="0.12135117924816641">(</span><span ne="0.8773592423922814">"ID value: "</span><span ne="0.8847831185192269"> +</span><span ne="0.9394349988532877"> node.</span><span ne="0.05283905541227718">get</span><span ne="0.9026445275737491">(</span><span ne="0.2639247966099856">"id"</span><span ne="0.28098677258419213">).</span><span ne="0.5609790738135251">bigIntegerValue</span><span ne="0.27153808527701395">());    </span><span ne="0.8966119326938803">// 9007199254740992</span></span>
<span><span ne="0.1884948062044981">    }</span></span>
<span><span ne="0.006224668633550978">}</span></span>
```

### Test Cross-Language Compatibility: The Martian Compatibility Protocol

Create comprehensive test suites that verify data round-trips correctly across all services in your architecture. This is critical for detecting subtle incompatibilities before they cause production issues.

**Essential Test Categories:**

**Numeric Precision Tests:**

-   Test integers at the boundaries of JavaScript’s safe integer range (2^53-1)
-   Verify large database IDs don’t lose precision when passed through JavaScript services
-   Test decimal values that are commonly problematic (0.1, 0.2, financial amounts)
-   Validate that monetary calculations remain exact across all services

**Unicode and String Handling:**

-   Test strings with different Unicode normalization forms (NFC vs NFD)
-   Verify proper handling of emoji, accented characters, and non-Latin scripts
-   Test strings containing control characters, null bytes, and escape sequences
-   Validate that search and comparison operations work consistently

**Data Structure Integrity:**

-   Test object key ordering preservation where required (especially for cryptographic operations)
-   Verify null vs undefined vs missing field handling across languages
-   Test empty arrays vs null arrays vs missing arrays
-   Validate nested object structures maintain their shape

**Date and Time Consistency:**

-   Test ISO 8601 strings with and without timezone information
-   Verify Unix timestamp handling (seconds vs milliseconds)
-   Test edge cases like leap seconds, daylight saving transitions
-   Validate that date arithmetic produces consistent results

**Error Handling Uniformity:**

-   Test malformed JSON handling (trailing commas, duplicate keys, invalid escapes)
-   Verify that validation errors are consistent across services
-   Test boundary conditions (very large payloads, deeply nested objects)
-   Validate that error responses maintain the same format

**Cryptographic Consistency:**

-   Test that HMAC signatures match when the same data is serialized by different services
-   Verify that content hashes are identical for semantically equivalent data
-   Test digital signature verification across language boundaries
-   Validate that canonical JSON serialization works consistently

**Performance and Memory Behavior:**

-   Test large payload handling to identify memory usage differences
-   Verify that streaming vs tree parsing produces identical results
-   Test concurrent parsing behavior under load
-   Validate that garbage collection patterns don’t affect data integrity

**Real-World Scenario Testing:**

-   Test actual API payloads from your production systems
-   Verify third-party integration data (payment processors, external APIs)
-   Test data migration scenarios between different storage systems
-   Validate that cached vs fresh data produces identical results

**Automated Compatibility Matrix:**

Set up automated tests that run the same test cases against services written in different languages, creating a compatibility matrix that shows which combinations work reliably. This should be part of your CI/CD pipeline and run before any deployment that changes JSON handling logic.

## Conclusion: May the Parse Be With You

JSON’s elegant simplicity is both its **greatest strength and also its weakness**. What looks like a straightforward data format transforms into something a bit more complicated when you start moving data between systems that were built by different teams, using different languages, with different assumptions about how the world works. **The issues are real**: large integers silently lose precision, Unicode strings get mangled in creative ways, object key ordering disappears when you need it most, and date parsing becomes a choose-your-own-adventure game. But here’s the thing: these problems won’t hit you every day.

When these issues do surface, they create some of the most soul-crushing debugging experiences in software development. You’ll spend **days tracking down** why user “José” can log in but “José” (with a different Unicode normalization) cannot. You’ll pull your hair out wondering why your HMAC validation works in development but fails in production, only to discover it’s because your API Gateway reorders the JSON keys.

The intermittent nature of these bugs makes them particularly insidious. They **hide in edge cases**, waiting for that one specific user ID, that one particular Unicode sequence, or that one unfortunate key ordering to surface in production and ruin your weekend.

So what’s the solution? Use Protocol Buffers! Just kidding, don’t get me started on that one. **Establish clear conventions**. Validate schemas rigorously. Test cross-language compatibility early and often. Choose your **libraries based on their track record**, not just their performance benchmarks. And when something “impossible” happens in production, remember that JSON parsers are written by humans with different constraints and caffeine levels. JSON isn’t JSON across all languages, but with **proper engineering discipline** and a **healthy dose of paranoia**, you can build systems that **work reliably** despite these inconsistencies. The key is acknowledging that the problem exists in the first place, rather than pretending JSON is the simple, universal format it appears to be.

Remember: in a world of imperfect standards and human-written and soon AI-written parsers, a **little skepticism goes a long way**. Trust, but verify. And always test your edge cases before they test you.
