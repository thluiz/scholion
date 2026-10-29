---
url: "http://www.leanpanda.com/blog/2015/08/24/machine-learning-automatic-classification/"
captured_at: "2015-08-25T10:43:35-03:00"
title: "Machine Learning made simple with Ruby"
domain: "leanpanda-com"
---

# Machine Learning made simple with Ruby

How is it possible to make automatic classification work properly without resorting to using external prediction services? Starting with Bayesian classification, you can use the ruby gem classifier-reborn to create a *Latent Semantic Indexer*. Hands on!

Estimate reading 8 minutes

At the moment, I’m working on a personal project that lets users insert announcements by adding links to a platform.

A periodically executed task analyses the links and downloads metadata such as titles, descriptions, photos, etc. using the opengraph tag (including the option of using a fallback, in the case of these not being specified).

At this point, the administrator has to be able to assign a category to the announcement and publish it.

## Classifiers

Typically, platform admins of this kind have a lot of stuff to do and — being honest — manually assigning a category to each and every announcement isn’t exactly fun.

So, I asked myself if it would be possible to develop a system that, with adequate training, would be able to automatically suggest an appropriate category for newly inserted content.

Seeing that all of the announcements have to be categorized, the introduction of automatic classifiers won’t make the administrators job any harder, even if it doesn’t work.

I originally decided to use a *bayesian classifier*\_ to achieve my goal, in the end choosing to use the ruby gem [classifier-reborn](https://github.com/jekyll/classifier-reborn). The gem makes use of a range of different classification algorithms and, reading through its documentation, I realized that another of these would be better suited to my case than a Bayesian classifier: a [Latent Semantic Indexer](http://en.wikipedia.org/wiki/Latent_semantic_indexing), to be precise.

## Latent Semantic Indexer

In practice, LSI is based on the principle that words used in a particular context tend to have a similar meaning.

In addition to offering a classification method, the gem also enables the software to work in reverse, making it possible to search for similar texts.
This kind of functionality could prove to be useful in future.

Here’s an example of this functionality, taken from the README:

```
require 'classifier-reborn'
  ClassifierReborn
strings   "This text deals with dogs. Dogs." 
            "This text involves dogs too. Dogs! " 
            "This text revolves around cats. Cats." 
            "This text also involves cats. Cats!" 
            "This text involves birds. Birds.":bird 
strings  add_item first 

search"dog" 
# returns => ["This text deals with dogs. Dogs.", "This text involves dogs too. Dogs! ",
#             "This text also involves cats. Cats!"]

find_relatedstrings 
# returns => ["This text revolves around cats. Cats.", "This text also involves cats. Cats!"]

classify "This text is also about dogs!"
# returns => :dog
```

OK, choice made! Let’s starting writing some code!

### Training

LSI classifiers have to be trained: that is, to be given a method of associating a given text with a particular category. In a system already containing manually classified publications, this training is simple to carry out.

The part of the code relative to the training has to be executed by an asynchronously executed task. Since this process is time-consuming, it is carried out only periodically.

We can define the behaviour of our Command Object using the specs:

```
require 'rails_helper'

describe ClassifyAdvertisements 
  :command  described_classadvertisements training 
  :advertisements  build:advertisement title: 'foo' 
  :training 
    
       title: 'foo baz' category_id:  
    
  
  :classifier  instance_double'ClassifierReborn::LSI' 

  before 
    allowClassifierReborn
       receive
          and_returnclassifier

    allowclassifier
       receive:add_item
  

  describe '#initialize' 
     'takes the advertisements to classify and the training as constructor parameters' 
      command
    

     'trains the classifier with the training advertisements title and category id' 
      command
      expectclassifier have_received:add_item'foo baz' 
    
  

  describe '#classify!' 
    :storer  instance_double'StoreClassifications' 

    before 
      allowStoreClassifications
         receive
            advertisements classifier
            and_returnstorer

        allowstorer
           receive:execute!
    

    before  commandclassify! 

     'classifies the advertisements' 
      expectstorer have_received:execute!
```

The idea is to write a class that accepts as constructions parameters the announcements to be classified and a hash list with `title` keys and `category_id`. The values of these hashes have to be passed to the classifier as part of the training process.

The classification proper will be delegated to a second object, initiated for each announcement to be classified, using the method `#classify`!

At this point, we can only imagine what the interface of this object will look like: it will probably receive the announcements to be classified and the pre-trained classifier.

Let’s put it through its tests:

```
class ClassifyAdvertisements
   initializeadvertisements training
    @advertisements  advertisements
    @training  training

    train_classifier!
  

   classify!
    advertisements  advertisement
      StoreClassificationsadvertisement classifierexecute!
    
  

  private

  attr_reader :advertisements :training

   train_classifier!
    training  
      classifieradd_item:title :category_id
    
  

   classifier
    @classifier  ClassifierReborn
```

Check that everything has gone well:

```
$ bundle exec rspec spec/commands/classify_advertisements_spec.rb
...

Finished in 0.11143 seconds (files took 3.88 seconds to load)
3 examples, 0 failures
```

Perfect! Now we have to implement the object that carries out the classification proper, saving the results in the database and updating the state of the announcement.

### Classification

We already have an idea of the interface; now let’s define the behaviour through the specs:

```
require 'rails_helper'

describe StoreClassifications 
  :command  described_classadvertisement classifier 
  :advertisement  create:advertisement title: 'foo' category:  
  :classifier  instance_double'ClassifierReborn::LSI' 
  :category  create:category 

   'takes and advertisement and a classifier as constructor parameters' 
    command
  

  describe '#execute!' 
    context 'on success' 
      before 
        allowclassifier
           receive:classify
              'foo'
              and_returncategory
      

      before  commandexecute! 

       'updates the advertisement category' 
        expectadvertisementreloadcategory_id category
      

       'updates the status of the advertisement' 
        expectadvertisementreloadclassified? 
      
    

    context 'if the classifier was not trained' 
      before 
        allowclassifier
           receive:classify
              'foo'
              and_raiseVectorZeroVectorError
      

      before  commandexecute! 

       'does not update the advertisement category' 
        expectadvertisementreloadcategory_id 
      

       'does not update the status of the advertisement' 
        expectadvertisementreloadcategory_classified? false
```

And now the code to satisfy the tests:

```
class StoreClassifications
   initializeadvertisement classifier
    @advertisement @classifier  advertisement classifier
  

   execute!
    ActiveRecordtransaction 
      advertisementupdate_attributescategory_id: classified_category_id
      advertisementclassified!
    
  rescue VectorZeroVectorError => 
    Railsloggererror "error classifying advertisement advertisementmessage
  

  private

  attr_reader :advertisement :classifier

   classified_category_id
    @classified_category_id  classifierclassifyadvertisementtitle
```

Let’s check that everything’s OK:

```
$ bundle exec rspec spec/commands/classify_advertisement_spec.rb
.....

Finished in 0.16245 seconds (files took 3.78 seconds to load)
5 examples, 0 failures
```

## Conclusions

Let’s see if it works:

```
 foo_category  Categorycreatename: 'foo'
=> #<Category:0x007fd9737ada10>

 bar_category  Categorycreatename: 'bar'
=> #<Category:0x007fd97770cb48>

 training  Advertisementcreatetitle: 'this is something about foo' category: foo_category Advertisementcreatetitle: 'this is something about bar' category: bar_category
=> #<Advertisement:0x007fd9778e61d0>, #<Advertisement:0x007fd9793aedc8>]

   Advertisementcreatetitle: "an article to be categorized talking about foo" category: 
=> #<Advertisement:0x007fd97a128490>

 ClassifyAdvertisements training   slice :title classify!

 category
=> "foo"
```

I’m satisfied with the results achieved by this implementation, even though there are a few remaining issues to be resolved… for example: the training is currently carried out using all of the published announcements, every time the task is executed. Saving the structure of the classification data once the training is finished and updating when changes are made to published announcements (synchronously or asynchronously) could be a better solution.
