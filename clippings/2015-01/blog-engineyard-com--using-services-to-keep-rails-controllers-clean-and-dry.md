---
url: "https://blog.engineyard.com/2014/keeping-your-rails-controllers-dry-with-services"
captured_at: "2015-01-28T09:30:54-03:00"
title: "Using Services to Keep Your Rails Controllers Clean and DRY"
domain: "blog-engineyard-com"
---

# Using Services to Keep Your Rails Controllers Clean and DRY

![7cf3c959854b757935fc2f320a4a0847.png](blog-engineyard-com--using-services-to-keep-rails-controllers-clean-and-dry/7cf3c959854b757935fc2f320a4a0847.png)

We've heard it again and again, like a nagging schoolmaster: keep your Rails controllers skinny. Yeah, yeah, we know. But easier said than done, sometimes. Things get complex. We need to talk to some other parts of our codebase or to external APIs to get the job done. Mailers. Stripe. External APIs. All that code starts to add up.

## Ah Tss Push It...Push It Down the Stack

If we ask: "where, pray tell, should this code live?", the answer comes like a resounding chorus: "push it down to the model layer!"

But what if we want to keep our models simple? They should actually reflect the business objects related to our app, according to [Domain Driven Design](http://quickleft.com/blog/engineering-lunch-series-building-complex-domains-in-rails) and other approaches.

Time to get custom!

Crack open the old `app` folder. What do you see? The usual fare? Guess what? Just because Rails comes with six folders doesn't mean we're restricted to six types of object. Let's make some new folders!

## At Your Service

I like to create various kinds of service objects in my Rails app. Tom Pewiński's [recent article](https://netguru.co/blog/service-objects-in-rails-will-help) in [Ruby Weekly](http://rubyweekly.com/) does a great job of covering how to write service objects that help complete an action, like `create_invoice` or `register_user`. While he puts all of his service objects into a single `services` folder, I like to get a little more granular. I'll typically create an `actions` folder for things like `create_invoice`, and folders for other service objects such as `decorators`, `policies`, and `support`. I also use a `services` folder, but I reserve it for service objects that talk to *external* entities, like Stripe, AWS, or geolocation services.

Here's how the app folder might look with all of these subfolders in it:

```
app
|- actions
|- assets
|- controllers
|- decorators
|- models
|- policies
|- services
|- support
|- views
```

## Earning Our Stripes

Let's give it a try, right now! We'll make a credit card service that uses the [Stripe](https://stripe.com/) gem.

We'll create an `app/services` folder and touch a `credit_card_service.rb` inside of it. It's going to be a Plain Old Ruby Object™ (PORO).

It's probably a good idea to wrap the calls to the Stripe gem in local methods like `external_customer_service` and `external_charge_service`, in case we ever want to switch over to Braintree or something else. On object initialization, we'll use dependency injection to accept charge amounts, card tokens, and emails. Our service will expose `charge!` and `create_customer!` methods to hook our controllers into.

```
# app/services/credit_card_service.rb

require 'stripe'

classCreditCardService
  initializeparams
    @card  params:card
    @amount  params:amount
    @email  params:email
  

  charge
    begin
      # This will return a Stripe::Charge object
      external_charge_servicecreatecharge_attributes
    rescue
      false
    
  

  create_customer
    begin
      # This will return a Stripe::Customer object
      external_customer_servicecreatecustomer_attributes
    rescue
      false
    
  

  private

  attr_reader :card :amount :email

  external_charge_service
    StripeCharge
  

  external_customer_service
    StripeCustomer
  

  charge_attributes
    
      amount amount
       
    
  

  customer_attributes
    
      email email
```

## Hook it Up

Now we can write some clean, easily maintainable controller code. We keep the registration logic private, and if we ever want to change it, the controller doesn't have to know anything about it.

```
# app/controllers/users_controller.rb

classUsersControllerActionController
  create
    @user  createuser_params

    registration  register_with_credit_card_service
     registration
      # Save the id from the Stripe::Customer object
      add_customer_id_to_userregistration
      
    
      
    
  

  private

  

  register_with_credit_card_service
    CreditCardService
       params:stripe_token
      email params:user:email
    create_customer
  

  add_customer_id_to_user
    @userupdate_attributesexternal_customer_id
```

## Test It Out

Since we're just using a PORO, this should be nice and easy to test. Let's make a `test/services` folder. If you want to add its contents to your rake tasks, [try this](http://stackoverflow.com/questions/18894060/rails-and-minitest-add-additional-folder). Let's assume that we already have a `test_helper.rb` that includes the Rails helpers in ActiveSupport::TestCase and [mocha](https://github.com/freerange/mocha).

```
# test/services/credit_card_service_test.rb

require 'test_helper'

classCreditCardServiceTestActiveSupportTestCase
   'it creates charges' 
    params  
      amount 
       'TOKEN'
    
    StripeChargeexpects:createparamsreturns
    # This will return false if it fails
    charge  CreditCardServiceparamscharge
    assert charge
  

   'it creates customers' 
    params  
      email 'test@example.card'
       'TOKEN'
    
    StripeCustomerexpects:createparamsreturns
    # This will return false if it fails
    customer  CreditCardServiceparamscreate_customer
    assert customer
```

## Keep It Clean

The last thing you want in your Rails app is a bunch of complicated controllers that are hard to change. Though it may sound pedantic, those voices chanting "Skinny Controller, Fat Model" are right. It's easy to get caught in the trap of answering "where should I put this code" with "let's open the `app` folder and see what cubbies I was given". Don't be afraid to take your Rails project by the horns! You can create your own actions, decorators, support objects, and services. Start including these patterns in your Rails app, and your code will come out clean and DRY: so fresh, so clean!

#### About Ben Lewis

Ben, a Colorado native and a third-generation programmer, lived many lives before following the footsteps of his forebears. After several years as an organic farm worker, gardener, and elementary school music teacher, he fell in love with coding one spring break and never looked back. A graduate of the second gSchool class, he prides himself in a dedication to Test-Driven Development, and specializes in Single Page Apps and Service-Oriented Architecture. He lives in Boulder with his partner Monica and their daughter Lumin, and enjoys cooking, gardening, hiking, and riding his bike. He continues to pursue music as a regional bluegrass fiddle performer. Ben tweets as [@fluxusfrequency](http://twitter.com/fluxusfrequency) and works for [Quick Left](http://quickleft.com/).
