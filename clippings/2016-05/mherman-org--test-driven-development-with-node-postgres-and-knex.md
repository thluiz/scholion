---
url: "http://mherman.org/blog/2016/04/28/test-driven-development-with-node"
captured_at: "2016-05-09T13:53:08-03:00"
title: "Test Driven Development With Node, Postgres, and Knex (Red/Green/Refactor) - Michael Herman"
domain: "mherman-org"
---

# Test Driven Development With Node, Postgres, and Knex (Red/Green/Refactor)

**Today we will be developing a RESTful API with [Node](https://nodejs.org/), [Express](http://expressjs.com/), [Knex](http://knexjs.org/) - a SQL query builder - and [PostgreSQL](http://www.postgresql.org/) using test driven development (TDD).**

This post assumes prior knowledge of:

- Node/Express
- NPM Packages

## Getting Started

Before we can start testing and writing code we need to set up our project, a database, and all the required dependencies…

### Project Setup

First, we need to create a basic boilerplate Express application. To do this, first install the [Express-Generator](http://expressjs.com/en/starter/generator.html) globally:

|  |  |
| --- | --- |
|  | ``` npm install express-generator@4.13.1 -g ``` |

We can now generate a basic Express application boilerplate:

|  |  |
| --- | --- |
|  | ``` express mocha-chai-knex mocha-chai-knex npm install ``` |

Run `npm start` to ensure the application works. Once the server is running, navigate to <http://localhost:3000/>, and you should see ‘Welcome to Express’ on the main page.

### Database Setup

Start by installing [PostgreSQL](http://www.postgresql.org/) from the official [download page](http://www.postgresql.org/download/).

> If you’re on a Mac we recommend using [Postgress.app](http://postgresapp.com/).

As noted, we’ll be using [Knex](http://knexjs.org/) to interact with our database. Knex is a SQL query builder that we can use with PostgreSQL to handle migrations, manage the schema, and query the database.

Let’s start by installing [Knex](http://knexjs.org/) and [pg](https://github.com/brianc/node-postgres), a module for interacting with Postgres.

|  |  |
| --- | --- |
|  | ``` npm install pg@4.5.3 knex@0.10.0 --save npm install knex@0.10.0 -g ``` |

Next, we need to create two new databases, one for developing and the other for testing. Open [psql](http://www.postgresql.org/docs/9.5/static/app-psql.html) in the terminal, and create a new database:

|  |  |
| --- | --- |
|  | ``` psql 9.4.5 Type "help"  help. # CREATE DATABASE mocha_chai_tv_shows; CREATE DATABASE # CREATE DATABASE mocha_chai_tv_shows_test; CREATE DATABASE ``` |

With out database created we can initialize Knex.

### Knex Setup

Run the following command to create *knexfile.js*, the [Knex configuration file](http://knexjs.org/#knexfile):

|  |  |
| --- | --- |
|  | ``` knex init Created ./knexfile.js ``` |

Update the default info to:

|  |  |
| --- | --- |
|  | ``` moduleexports       client      connection 'postgres://localhost/mocha_chai_tv_shows_test'     migrations        directory __dirname  '/db/migrations'     seeds        directory __dirname  '/db/seeds/test'   development      client      connection 'postgres://localhost/mocha_chai_tv_shows'     migrations        directory __dirname  '/db/migrations'     seeds        directory __dirname  '/db/seeds/development'   production      client      connection processDATABASE_URL     migrations        directory __dirname  '/db/migrations'     seeds        directory __dirname  '/db/seeds/production' ``` |

This sets up three different settings for our databases:

1. `test` - for testing on the local environment
2. `development` - for developing, again on the local environment
3. `production` - for the production environment

Now, we can add schema migrations. [Migrations](https://en.wikipedia.org/wiki/Schema_migration) allow us to define and update the database schema. We can create migrations in the terminal like so:

|  |  |
| --- | --- |
|  | ``` knex migrate:make tv_shows ``` |

Now, knex has automatically added in a “db/migrations” folder, with a timestamped file inside of it. Here is where we define our schema. It should just contain two empty functions at the moment.

Let’s add in our code to create and drop tables.

|  |  |
| --- | --- |
|  | ``` exports  function Promise    return schemacreateTable'shows' functiontable     tableincrements     tablestring'name'notNullableunique     tablestring'channel'notNullable     tablestring'genre'notNullable     tableinteger'rating'notNullable     tableboolean'explicit'notNullable exports  function Promise    return schemadropTable'shows' ``` |

Here, the `up` function creates the `shows` table while the `down` function drops the table. So we now have a schema defined, and a migration file ready to create that schema.

Create a new file called *knex.js* inside the “db” folder. In this file we specify the environment (`test`, `development`, or `production`), require the *knexfile.js*, and export the configuration (based on the environment) for our database:

|  |  |
| --- | --- |
|  | ```  environment  processNODE_ENV  'development'  config  require'../knexfile.js'environment moduleexports  require'knex'config ``` |

Apply the migrations to both databases:

|  |  |
| --- | --- |
|  | ``` knex migrate:latest --env development knex migrate:latest --env ``` |

### Knex Seeds

[Seeding](https://en.wikipedia.org/wiki/Database_seeding) is simply the process of populating the database with initial data. Knex utilizes [seed files](http://knexjs.org/#Seeds-CLI) for this.

Run the following in your terminal to create a seed for development:

|  |  |
| --- | --- |
|  | ``` knex seed:make shows_seed --env development ``` |

This will generate a folder called “seeds/development” in the “db” directory of your project, and in that file there will be a boilerplate setup for inserting data into the database:

|  |  |
| --- | --- |
|  | ``` exports  function Promise    return Promise     // Deletes ALL existing entries     'table_name'     // Inserts seed entries     'table_name'insert  colName 'rowValue'     'table_name'insert  colName 'rowValue2'     'table_name'insert  colName 'rowValue3' ``` |

Let’s change the file so we’re inserting relevant data. Notice how there’s also built-in promises so that the data will be seeded in the order that we specify:

|  |  |
| --- | --- |
|  | ``` exports  function Promise    return 'shows' // Deletes ALL existing entries     function  // Inserts seed entries one by one in series       return 'shows'insert          'Suits'         channel 'USA Network'         genre 'Drama'         rating          explicit false     function         return 'shows'insert          'Game of Thrones'         channel 'HBO'         genre 'Fantasy'         rating          explicit      function         return 'shows'insert          'South Park'         channel 'Comedy Central'         genre 'Comedy'         rating          explicit      function         return 'shows'insert          'Mad Men'         channel 'AMC'         genre 'Drama'         rating          explicit false ``` |

Since JavaScript is asynchronous, the order that data is inserted can sometimes change. We want to make sure that the data is in the same order each time we run our seed file(s).

Run the seed file:

|  |  |
| --- | --- |
|  | ``` knex seed:run --env development ``` |

Before moving on, follow the same process for the test seed. Just use the same data as the development seed.

### Mocha/Chai Setup

With the database set up with data in it, we can start setting up our tests. Start by installing [Mocha](http://mochajs.org/) (test runner) and [Chai](http://chaijs.com/) ([assertion](https://en.wikipedia.org/wiki/Assertion_(software_development)) as well as [ChaiHTTP](https://github.com/chaijs/chai-http) (HTTP request module for integration testing). Make sure to also install mocha globally, so that we can run tests from the command line.

|  |  |
| --- | --- |
|  | ``` npm install mocha@2.4.5 -g npm install mocha@2.4.5 chai@3.5.0 chai-http@2.0.1 --save-dev ``` |

By default, Mocha searches for tests with a “test” folder.

> This configuration can be changed with a [mocha.opts](https://mochajs.org/#mochaopts) file

Add a “test” folder to the root directory, and in that folder add a file called *routes.spec.js*. Then update *routes/index.js*:

|  |  |
| --- | --- |
|  | ```  express  require'express'  router  expressRouter // *** GET all shows *** // router'/shows' function      'send shows back' moduleexports  router ``` |

Then within *app.js* update this line-

|  |  |
| --- | --- |
|  | ```  routes ``` |

|  |  |
| --- | --- |
|  | ``` '/api/v1' routes ``` |

Now every single route in that file will be prefixed with ‘/api/v1’ Try it out. Fire up the server, and navigate to [http://localhost:3000/api/v1shows](http://localhost:3000/api/v1/shows). You should see the string ‘send shows back’ in the browser.

Finally, update this line in *app.js*-

|  |  |
| --- | --- |
|  | ``` logger'dev' ``` |

|  |  |
| --- | --- |
|  | ```  processNODE_ENV  'test'    logger'dev' ``` |

This [prevents](http://stackoverflow.com/a/22710649/1799408) application log messages from displaying in the stdout when the tests are ran, making it much easier to read the output.

And make sure the error handlers return JSON:

|  |  |
| --- | --- |
|  | ``` // error handlers // development error handler // will print stacktrace  'env'  'development'    function         statusstatus         message message       error  // production error handler // no stacktraces leaked to user function       statusstatus       message message     error ``` |

## Developing via TDD

The premise behind Test Driven Development (TDD) is that you write tests first that fail which you then make pass. This process is often referred to as [Red/Green/Refactor](https://github.com/mjhea0/flaskr-tdd#test-driven-development).

### Test Setup

In our test file, we’ll need to start by including the necessary requirements for testing:

|  |  |
| --- | --- |
|  | ``` processNODE_ENV  'test'    require'chai'  should  should  chaiHttp  require'chai-http'  server  require'../app' chaiHttp describe'API Routes' function ``` |

The first line sets the `NODE_ENV` to `test` so that the correct Knex config is used from *knexfile.js*. The next line requires `chai`, the assertion module, giving us access to all the `chai` methods - like `should()`.

> By utilizing `should()` we are using the [should](http://chaijs.com/guide/styles/#should) assertion style. This is a personal preference. You could also use [expect](http://chaijs.com/guide/styles/#expect) or [assert](http://chaijs.com/guide/styles/#assert).

Then we require `chai-http`. This module allows us make http requests from within our test file. Next, we link to our app so that we can test the request-response cycle. Finally, the `describe` block underneath the requirements is the wrapper for the tests. Keep in mind that you can nest `describe` [blocks](http://samwize.com/2014/02/08/a-guide-to-mochas-describe-it-and-setup-hooks/) to better organize your test structure by grouping similar tests together.

### GET all shows

In the first test case, which is nested inside the first `describe` block, we want to get ALL shows in our database:

|  |  |
| --- | --- |
|  | ``` describe'GET /api/v1/shows' function    'should return all shows' function      requestserver     '/api/v1/shows'     function       shouldstatus     should // jshint ignore:line     should'array'     lengthshouldequal     shouldproperty'name'     shouldequal'Suits'     shouldproperty'channel'     channelshouldequal'USA Network'     shouldproperty'genre'     genreshouldequal'Drama'     shouldproperty'rating'     ratingshouldequal     shouldproperty'explicit'     explicitshouldequalfalse ``` |

So, we have a `describe` block, and within that block, we have a single `it` statement. An `it` statement defines a specific test case. Here we hit the route ‘/api/v1/shows’ with a GET request and test that the actual response is the same as the expected response.

Let’s break this test down…

First, by removing the test conditions, we can look at the basic test structure:

|  |  |
| --- | --- |
|  | ``` 'should return all shows' function    requestserver   '/api/v1/shows'   function ``` |

Since this is an asynchronous test, we need some way of telling the callback function that the test is complete. This is where the `done()` callback method comes into play. Once called (or if a two second timer is exceeded), Mocha knows that the test is finished running, and it can move on to the next test.

Now let’s look at the assertions:

|  |  |
| --- | --- |
|  | ``` shouldstatus should // jshint ignore:line should'array' lengthshouldequal shouldproperty'name' shouldequal'Suits' shouldproperty'channel' channelshouldequal'USA Network' shouldproperty'genre' genreshouldequal'Drama' shouldproperty'rating' ratingshouldequal shouldproperty'explicit' explicitshouldequalfalse ``` |

The first thing we generally want to do, is test that the response has a status of 200. After that, these tests will change depending on what we return in the route handler. In this case, we are expecting that the content type is JSON and that the response body will be an array (of objects) and have a length equal to four (since there are four rows in the database). Finally, we are testing the keys and values within the first object of the array.

Try it out:

|  |  |
| --- | --- |
|  | ``` mocha ``` |

If all went well you should see this:

|  |  |
| --- | --- |
|  | ```   API Routes     GET /api/v1/shows       1 should return all shows    passing 59ms    failing   1 API Routes GET /api/v1/shows should return all shows:      Uncaught AssertionError: expected 'text/html; charset=utf-8'      to include 'application/json' ``` |

Essentially, the second assertion - `res.should.be.json;` - failed since we are sending plain text back. This is good! Remember: Red-Green-Refactor!

We just need to update the route to get the test to pass.

#### Green

Before updating the route, let’s create a queries module for handling, well, the database queries. Create a new file called *queries.js* with the “db” folder, and add the following code:

|  |  |
| --- | --- |
|  | ```    require'./knex.js' function Shows    return 'shows' // *** queries *** // function getAll    return Showsselect moduleexports     getAll getAll ``` |

Here, we made a reference to our database via the Knex config file, added a helper function for simplifying each individual query, and finally queried the database to get ALL shows.

Update the route:

|  |  |
| --- | --- |
|  | ```  express  require'express'  router  expressRouter  queries  require'../db/queries' // *** GET all shows *** // router'/shows' function      queriesgetAll   functionshows      statusshows   catchfunctionerror      error moduleexports  router ``` |

Run mocha again and see what happens:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 128ms  passing 164ms ``` |

Awesome! Just don’t forget the last step - refactor.

#### Refactor

What’s happening in the test database?

|  |  |
| --- | --- |
|  | ``` # psql psql 9.4.5 Type "help"  help. # \c mocha_chai_tv_shows_test You are now connected to database "mocha_chai_tv_shows". mocha_chai_tv_shows# SELECT * FROM shows;  id       name           channel       genre   rating  explicit ----+-----------------+----------------+---------+--------+----------     Suits            USA Network     Drama           f     Game of Thrones  HBO             Fantasy         t     South Park       Comedy Central  Comedy          t     Mad Men          AMC             Drama           f ``` |

Since we seeded the database earlier, there’s data already in there, which could affect other tests (especially when rows are added, changed, and/or dropped). In the test, we are asserting that the length of the array is four. Well, if we add an item then that’s going to change the length, and that first test will fail.

Tests should be isolated from each other. So, we really should rollback the migrations before and after each test is ran, and then apply the migrations and re-seed the database before the next test is ran.

This is where `beforeEach` and `afterEach` come into play:

|  |  |
| --- | --- |
|  | ``` processNODE_ENV  'test'    require'chai'  chaiHttp  require'chai-http'  server  require'../app'    require'../db/knex'  should  should chaiHttp describe'API Routes' function    beforeEachfunction      migraterollback     function        migratelatest       function          return          function    afterEachfunction      migraterollback     function    describe'Get all shows' function      'should get all shows' function        requestserver       '/api/v1/shows'       function           shouldstatus         should // jshint ignore:line         should'array'         lengthshouldequal         shouldproperty'name'         shouldequal'Suits'         shouldproperty'channel'         channelshouldequal'USA Network'         shouldproperty'genre'         genreshouldequal'Drama'         shouldproperty'rating'         ratingshouldequal         shouldproperty'explicit'         explicitshouldequalfalse ``` |

Now, the migrations will run and the database will be re-seeded before each nested `describe` block, and the migrations will be rolled back after each block (which will also drop the data).

> Why rollback before each test? If any errors occur during a test, it won’t reach the `afterEach` block. So we want to make sure that if an error occurs we still rollback the database.

Run the tests again:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 52ms  passing 325ms ``` |

1 down, 4 to go!!!

> Did you notice how the overall time is slightly slower? 325ms vs 164ms. This is because of the `beforeEach` and `afterEach`. Think about what’s happening, and why this would slow down the tests.

### GET single show

We have our route and test built to get All shows, so the next step is to just get one show back.

Based on our test seed, the first show that should (you never know for certain with async code) is `Suits`:

|  |  |
| --- | --- |
|  | ```    'Suits'   channel 'USA Network'   genre 'Drama'   rating    explicit false ``` |

We can write out a test for a new route that will return just a single show and the meta information about it. Remember our last test? It returned an array of objects. This time it should be a *single* object since we will be searching for a *single* item in the database.

|  |  |
| --- | --- |
|  | ``` describe'GET /api/v1/shows/:id' function    'should return a single show' function      requestserver     '/api/v1/shows/1'     function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'name'       shouldequal'Suits'       shouldproperty'channel'       channelshouldequal'USA Network'       shouldproperty'genre'       genreshouldequal'Drama'       shouldproperty'rating'       ratingshouldequal       shouldproperty'explicit'       explicitshouldequalfalse ``` |

This is very similar to the previous test. We’re still testing for a status code of 200, and the response should be JSON. This time, we expect that `res.body` is an object. Each of the properties afterwards should be the properties of the item with id ‘1’ in the database. So now if we run the tests, the first assertion should fail because we haven’t written our route yet:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows   GET /api/v1/shows/:id     1 should return a single show  passing 383ms  failing 1 API Routes GET /api/v1/shows/:id should return a single show:    Uncaught AssertionError: expected  Object domain, _events, ...     to have status code  but got 404 ``` |

#### Green

Add the query to *queries.js*, making sure to update `module.exports`:

|  |  |
| --- | --- |
|  | ``` function getSingleshowID    return Showswhere parseIntshowIDfirst moduleexports     getAll getAll   getSingle getSingle ``` |

Then build out the route:

|  |  |
| --- | --- |
|  | ``` // *** GET single show *** // router'/shows/:id' function      queriesgetSingleparams   function      status   catchfunctionerror      error ``` |

Now run mocha, and let’s see if that worked:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 54ms   GET /api/v1/shows/:id     ✓ should return a single show  passing 499ms ``` |

Two routes down, two tests passing.

We now want to add an item to our database.

For time’s sake, write the test assuming you will get a JSON object back that contains the data added to the database:

|  |  |
| --- | --- |
|  | ``` describe'POST /api/v1/shows' function    'should add a show' function      requestserver     '/api/v1/shows'        'Family Guy'       channel  'Fox'       genre 'Comedy'       rating        explicit      function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'name'       shouldequal'Family Guy'       shouldproperty'channel'       channelshouldequal'Fox'       shouldproperty'genre'       genreshouldequal'Comedy'       shouldproperty'rating'       ratingshouldequal       shouldproperty'explicit'       explicitshouldequal ``` |

You can see here that our test block is slightly different than the previous two since we need to send information with the request to replicate how a client might send information to the server.

#### Green

With the test written and failing (did you remember to run the tests?), we can write the query and add the route (notice the pattern yet?).

Query:

|  |  |
| --- | --- |
|  | ``` function     return Showsinsert ``` |

Route:

|  |  |
| --- | --- |
|  | ``` // *** add show *** // router'/shows' function      queries   functionshowID      queriesgetSingleshowID     function        status     catchfunctionerror        error   catchfunctionerror      error ``` |

`.insert()` returns an array containing the unique ID of the newly added item, so in order to return the actual data, we utilized the `getSingle()` query. This also ensures that the data has been inserted into the database correctly.

Do the tests pass?

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 50ms   GET /api/v1/shows/:id     ✓ should return a single show   POST /api/v1/shows     ✓ should add a show 71ms  passing 791ms ``` |

Excellent. Just two routes left to go.

We need to test the edit route.

Similar to our POST route we will need to send data to the server. In this case, we’ll utilize the ID of an existing show in the database and send along an object with the updated fields. Then we’ll assert that the show has been updated correctly.

|  |  |
| --- | --- |
|  | ``` describe'PUT /api/v1/shows/:id' function    'should update a show' function      requestserver     '/api/v1/shows/1'       rating        explicit      function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'name'       shouldequal'Suits'       shouldproperty'channel'       channelshouldequal'USA Network'       shouldproperty'genre'       genreshouldequal'Drama'       shouldproperty'rating'       ratingshouldequal       shouldproperty'explicit'       explicitshouldequal ``` |

So here we are stating that the response body should contain the updated object from the database.

#### Green

You know the drill - Start with the query:

|  |  |
| --- | --- |
|  | ``` function updateshowID updates    return Showswhere parseIntshowIDupdateupdates ``` |

Then update the route:

|  |  |
| --- | --- |
|  | ``` // *** update show *** // router'/shows/:id' function      queriesupdateparams    function      queriesgetSingleparams     function        status     catchfunctionerror        error   catchfunctionerror      error ``` |

Here, we again make two calls to the database. Once we’ve updated the item, we then nest another query to get that same item - which we then check to ensure that it has in fact been updated correctly.

The tests should pass.

#### Refactor

What happens if we try to change the ID? Update the test:

|  |  |
| --- | --- |
|  | ``` describe'PUT /api/v1/shows/:id' function    'should update a show' function      requestserver     '/api/v1/shows/1'       rating        explicit      function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'name'       shouldequal'Suits'       shouldproperty'channel'       channelshouldequal'USA Network'       shouldproperty'genre'       genreshouldequal'Drama'       shouldproperty'rating'       ratingshouldequal       shouldproperty'explicit'       explicitshouldequal ``` |

Run the tests now and they should fail:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 43ms   GET /api/v1/shows/:id     ✓ should return a single show   POST /api/v1/shows     ✓ should add a show 50ms   PUT /api/v1/shows/:id     1 should update a show  passing 804ms  failing 1 API Routes PUT /api/v1/shows/:id should update a show:    Uncaught AssertionError: expected  to be an object ``` |

Why? Because the updated ID of the test does not equal the ID passed in as a query parameter. What does this all mean? The unique ID should never change (unless it’s removed altogether).

|  |  |
| --- | --- |
|  | ``` // *** update show *** // router'/shows/:id' function      hasOwnProperty      return status       error 'You cannot update the id field'   queriesupdateparams    function      queriesgetSingleparams     function        status     catchfunctionerror        error   catchfunctionerror      error ``` |

Now, let’s revert the changes in the test, by removing `id: 20,`, and add a new test:

|  |  |
| --- | --- |
|  | ``` describe'PUT /api/v1/shows/:id' function    'should update a show' function      requestserver     '/api/v1/shows/1'       rating        explicit      function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'name'       shouldequal'Suits'       shouldproperty'channel'       channelshouldequal'USA Network'       shouldproperty'genre'       genreshouldequal'Drama'       shouldproperty'rating'       ratingshouldequal       shouldproperty'explicit'       explicitshouldequal   'should NOT update a show if the id field is part of the request' function      requestserver     '/api/v1/shows/1'       rating        explicit      function         shouldstatus       should // jshint ignore:line       should'object'       shouldproperty'error'       errorshouldequal'You cannot update the id field' ``` |

Run the tests:

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 49ms   GET /api/v1/shows/:id     ✓ should return a single show   POST /api/v1/shows     ✓ should add a show 51ms   PUT /api/v1/shows/:id     ✓ should update a show     ✓ should NOT update a show  the id field is part of the request ``` |

Boom!

### DELETE

Now on to the final test - the delete.

Again, let’s use the ID of the first item in our database as the starting point for the test:

|  |  |
| --- | --- |
|  | ``` describe'DELETE /api/v1/shows/:id' function    'should delete a show' function      requestserver     delete'/api/v1/shows/1'     functionerror response        responseshouldstatus       responseshould // jshint ignore:line       responseshould'object'       responseshouldproperty'name'       responseshouldequal'Suits'       responseshouldproperty'channel'       responsechannelshouldequal'USA Network'       responseshouldproperty'genre'       responsegenreshouldequal'Drama'       responseshouldproperty'rating'       responseratingshouldequal       responseshouldproperty'explicit'       responseexplicitshouldequalfalse       requestserver       '/api/v1/shows'       function           shouldstatus         should // jshint ignore:line         should'array'         lengthshouldequal         shouldproperty'name'         shouldequal'Game of Thrones'         shouldproperty'channel'         channelshouldequal'HBO'         shouldproperty'genre'         genreshouldequal'Fantasy'         shouldproperty'rating'         ratingshouldequal         shouldproperty'explicit'         explicitshouldequal ``` |

The test ensure that the deleted show is returned and that the database no longer contains the show.

#### Green

Query:

|  |  |
| --- | --- |
|  | ``` function deleteItemshowID    return Showswhere parseIntshowID ``` |

Route:

|  |  |
| --- | --- |
|  | ``` // *** delete show *** // routerdelete'/shows/:id' function      queriesgetSingleparams   function      queriesdeleteItemparams     function        status     catchfunctionerror        error   catchfunctionerror      error ``` |

The Knex `delete()` function returns a number indicating the number of rows in the database that have been affected, so to return the deleted object, we must query for it first.

Let’s run those tests!!

|  |  |
| --- | --- |
|  | ``` API Routes   GET /api/v1/shows     ✓ should return all shows 69ms   GET /api/v1/shows/:id     ✓ should return a single show   POST /api/v1/shows     ✓ should add a show 54ms   PUT /api/v1/shows/:id     ✓ should update a show     ✓ should NOT update a show  the id field is part of the request   DELETE /api/v1/shows/:id     ✓ should delete a show  passing 1s ``` |

6 tests written. 5 routes built. All tests passing!

## Conclusion

So there you have it: A test-first approach to developing a RESTful API. Are we done? Not quite since we are not handling or testing for all possible errors.

For example, what would happen if we tried to POST an item without all the required fields? Or if we tried to delete an item that isn’t in the database? Sure the `catch()` methods will handle these, but they are simply passing the request to the built-in error handlers. We should handle these better in the routes and throw back appropriate error messages and status codes.

Try this out on your own. Be sure to grab the code from the [repository](https://github.com/mjhea0/mocha-chai-knex). Cheers!

*Edits made by [Bradley Bouley](https://www.linkedin.com/in/bbouley). Thank you!*
