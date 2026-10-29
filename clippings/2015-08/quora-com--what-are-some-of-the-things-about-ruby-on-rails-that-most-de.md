---
url: "http://www.quora.com/What-are-some-of-the-things-about-Ruby-on-Rails-that-most-developers-dont-know"
captured_at: "2015-08-09T17:43:18-03:00"
title: "(1) What are some of the things about Ruby on Rails that most developers don't know? - Quora"
domain: "quora-com"
---

# What are some of the things about Ruby on Rails that most developers don't know?

Ask to Answer

**ActiveRecord::Relation#to\_sql**  
Most

```
ActiveRecord
```

methods return an

```
ActiveRecord::Relation
```

instance.  There's an

```
ActiveRecord::Relation#to_sql
```

method which returns the underlying SQL.  
  
See: [http://api.rubyonrails.org/class...](http://api.rubyonrails.org/classes/ActiveRecord/ConnectionAdapters/DatabaseStatements.html#method-i-to_sql)  
  
Try this:

```
User.where(:first_name => 'Jim').order(:created_at).to_sql
```

This returns the string

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` SELECT "users" ```  ``` "users" ```  ``` WHERE "users""first_name" 'Jim' ```  ``` ORDER BY created_at ``` |

**Associations and the Law of Demeter**  
Sometimes you'll have two [ActiveRecord](http://www.quora.com/ActiveRecord) models and want to define an association in one that returns a subset of elements from the other.  Until recently I didn't know how to do this without one class hard-coding parts of the the other class's schema in a

```
has_many
```

declaration.  
  
For example, perhaps we have users and posts:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` class ActiveRecord:Base ```  ``` has_many :posts ```  ``` class ActiveRecord:Base ```  ``` belongs_to :user ```  ``` published ```  ``` where:published => ``` |

We want to define a

```
User#published_posts
```

method which returns all *published* posts authored by a particular user because, e.g., this is all that will be displayed on an author's profile page.  We could do this

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` class ActiveRecord:Base ```  ``` has_many :posts ```  ``` published_posts ```  ``` postspublished ``` |

The problem, though, is that we can't take advantage of association-specific features like eager loading.  So, most of the time we see folks recommending this

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` class ActiveRecord:Base ```  ``` has_many :posts ```  ``` has_many :published_posts ```  ``` :class_name => 'Post' ```  ``` :where => :published => ``` |

Now, this sucks.  It's a violation of the [Law of Demeter](http://en.wikipedia.org/wiki/Law_of_Demeter) -- the class knows all about the internals of the class, down to the schema level.  As a result we're also repeating ourselves and writing

```
:published => true
```

twice.  
  
But check this:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` class ActiveRecord:Base ```  ``` has_many :posts ```  ``` has_many :published_posts ```  ``` :class_name => 'Post' ```  ``` :where => publishedwhere_values_hash ``` |

Boom.  Beautiful.  No repetition.  The class is asking the class for the proper SQL conditions rather than assuming it knows best.  The [Law of Demeter](http://en.wikipedia.org/wiki/Law_of_Demeter) is upheld.  All is well in the world.
