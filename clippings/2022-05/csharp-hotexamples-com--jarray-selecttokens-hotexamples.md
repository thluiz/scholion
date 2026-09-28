---
url: "https://csharp.hotexamples.com/examples/Newtonsoft.Json.Linq/JArray/SelectTokens/php-jarray-selecttokens-method-examples.html"
captured_at: "2022-05-10T09:58:42-03:00"
title: "JArray.SelectTokens, Newtonsoft.Json.Linq C# (CSharp) Code Examples - HotExamples"
domain: "csharp-hotexamples-com"
---

# C# (CSharp) Newtonsoft.Json.Linq JArray.SelectTokens Examples

**C# (CSharp) Newtonsoft.Json.Linq JArray.SelectTokens - 12 examples found**. These are the top rated real world C# (CSharp) examples of **Newtonsoft.Json.Linq.JArray.SelectTokens** extracted from open source projects. You can rate examples to help us improve the quality of examples.

Programming Language: C# (CSharp)

Namespace/Package Name: Newtonsoft.Json.Linq

Class/Type: [JArray](https://csharp.hotexamples.com/examples/Newtonsoft.Json.Linq/JArray/-/php-jarray-class-examples.html)

Method/Function: SelectTokens

Examples at hotexamples.com: 12

```
        public void NestedQuery()
        {
            JArray a = new JArray(
                new JObject(
                    new JProperty("name", "Bad Boys"),
                    new JProperty("cast", new JArray(
                        new JObject(new JProperty("name", "Will Smith"))))),
                new JObject(
                    new JProperty("name", "Independence Day"),
                    new JProperty("cast", new JArray(
                        new JObject(new JProperty("name", "Will Smith"))))),
                new JObject(
                    new JProperty("name", "The Rock"),
                    new JProperty("cast", new JArray(
                        new JObject(new JProperty("name", "Nick Cage")))))
                );

            IList<JToken> t = a.SelectTokens("[?(@.cast[?(@.name=='Will Smith')])].name").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(2, t.Count);
            Assert.AreEqual("Bad Boys", (string)t[0]);
            Assert.AreEqual("Independence Day", (string)t[1]);
        }
```

```
        public void GreaterQueryBigInteger()
        {
            JArray a = new JArray(
                new JObject(new JProperty("hi", new BigInteger(1))),
                new JObject(new JProperty("hi", new BigInteger(2))),
                new JObject(new JProperty("hi", new BigInteger(3))));

            IList<JToken> t = a.SelectTokens("[ ?( @.hi > 1 ) ]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(2, t.Count);
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 2)), t[0]));
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 3)), t[1]));
        }
```

```
        public void GreaterOrEqualQuery()
        {
            JArray a = new JArray(
                new JObject(new JProperty("hi", 1)),
                new JObject(new JProperty("hi", 2)),
                new JObject(new JProperty("hi", 2.0)),
                new JObject(new JProperty("hi", 3)));

            IList<JToken> t = a.SelectTokens("[ ?( @.hi >= 1 ) ]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(4, t.Count);
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 1)), t[0]));
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 2)), t[1]));
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 2.0)), t[2]));
            Assert.IsTrue(JToken.DeepEquals(new JObject(new JProperty("hi", 3)), t[3]));
        }
```

```
        public void NoPathQuery()
        {
            JArray a = new JArray(1, 2, 3);

            IList<JToken> t = a.SelectTokens("[ ?( @ > 1 ) ]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(2, t.Count);
            Assert.AreEqual(2, (int)t[0]);
            Assert.AreEqual(3, (int)t[1]);
        }
```

```
        public void MultipleQueries()
        {
            JArray a = new JArray(1, 2, 3, 4, 5, 6, 7, 8, 9);

            // json path does item based evaluation - http://www.sitepen.com/blog/2008/03/17/jsonpath-support/
            // first query resolves array to ints
            // int has no children to query
            IList<JToken> t = a.SelectTokens("[?(@ <> 1)][?(@ <> 4)][?(@ < 7)]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(0, t.Count);
        }
```

```
        public void EvaluateWildcardScanNestResults()
        {
            JObject o1 = new JObject { { "Name", 1 } };
            JObject o2 = new JObject { { "Name", 2 } };
            JObject o3 = new JObject { { "Name", new JObject { { "Name", new JArray(3) } } } };
            JArray a = new JArray(o1, o2, o3);

            IList<JToken> t = a.SelectTokens("$..*").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(9, t.Count);

            Assert.IsTrue(JToken.DeepEquals(a, t[0]));
            Assert.IsTrue(JToken.DeepEquals(o1, t[1]));
            Assert.AreEqual(1, (int)t[2]);
            Assert.IsTrue(JToken.DeepEquals(o2, t[3]));
            Assert.AreEqual(2, (int)t[4]);
            Assert.IsTrue(JToken.DeepEquals(o3, t[5]));
            Assert.IsTrue(JToken.DeepEquals(new JObject { { "Name", new JArray(3) } }, t[6]));
            Assert.IsTrue(JToken.DeepEquals(new JArray(3), t[7]));
            Assert.AreEqual(3, (int)t[8]);
        }
```

```
        public void NotEqualsQuery()
        {
            JArray a = new JArray(
                new JArray(new JObject(new JProperty("hi", "ho"))),
                new JArray(new JObject(new JProperty("hi", "ha"))));

            IList<JToken> t = a.SelectTokens("[ ?( @..hi <> 'ha' ) ]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(1, t.Count);
            Assert.IsTrue(JToken.DeepEquals(new JArray(new JObject(new JProperty("hi", "ho"))), t[0]));
        }
```

```
        public void EvaluateWildcardScan()
        {
            JObject o1 = new JObject { { "Name", 1 } };
            JObject o2 = new JObject { { "Name", 2 } };
            JArray a = new JArray(o1, o2);

            IList<JToken> t = a.SelectTokens("$..*").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(5, t.Count);
            Assert.IsTrue(JToken.DeepEquals(a, t[0]));
            Assert.IsTrue(JToken.DeepEquals(o1, t[1]));
            Assert.AreEqual(1, (int)t[2]);
            Assert.IsTrue(JToken.DeepEquals(o2, t[3]));
            Assert.AreEqual(2, (int)t[4]);
        }
```

```
        public void EvaluateScan()
        {
            JObject o1 = new JObject { { "Name", 1 } };
            JObject o2 = new JObject { { "Name", 2 } };
            JArray a = new JArray(o1, o2);

            IList<JToken> t = a.SelectTokens("$..Name").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(2, t.Count);
            Assert.AreEqual(1, (int)t[0]);
            Assert.AreEqual(2, (int)t[1]);
        }
```

```
        public void EvaluateArrayMultipleIndexes()
        {
            JArray a = new JArray(1, 2, 3, 4);

            IEnumerable<JToken> t = a.SelectTokens("[1,2,0]");
            Assert.IsNotNull(t);
            Assert.AreEqual(3, t.Count());
            Assert.AreEqual(2, (int)t.ElementAt(0));
            Assert.AreEqual(3, (int)t.ElementAt(1));
            Assert.AreEqual(1, (int)t.ElementAt(2));
        }
```

```
        public void EvaluateWildcardArray()
        {
            JArray a = new JArray(1, 2, 3, 4);

            List<JToken> t = a.SelectTokens("[*]").ToList();
            Assert.IsNotNull(t);
            Assert.AreEqual(4, t.Count);
            Assert.AreEqual(1, (int)t[0]);
            Assert.AreEqual(2, (int)t[1]);
            Assert.AreEqual(3, (int)t[2]);
            Assert.AreEqual(4, (int)t[3]);
        }
```

```
        public void EvaluateArraySlice()
        {
            JArray a = new JArray(1, 2, 3, 4, 5, 6, 7, 8, 9);
            IList<JToken> t = null;

            t = a.SelectTokens("[-3:]").ToList();
            Assert.AreEqual(3, t.Count);
            Assert.AreEqual(7, (int)t[0]);
            Assert.AreEqual(8, (int)t[1]);
            Assert.AreEqual(9, (int)t[2]);

            t = a.SelectTokens("[-1:-2:-1]").ToList();
            Assert.AreEqual(1, t.Count);
            Assert.AreEqual(9, (int)t[0]);

            t = a.SelectTokens("[-2:-1]").ToList();
            Assert.AreEqual(1, t.Count);
            Assert.AreEqual(8, (int)t[0]);

            t = a.SelectTokens("[1:1]").ToList();
            Assert.AreEqual(0, t.Count);

            t = a.SelectTokens("[1:2]").ToList();
            Assert.AreEqual(1, t.Count);
            Assert.AreEqual(2, (int)t[0]);

            t = a.SelectTokens("[::-1]").ToList();
            Assert.AreEqual(9, t.Count);
            Assert.AreEqual(9, (int)t[0]);
            Assert.AreEqual(8, (int)t[1]);
            Assert.AreEqual(7, (int)t[2]);
            Assert.AreEqual(6, (int)t[3]);
            Assert.AreEqual(5, (int)t[4]);
            Assert.AreEqual(4, (int)t[5]);
            Assert.AreEqual(3, (int)t[6]);
            Assert.AreEqual(2, (int)t[7]);
            Assert.AreEqual(1, (int)t[8]);

            t = a.SelectTokens("[::-2]").ToList();
            Assert.AreEqual(5, t.Count);
            Assert.AreEqual(9, (int)t[0]);
            Assert.AreEqual(7, (int)t[1]);
            Assert.AreEqual(5, (int)t[2]);
            Assert.AreEqual(3, (int)t[3]);
            Assert.AreEqual(1, (int)t[4]);
        }
```
