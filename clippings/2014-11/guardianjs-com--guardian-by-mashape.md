---
url: "http://guardianjs.com/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2014-11-23T08:10:14-03:00"
title: "Guardian by Mashape"
domain: "guardianjs-com"
---

# Overview

Consuming OAuth services has never been easier. Guardian reduces the OAuth footprint in your code to a *single* request.

Built with modularity in mind, Guardian leverages plugins to handle OAuth flows, should you encounter a flow that Guardian doesn't handle, create a small flow plugin to do so and carry on. Guardian comes with **5** pre-made plugins that cover **99%** of OAuth services.

Not to mention, Guardian is perfect for **both** production *and* testing. Services like Github require you to enter a single callback url, this is fine when in production, but move to another environment and soon you'll have conflicts, require building complex services to juggle environment scenarios and more. Guardian is centralized and easily configurable to allow multiple environments giving you the flexibility you need.

Created with love by [nijikokun](http://github.com/nijikokun) at [http://mashape.com](http://mashape.com/)

## Requirements

- [Node.js](http://nodejs.org/download/)
- [Redis](http://redis.io/topics/quickstart)

## Install

Install [Redis](http://redis.io/topics/quickstart), then install Guardian globally:

```
$ npm install -g guardian
```

## Usage

```
$ guardian
```

### Configuration

Configuration files are loaded from the current working directory of where you call Guardian. Should no configuration argument be passed `./config/default.js` is loaded.

```
$ guardian -c <relative configuration path>
```

**Options**

|
|  |
|
|
| `host` | |
| Default | `localhost:3000` |
| Description | Public IP or Domain Name, used to generate the callback uri. |
|
| `protocol` | |
| Default | `http` |
| Description | Host Protocol |
|
| `port` | |
| Default | `3000` |
| Description | Server Port |
|
| `workers` | |
| Default | `require('os').cpus().length` |
| Description | Number of forked instances of the Guardian server to run, suggested amount is CPU count. |
|
| `pid.dir` | |
| Default | `./` |
| Description | `.guardian.pid` file output directory, for production we suggest placing this under the `/home/<user>/` directory, requires trailing slash. |
|
| `redis.host` | |
| Default | `127.0.0.1` |
| Description | Host redis can be reached on |
|
| `redis.port` | |
| Default | `6379` |
| Description | Port redis is current running on |
|
| `redis.pass` | |
| Description | Redis password |
|
| `redis.expire` | |
| Default | `60` |
| Description | Guardian store expiration timeout in Seconds |
|
| `cookie.secret` | |
| Description | Guardian cookie secret |
|
| `session.secret` | |
| Description | Guardian session secret |

## Routes

Guardian HTTP API for handling authentication flows.

### Storage

```
POST /store
```

Stores information given, returns a session hash to be used later on.
Information stored lives for `60` seconds by default, change `redis.expire` to alter timeout duration.

#### Parameters

###### OAuth 2

Details specific to OAuth2

|
|  |
|
|
| `client_id` | |
| Description | OAuth Client Identifier |
|
| `client_secret` | |
| Description | OAuth Client Secret |
|
| `grant_type` | |
| Description | Common values (dependant on OAuth flow used): `authorization_code`, `client_credentials`, `password`, `refresh_token`, ... |
|
| `access_name` | |
| Default | `access_token` |
| Description | Access token name |
|
| `authorize_method` | |
| Default | `Bearer` |
| Description | *Optional* - Authorization header method, some possible values: `Bearer`, `OAuth`, `Digest` |
|
| `state` | |
| Description | State identifier, depends on provider |
|
| `scope` | |
| Description | OAuth request scopes, depends on provider |

###### OAuth 1

Details specific to OAuth 1.0a

|
|  |
|
|
| `consumer_key` | |
| Description | OAuth Consumer Identifier |
|
| `consumer_secret` | |
| Description | OAuth Consumer Secret |
|
| `signature_method` | |
| Default | `HMAC-SHA1` |
| Description | OAuth Header encryption method, possible values: `PLAINTEXT`, `HMAC-SHA1`, `RSA-SHA1` |
|
| `oauth_token` | |
| Description | *Optional;* OAuth Token. Used in OAuth 1.0a 1-Legged (Resource request) |

###### Plugin (*required*)

Parameters combined to create the [plugin file name](https://github.com/Mashape/guardian/blob/master/lib/core.js#L100-L118).

|
|  |
|
|
| `auth_type` | |
| Default | `oauth` |
| Description | Authentication type, `a-z` characters accepted only. |
|
| `auth_flow` | |
| Description | *Optional;* Authentication flow, would be `echo`, `owner_resources`, etc... `a-z` characters accepted only. |
|
| `auth_version` | |
| Description | *Optional;* Authentication version, for OAuth 2, we would use `2`, numeric only. |
|
| `auth_leg` | |
| Description | *Optional;* Authentication leg, for OAuth 2 (3-legged), we would use `3`, numeric only. |

For example, [`plugins/oauth_2_3-legged.js`](http://guardianjs.com/plugins/oauth_2_3-legged.js) (OAuth 2, 3-legged), would look like:

```
{
  ...
  auth_type: 'oauth',
  auth_version: 2,
  auth_leg: 3
  ...
}
```

###### General

|
|  |
|
|
| `request_url` | |
| Description | Authentication Request Url, e.g. `https://github.com/login/oauth/request_url` |
|
| `access_url` | |
| Description | Authentication Access Url, e.g. `https://github.com/login/oauth/access_token` |
|
| `authorize_url` | |
| Description | Authentication Authorization Url, e.g. `https://github.com/login/oauth/authorize` |
|
| `callback` | |
| Description | Authentication Callback URL on requesting server to obtain `access_token` and `access_secret`, e.g. `http://localhost:3001/callback` |

#### Example

Request:

```
> POST https://<guardian-host>/store

{
  client_id: 'Client Identifier',
  client_secret: 'Client Secret',
  access_name: 'access_token',
  authorize_url: 'https://github.com/login/oauth/authorize',
  access_url: 'https://github.com/login/oauth/access_token',
  request_url: 'https://github.com/login/oauth/request_url',
  auth_type: "oauth",
  auth_version: 2,
  auth_leg: 3,
  callback: "http://localhost:3001/callback"
}
```

Response:

```
< 200 OK
< Header: Content-Type=application/json

{
  hash: '<guardian session hash>',
  url: 'https://<guardian-host>/start?hash=<guardian session hash>'
}
```

### Hash Check

```
GET /hash-check
```

Allows you to preview / verify your stored information in-case of error or malformed response.

Once again, stored information by default lasts only `10` seconds.

#### Parameters

|
|  |
|
|
| `hash` | |
| Description | Guardian session hash obtained from [Storage](http://guardianjs.com/?utm_source=javascriptweekly&utm_medium=email#storage) |

### Start

```
GET /start?hash=<guardian store hash>
```

Redirecting the client to this route starts the Guardian authentication steps, Each steps are done with `302` response code and should be followed.

#### Parameters

|
|  |
|
|
| `hash` | |
| Description | Guardian session hash obtained from [Storage](http://guardianjs.com/?utm_source=javascriptweekly&utm_medium=email#storage) |

###### OAuth 1.0a

Used in the OAuth 1.0a Signature Process for 1-Legged requests. [Example](https://github.com/Mashape/guardian/blob/master/tests/factual.js#L46).

|
|  |
|
|
| `url` | |
| Description | Request URL, query parameters will be parsed from here as well as parameters property. |
|
| `method` | |
| Description | Request Method. |
|
| `body` | |
| Description | Request Payload / Body. |
|
| `parameters` | |
| Description | Request Parameters for Request Signatures or etc... |

## Tests & Examples

Each test in the test folder is based on an API or feature of guardian rather than TDD or BDD based tests, we verify successful authentication and we can retrieve information while authenticated from the API using tokens Guardian provides.

In this manner the tests also serve as very good [examples](https://github.com/Mashape/guardian/blob/master/tests/) of how to use Guardian.

To run one of these test you'll need to have keys ready and run the following command:

```
$ node tests/<provider name>.js \
  -k {Your Consumer/Client Key/Id} \ 
  -s {Your Consumer/Client Secret} \
  -h {host, ie: localhost or domain}
```

Then visit the server running on port `3001` to start the authentication process.

You will recieve a response with the headers sent, and the returned response from the API, Guardian must be running locally on port `3000` for these examples to work correctly.

## License

[MIT](https://github.com/Mashape/guardian/blob/master/LICENSE)
