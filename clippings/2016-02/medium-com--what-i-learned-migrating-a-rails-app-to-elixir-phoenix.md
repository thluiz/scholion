---
url: "https://medium.com/@stueccles/what-i-learned-migrating-a-rails-app-to-elixir-phoenix-f707436749aa"
captured_at: "2016-02-07T20:33:02-03:00"
title: "What I learned migrating a Rails app to Elixir/Phoenix — Medium"
domain: "medium-com"
---

# What I learned migrating a Rails app to Elixir/Phoenix

I’ve been keen on Elixir for a while now. For us at Made by Many the promise of the productivity of Ruby without compromising on raw performance and scalability is rapidly making it a prime candidate for our go-to server-side language of choice.

To overcome the Elixir learning curve I’ve done a few things including reading and working the exercises in the excellent Dave Thomas book and attending Elixir Conf in Austin. The other thing has been to being to migrate [a colleague’s](http://twitter.com/cjbell_) Rails app to Phoenix.

The app is a non-trivial e-Commerce application that runs his excellent high-end sock business at [Form &Thread](https://formandthread.com/). I’ve documented some initial gotchas and interesting things from the migration. If you are migrating a Rails app your mileage may vary and you may have much different issues. Before we get into some details, here are the three high-level insights.

*Note: I’m not going to go into Elixir basics and how to install Phoenix etc. It presumes some knowledge of the language and the Phoenix Framework.*

**1 Lose the Object Orientated mindset, especially around models.**

This is the biggest mental transition to go through when you are used to Ruby programming. Especially where the mind-set of “thin controllers, fat models” is baked into Rails programmers which has created many obese models, even if they are using decorator/presenter patterns or service objects.

Instead you are thinking in small functions that you string together. Once you make the transition I’ve found it is actually easier to understand what is going on. There is just a lot less magic to wrap your head around.

**2 There are some integrations you are going to have to write yourself**

The Elixir ecosystem isn’t developed to a point where there are libraries to integrate with every service you may use. You might have to roll up your sleeves to make that integration library yourself. But this is how we grow the ecosystem. I created a [segment.com library in Elixir](https://github.com/stueccles/analytics-elixir/) for this reason.

There are also far fewer utility extension and helper libraries available for Phoenix but so far I’ve found that language features do a lot to overcome this. Although in the end you should expect to write a little more code.

**3 Some things should just be done completely differently in Elixir/Phoenix**

There are some software design patterns you just should do differently when creating an Elixir app. For instance when you think asynchronous, the general Rails pattern is to think message queue and a worker in a background process such as [Sidekiq](http://sidekiq.org/)/[DelayedJob](https://github.com/collectiveidea/delayed_job) etc. This is totally unnecessary in Elixir which is designed for concurrency. Typically you can just wrap a function in a *Task.async* or create your own OTP application.

> “There is just a lot less magic to wrap your head around.”

#### **Migrating the front end build pipeline to brunch**

First step after setting up a new phoenix application was to migrate the front end build pipeline from the Rails pipeline to the Phoenix front-end build of choice [*Brunch*](http://brunch.io/)*.*

The first problem was the Rails pipeline handles SASS by default while Brunch does not. But SASS can be easily added with the [sass-brunch module](https://github.com/brunch/sass-brunch). I added this to the *package.json* along with some other node modules we needed.

```
"sass-brunch": "^1.8.10",  
"bourbon": "^4.2.6",  
"css-patterns": "^0.2.0",  
"normalize.css": "^3.0.3"
```

Some modifications were required to *brunch.config* to configure sass-brunch to include the *node\_modules* directory for sass to add [bourbon](http://bourbon.io/), normalize and the Made by Many [css-patterns](https://github.com/madebymany/css-patterns).

```
plugins: {  
  babel: {  
    // Do not use ES6 compiler in vendor code  
    ignore: [/web\/static\/vendor/]  
  },  
  sass: {  
    options: {  
      includePaths: [ ‘node_modules’ ]  
    }  
  }  
}
```

And then imported to the top of the *application.scss* with paths relative to the *node\_modules* directory.

```
@import “bourbon/app/assets/stylesheets/bourbon”;  
@import “normalize.css/normalize.css”;  
@import “css-patterns/stylesheets/patterns”;
```

A little directory restructure is required to move the *js* and *css* out of the *assets* directory to *web/static*. While the *images* and *fonts* directory go in *web/static/assets.*

The other major front-end change was is there is no [*sass-rails*](https://github.com/rails/sass-rails) gem magically providing you *asset\_path* or *asset\_url*. These all need removing and specific paths added.

```
url(asset-path(‘Apercu Bold-webfont.eot’));
```

```
..becomes..
```

```
url(‘/fonts/Apercu Bold-webfont.eot’);
```

#### ActiveRecord to Ecto Model Migration

*Note: although Phoenix still calls them models, Ecto has moved to a Schema terminology and I expect Phoenix to do the same. It helps a lot to* ***not*** *think of them as models;**gets you out of the OO mindset. For now i’m going to refer to them in Phoenix as models.*

This was a relatively simple task of taking the *schema.rb* and creating the necessary migrations and model files in Phoenix with the [*mix phoenix.gen.model*](http://www.phoenixframework.org/docs/mix-tasks) *t*asks . There were exceptions I ran into, your mileage may vary.

1. No *has\_and\_belongs\_to\_many* functionality in Ecto may mean you need to create your own join model which would be unnecessary in Rails. You can then use *has\_many :through* to create a similar structure
2. No working HSTORE implementation in Ecto

The existing data model used Postgres HSTORE to store key-value information on some models. At the moment Ecto doesn’t support HSTORE and making it would have taken too long. Instead I migrated the data to *jsonb* which has a internal Elixir Map representation, see [<https://robots.thoughtbot.com/embedding-elixir-structs-in-ecto-models>]

One gotcha though to using JSONB is ensuring the JSON extension is in the config for the environment:

```
config :form_and_thread, FormAndThread.Repo,  
 adapter: Ecto.Adapters.Postgres,  
 extensions: [{Postgrex.Extensions.JSON, [library: nil]}],
```

Migrate any seed data with your Ecto Elixir code in *priv/repo/seeds.exs* which you can run it by invoking:

```
mix run priv/repo/seeds.exs
```

#### Using the models

Ecto is not ActiveRecord. There are going to be some things you will need to change up. Here are two of them I ran into:

**No Scope**

Ecto doesn’t use scopes. Instead we use a pattern of storing queries in the module and then composing them when needed, see <http://blog.drewolson.org/composable-queries-ecto/>

```
class Order < ActiveRecord::Base
```

```
  scope :received_or_shipped, -> { where(state: [‘received’, ‘shipped’]) }
```

```
..becomes..
```

```
defmodule FormAndThread.Order do
```

```
  def received_or_shipped_query(query) do  
    from o in query,  
    where: o.state == 'received' or o.state == 'shipped'  
  end  
end
```

```
Order |> Order.received_or_shipped_query |> Repo.all
```

**No Lazy loading associations**

ActiveRecord will lazy load you associations when you come to access them. However with Ecto you’ll need to use Repo.preload or it will throw an error. We use a pattern for storing the relations we want commonly preloaded in a method that can be passed to the Repo.preload method (note that we can do deeply nested preloads here).

```
defmodule FormAndThread.Order do
```

```
  def preloaded do  
   [:shipping_address, line_items: [variant: [:product]]]   
  end  
end
```

```
order = get_current_order(conn) |> Repo.preload(Order.preloaded)
```

**Embrace the changeset instead of model callbacks**

The changeset pattern is how you are going to make changes to your models in your new immutable world and you should use different type of changesets for updates rather than rely on model callbacks.

```
before_create :set_default_shipping_country, :set_random_number
```

```
..becomes..
```

```
def create_changeset(model, params \\ :empty) do  
  changeset(model, params)  
  |> put_change(:number, random_unique_order_number)  
  |> put_change(:shipping_country, @default_shipping_country)  
end
```

> “Ecto is not ActiveRecord”

#### Controller migration

The controller structure follows a very similar pattern from Rails to Phoenix. In fact I won’t even go into routes because it is so similar. Let’s look at some of the things we did have to change up.

The Rails app I was migrating from used a lot of *before\_action* in controllers to fetch data. These could have been converted to plugs in Phoenix but instead I used a pattern of pipelining through different functions inside the action method. It then becomes very clean and easy to see what happens in each render pipeline:

```
before_action :fetch_product, only: [:show]
```

```
def fetch_product  
  @product = Product.includes(:variants).find_by(slug: params[:id])  
end
```

```
..becomes..
```

```
def show(conn, %{“id” => id}) do  
  conn  
   |> assign_current_order  
   |> assign_product(id)  
   |> render(“show.html”)  
end
```

```
defp assign_product(conn, id) do  
  assign(conn, :product, Repo.get!(Product, id, preload [:variants]))  
end
```

And in some cases used the plug to check for requirements before the action method.

```
before_action :check_for_order, only: [:show, :update]  
  
def check_for_order  
  redirect_to root_path unless current_order.present?  
end
```

```
becomes
```

```
plug :check_for_order
```

```
defp check_for_order(conn, _params) do  
  case get_current_order(conn) do  
    nil ->  
      conn |> redirect(to: “/”) |> halt  
    order ->  
      assign(conn, :order, order)  
   end  
end
```

#### Templates/Views

There is a little nomenclature change here. What Rails will call a view is actual a template in Phoenix. The template file is actually compiled to a function within a View module. The Phoenix Views are also where we would put the helper functions normally found in Rails helpers. A simple example for calculating the total amount of a line item to display.

```
def line_item_amount(line_item) do  
  Decimal.mult(line_item.price, Decimal.new(line_item.quantity))  
end
```

Only explicitly assigned variables can be accessed in the view, unlike Rails which allows all instance variables to be accessed by default. The Rails app I was migrating also used Decorators using the draper gem to enhance models. Instead we move these to functions in the View

```
<% product.imagery.each_with_index do |image, index| %>
```

```
..becomes..
```

```
<%= for {img, index} <- Enum.with_index(product_images(@product)) do %>
```

```
product_images is a function in FormAndThread.ProductView
```

#### Services

The other main component of the application was actually the services that ran through the main business logic of the core actions. For these I created Elixir modules to contain the functionality.

The great thing about Elixir is how simple we can make an easy to understand flow of actions. With a pattern that every action that mutates the underlying order record in the database returns its new state before being passed to the next action.

```
defmodule FormAndThread.Checkout do  
...
```

```
def complete(changeset) do  
  changeset  
  |> Repo.update!  
  |> Repo.preload(Order.preloaded)  
  |> charge_customer  
  |> deliver_confirmation_email  
  |> reconcile_stock_levels  
  |> mark_as_received  
end
```

```
def charge_customer(order) do  
 Gateway.charge_customer(order)  
end
```

```
def deliver_confirmation_email(order) do  
  Mailer.send_order_received_email(order)  
end
```

```
def reconcile_stock_levels(order) do  
  Repo.transaction(fn ->  
    for li <- order.line_items do  
      Repo.update!(%{li.variant | stock_level: li.variant.stock_level — li.quantity})  
    end  
  end)  
  order  
end
```

```
def mark_as_received(order) do  
  Order.changeset(order, %{state: “received”, completed_at:    Ecto.DateTime.local()})  
  |> Repo.update!  
end
```

#### Summary

So i’m sure there will be many more transition patterns that are useful in migrating a Rails app but so far I’ve found the process not only pretty painless but also feels vastly superior. Not to mention just how much faster the Elixir app is; response times under 100ms bring joy to the heart.
