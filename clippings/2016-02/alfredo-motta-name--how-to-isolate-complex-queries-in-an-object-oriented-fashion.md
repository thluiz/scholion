---
url: "http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/"
captured_at: "2016-02-07T22:42:34-03:00"
title: "How to isolate complex queries in an object oriented fashion – Alfredo Motta"
domain: "alfredo-motta-name"
---

# The problem

Let's assume we are building a system to search talented football players. A player has the following fields:

|  |  |
| --- | --- |
|  | ActiveRecordSchemadefine  create\_tableplayers  stringforename  stringsurname  birthdate  string  stringnationality  stringpreferredfoot  integershoots  integergoals  integerassists  integerpasses  integersuccessfulpasses  stringname |

And the corresponding active record model is the following:

|  |  |
| --- | --- |
|  | classPlayerActiveRecord  scoperight\_foot->wherepreferred\_foot'right'  scopeleft\_foot->wherepreferred\_foot'left' |

Our application mostly deal with `TalentHunters`, objects whose responsibility is to find good players based on a search criteria. For simplicity let's assume that a search criteria has just three components:

- whether or not the player is part of a big team
- whether or not the player has a good shoot accuracy
- and whether or not the player is young.

Finally let's also assume that our talent hunter only specialise on right foot players. The simplest, fastest implementation we can think is an object that uses the search parameters to build the query using a list of conditional statements. Here is a possible implementation:

|  |  |
| --- | --- |
|  | classTalentHunterWithNaiveQuery  TOP\_TEAMS'ac milan''real madrid''barcelona'  SHOOT\_ACCURACY  MAX\_AGE  initializeoptions  @playing\_for\_top\_teamoptionsfetchplaying\_for\_top\_team  @with\_young\_ageoptionsfetchwith\_young\_age  @with\_great\_accuracyoptionsfetchwith\_great\_accuracy  find\_goodforward  scopePlayer  scopescoperightfoot  @playing\_for\_top\_team  scopescopewhere'team\_name IN (?)'TOP\_TEAMS  scopescopewhere'team\_name IN (?)'TOP\_TEAMS  @with\_great\_accuracy  scopescopewhere'goals / shoots > ?'SHOOT\_ACCURACY  scopescopewhere'goals / shoots > ?'SHOOT\_ACCURACY  @with\_young\_age  scopescopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE  scopescopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE  scope |

I don't think this is necessarily bad. We can refactor it using the Extract Method [1](http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/#easy-footnote-bottom-1) or we can possibly creates scopes in the `Player` model to handle the different queries.

Here I'd like to present an alternative which relies on a flavour of the Query Object design pattern [2](http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/#easy-footnote-bottom-2) [3](http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/#easy-footnote-bottom-3).

# Refactoring

The key idea is to isolate the queries in a separate object without polluting the active record model with scopes. This is because queries like `young`, `with great shoot accuracy` or `playing for a top team` only makes sense when performing the task of talent hunting so it seems natural to keep them separate.

I am a great fan of the decorator pattern [4](http://www.alfredo.motta.name/how-to-isolate-complex-queries-in-an-object-oriented-fashion/#easy-footnote-bottom-4) to enrich objects functionality for a specific use case. For talent hunting we are looking for some sort of definition of `InterestingPlayer`, that behaves like a `Player` but have some extra scopes to make our querying life easier. Here is an attempt:

|  |  |
| --- | --- |
|  | classInterestingPlayer  TOP\_TEAMS'ac milan''real madrid''barcelona'  SHOOT\_ACCURACY  MAX\_AGE  attr\_readerscope  initializescopePlayer  @scopescope  playing\_for\_bigteam  class@scopewhere'team\_name IN (?)'TOP\_TEAMS  not\_playing\_for\_bigteam  class@scopewhere'team\_name IN (?)'TOP\_TEAMS  with\_great\_shootaccuracy  class@scopewhere'goals / shoots > ?'SHOOT\_ACCURACY  without\_great\_shootaccuracy  class@scopewhere'goals / shoots > ?'SHOOT\_ACCURACY  young  class@scopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE  class@scopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE  method\_missingmethod&block  result@scopemethod&block  is\_a\_relationresultclassresultresult  respond\_tomethodinclude\_privatefalse  super@scoperespond\_tomethodinclude\_private  private  is\_a\_relation  instance\_ofrelation\_classname  relation\_classname  "#{@scope.name}::ActiveRecord\_Relation"constantize |

We can split the methods of this object in two sets. The first set of methods is enriching the `Player` active record model with domain specific queries related to the task of talent hunting. When you call one of the domain specific queries  an object of type `InterestingPlayer` is built and returned immediately, like here:

|  |  |
| --- | --- |
|  | playing\_for\_bigteam  class@scopewhere'team\_name IN (?)'TOP\_TEAMS  not\_playing\_for\_bigteam  class@scopewhere'team\_name IN (?)'TOP\_TEAMS  with\_great\_shootaccuracy  class@scopewhere'goals / shoots > ?'SHOOT\_ACCURACY  without\_great\_shootaccuracy  class@scopewhere'goals / shoots > ?'SHOOT\_ACCURACY  young  class@scopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE  class@scopewhere'YEAR(?) - YEAR(birth\_date) < ?'todayMAX\_AGE |

The second set of methods is slightly more complicated and it is the one dealing with the delegation. When `InterestingPlayer` receives a method call that does not match with any of its public methods we delegate the call to the underlying scope. At this point couple of things could happen:

- The result is a relation again. In this case we just want to return another instance of `InterestingPlayer` to let the user compose his query further.
- The result is not a relation, and so the query object have finished his work and we just want to return the result.

This is how this how it could be implemented:

|  |  |
| --- | --- |
|  | method\_missingmethod&block  result@scopemethod&block  is\_a\_relationresultclassresultresult  respond\_tomethodinclude\_privatefalse  super@scoperespond\_tomethodinclude\_private  private  is\_a\_relation  instance\_ofrelation\_classname  relation\_classname  "#{@scope.name}::ActiveRecord\_Relation"constantize |

Finally, let's have a look at how a `TalentHunter` use this query object:

|  |  |
| --- | --- |
|  | classTalentHunterWithQueryObject  initializeoptions  @playing\_for\_top\_teamoptionsfetchplaying\_for\_top\_team  @with\_young\_ageoptionsfetchwith\_young\_age  @with\_great\_accuracyoptionsfetchwith\_great\_accuracy  find\_goodforward  searchInterestingPlayer  searchsearchrightfoot  search@playing\_for\_top\_teamsearchplaying\_for\_big\_teamsearchnot\_playing\_for\_bigteam  search@with\_great\_accuracysearchwith\_great\_shoot\_accuracysearchwithout\_great\_shootaccuracy  search@with\_young\_agesearchyoungsearch  search |

I think this enabled two major results:

- We extracted the domain specific queries into the `InterestingPlayer` object, effectively enabling reuse without polluting the general purpose active record model.
- We made the `find_good_forward` method a bit easier to read because it now only uses domain terms instead of having to translated them into db queries.

# Conclusions

We have seen how to decorate a simple active record model (`Player`) to extract queries related to a specific task into a separate object (`InterestingPlayer`). As a result we simplified the object responsible to build the query and arguably it is now easier to read and comprehend (`TalentHunter`). Code and tests are available on [Github](https://github.com/mottalrd/complex-queries-in-oop).

I'd love to hear your opinion on the comments, or just [tweet me](https://twitter.com/mottalrd) your opinion!

# References

---

*Also published on [Medium](https://medium.com/@motta.lrd/facd9dc8cb7).*
