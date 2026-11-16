---
url: "https://visualstudiomagazine.com/articles/2020/01/06/defining-grpc-messages.aspx"
captured_at: "2026-11-16T05:07:33+00:00"
title: "How to Design Messages for gRPC Services in .NET Core -- Visual Studio Magazine"
domain: "visualstudiomagazine-com"
---

PRACTICAL .NET

How to Design Messages for gRPC Services in .NET Core

Defining your gRPC service using the Protocol Buffers specification is pretty easy. There are just a couple of things to be aware of as you convert from the specification to .NET Core and then manage your service's evolution.

By Peter Vogel01/06/2020

In a previous column, I described how to build both a gRPC service and a client that could access it, using ASP.NET Core Version 2.2/3.0, Visual Studio 2019 Preview, and the proto3 specification. The core of creating a gRPC service is the .proto file that describes the service in a language-neutral format. Using a .proto file, Visual Studio can generate either a base class for your service (you just write your business-specific code) or a client class that you can use to reliably access the service.

A .proto file must be compliant with Google's Protocol Buffers specification (commonly called ProtoBuf). The contents of a proto file allow you to specify the interface for your service. A service interface consists of two parts:

The methods your gRPC service makes available
The data structure of the parameters and return values for those methods

You build up these data structures (called "messages" in ProtoBuf-speak) using the scalar types defined in the Protocol Buffers specification. The available types include boolean, string, byte array and various numeric types (float, integers, longs). There are no date or fixed decimal types. In an upcoming column, I'll show you how to add a timestamp type. For decimals you can use float ... with the accompanying possibility of loss of precision that comes with floats.

If you're starting a new project, you'll want to use the proto3 syntax which has been around since 2016. However, you must explicitly specify the proto3 standard on the first "non-empty" line of your .proto file (to quote the specification) otherwise your .proto file will be parsed using the proto2 specification. Specifying that your file uses proto3 looks like this:

syntax = "proto3";

Messages and C# Classes

Using the proto3 specification, a message format for customer information might look like this:

message CustomerResponse {
int32 custid = 1;
string firstName = 2;
string lastName = 3;
int32 age = 4;
fixed32 creditLimit = 5;
}

The numbers that follow the equals sign specify the position of the field in the message, beginning with position 1 (in my example, firstName will be the second field in the message). These numbers must be unique within the message (i.e. you can't have two fields at the same position). You don't have to list the fields in numerical order but it makes it easier to spot duplicate field numbers if you do (though Visual Studio will spot any duplicate numbers and report them in the Error List when you build your application). You can also skip positions, if you want. This definition uses only odd numbers, for example:

message CustomerResponse {
int32 custid = 1;
string firstName = 3;
string lastName = 5;
}

In .NET Core, message formats are converted into classes with each field becoming a property on a class that has the same name as the message. .NET Core also converts the first character of your field names into uppercase when naming these properties. So, for example, the custId field in my previous example will become a CustId property on a CustomerResponse class in my code. Any underscores in your field names are also removed in this process and the following letter is uppercased (i.e. the Last_name field name becomes the LastName property).

That process also involves mapping .NET types to the ProtoBuf types (e.g. the ProtoBuf int32 becomes a .NET int, ProtoBuf's int64 becomes a long, fixed32 becomes uint) which has required adding some new classes to .NET Core. For example, byte arrays are supported in ProtoBuf with a type called bytes. That field type is supported by a new .NET data type called ByteString. To load a ByteString, you use the ByteString class' static CopyFrom method, passing a byte array, like this:

byte[] bytes = new byte[1000];
cr.Valid = ByteString.CopyFrom(bytes);

To retrieve a byte array from a ByteString, you use the object's CopyTo method, passing the array you want the bytes to be copied into and a start position:

cr.Valid.CopyTo(bytes,0);

Arrays and Dictionaries

You can also include collections in your definitions using the repeated keyword (fields that aren't collections are referred to as "singular" in ProtoBuf-speak). If my Customer message needs a set of repeating transaction amounts, I could specify the field like this:

message Customer {
int32 id = 1;
repeated fixed32 transactionAmounts = 4;

Repeated fields, when converted to a property on a class, also use a new type: Google.Protobuf.RepeatedField<T>. My example would generate a property of Google.Protobuf.RepeatedField<uint> (unsigned integer), for example. You can initialize the array using the {} syntax like this:

CustomerResponse cr = new CustomerResponse
{
CreditLimit = {10, 15, 100}
};

But you're probably more likely to use its various Add* methods to put items in the collection:

cr.CreditLimit.Add(200);

You can access items in a RepeatedField using the LINQ methods (e.g. First()) or by position. This works fine, for example:

uint tranAmount = cr.CreditLimit[1];

ProtoBuf also supports a Dictionary-type collection called map which allows you to specify types for a dictionary's keys and values. My Customer message might keep track of a Customer's various credit cards using "friendly names" to define a Dictionary that has a string both for the key ("Peter's Card", "My Travel Card") and for the value (the credit card number):

message CustomerResponse {
int32 custId = 1;
map<string, string> cards = 2;

Interestingly, in Visual Studio 2019 Preview, the editor doesn't highlight map like other types (it compiles just fine though).

The corresponding property will be of type Google.Protobuf.Collections.MapField and you load it by passing its Add method a key and a value, just like any other Dictionary.

Managing Change

Changing a .proto file after you go live (and clients start using it) is relatively forgiving. You can, for example, add fields with new position numbers to the .proto file used by your server-side software without disturbing clients still using an earlier version of the file: The client simply ignores fields not listed in its .proto file.

Similarly, in the reverse scenario (when the server .proto file doesn't have fields that the client's .proto field does) the client simply finds that the properties the server didn't send are set to their default value. By the way, fields defined in the server's .proto file that aren't defined in the client's .proto file are still sent to the client but .NET doesn't provide a convenient way to access it (at least, not yet).

Really, as your service evolves and you modify its .proto file, there are only two rules that you should abide by:

Don't change the position number of an existing field
Don't recycle position numbers (i.e. don't replace an obsolete field 3 with a new field 3)

However, the properties generated from the .proto file aren't nullable so, if you don't set a property to a value, it will be set to its default value. That means that numerics are set to 0; strings are set to string.Empty (a zero-length string); bools become false; a ByteString property defaults to a ByteString object with its IsEmpty property set to true; and both RepeatedField and MapField properties default to their corresponding objects, each with no items and with its Count property set to 0.

Because of this behavior there is some danger in removing a field from a service's .proto file and not updating all the clients (or just not setting a property on an object when generating a response on the server). The danger is that a client can't tell the difference between an unused field and a property that has been set to its default value. If my Customer's Valid property has been set to false, the client can't be sure if the Customer isn't valid or if the server is no longer generating that field.

You might want to consider initializing your properties to some "non-reasonable" value (e.g. -1 for numerics) so that clients can tell the difference between a property set to its default value and a field that's been removed. Because that's not possible with Boolean values (Booleans don't have non-reasonable values), you want to be especially wary of removing (or even no longer using) a field of type bool.

Efficiencies and Limitations

As I discussed in an earlier overview , one of the features of gRPC services is that their messages are much smaller than HTTP-based (RESTful) services. If you really want to exploit that efficiency, you'll care that positions 1 through 15 require only a single byte of extra overhead (i.e. data beyond the stored value) while positions 16 through 2047 require two bytes. Keeping message formats to under 16 positions seems like a good idea.

For other efficiency tips in terms of picking types to pack data into the smallest possible space, see the scalar type descriptions in the specification.

By the way, you can't use as field position numbers any of: negative numbers, 0, the numbers 19,000 through 19,999 (reserved for ProtoBuf's use), or numbers larger than 536,870,911. Can I also suggest that if you wanted to use those numbers then you have problems that I can't solve in this column.

Really. Stop doing that.

That's a quick introduction to the basics of defining gRPC messages. In upcoming columns I'll be looking at defining enumerated values, reusing types, managing states, and "well known types."

About the Author

Peter Vogel is a system architect and principal in PH&V Information Services. PH&V provides full-stack consulting from UX design through object modeling to database design. Peter tweets about his VSM columns with the hashtag #vogelarticles. His blog posts on user experience design can be found at http://blog.learningtree.com/tag/ui/.
