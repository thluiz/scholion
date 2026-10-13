---
url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_5_-_practical_code_sharing_strategies"
captured_at: "2013-08-05T13:51:58-03:00"
title: "Part 5 - Practical Code Sharing Strategies | xamarin"
domain: "docs-xamarin-com"
---

# 1**.** Data Layer

The data layer consists of a storage engine and methods to read and write
information**.** For performance, flexibility and cross-platform compatibility the
SQLite database engine is recommended for Xamarin cross-platform applications**.**
It runs on a wide variety of platforms including Windows, Windows Phone,
Android, iOS and Mac**.**

## 1**.**1. SQLite

SQLite is an open-source database implementation**.** The source and
documentation can be found at [SQLite.org](http://www.sqlite.org/) **.** SQLite support is available on each mobile
platform:

- **iOS** – Built in to the operating system**.**
- **Android** – Built in to the operating system since Android
  2**.**2 (API Level 10).
- **Windows Phone** – Can support SQLite by shipping the
  open-source C# SQLite assembly with your app**.** More information can be found
  at [C#
  SQLite on Google Code](http://code.google.com/p/csharp-sqlite/) **.**

Even with the database engine available on all platforms, the native methods
to access the database are different**.** Both iOS and Android offer built-in APIs
to access SQLite that could be used from Xamarin.iOS or Xamarin.Android, however
using the native SDK methods offers no ability to share code (other than perhaps
the SQL queries themselves, assuming they’re stored as strings)**.** For details
about native database functionality search for CoreData in iOS or
Android’s SQLiteOpenHelper class; because these options are not
cross-platform they are beyond the scope of this document**.**

## 1.2. ADO.NET

Both Xamarin.iOS and Xamarin.Android support System.Data and
Mono.Data.Sqlite (see the Xamarin.iOS [documentation](http://docs.xamarin.com/guides/ios/advanced_topics/system.data)  for more info)**.**
Using these namespaces allows you to write ADO.NET code that works on both
platforms. Edit the project’s references to include
System.Data.dll and Mono.Data.Sqlite.dll and add these
using statements to your code:

```
using System.Data;
using Mono.Data.Sqlite;
```

Then the following sample code will work:

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32

`` string dbPath = Path.Combine (
Environment.GetFolderPath (Environment.SpecialFolder.Personal),
"items.db3");
bool exists = File.Exists (dbPath);
if (!exists)
SqliteConnection.CreateFile (dbPath);
var connection = new SqliteConnection ("Data Source=" + dbPath);
connection.Open ();
if (!exists) {
// This is the first time the app has run and/or that we need the DB.
// Copy a "template" DB from your assets, or programmatically create one like this:
var commands = new[]{
"CREATE TABLE [Items] (Key ntext, Value ntext);",
"INSERT INTO [Items] ([Key], [Value]) VALUES ('sample', 'text')"
};
foreach (var command in commands) {
using (var c = connection.CreateCommand ()) {
c.CommandText = command;
c.ExecuteNonQuery ();
}
}
}
// use `connection`... here, we'll just append the contents to a TextView
using (var contents = connection.CreateCommand ()) {
contents.CommandText = "SELECT [Key], [Value] from [Items]";
var r = contents.ExecuteReader ();
while (r.Read ())
Console.Write("\n\tKey={0}; Value={1}",
r ["Key"].ToString (),
r ["Value"].ToString ());
}
connection.Close (); ``

Real-world implementations of ADO.NET would obviously be split across
different methods and classes (this example is for demonstration purposes
only)**.**

## 1**.**3. SQLite-NET – Cross-Platform ORM

An ORM (or Object-Relational Mapper) attempts to simplify storage of data
modeled in classes**.** Rather than manually writing SQL queries that CREATE TABLEs
or SELECT, INSERT and DELETE data that is manually extracted from class fields
and properties, an ORM adds a layer of code that does that for you**.** Using
reflection to examine the structure of your classes, an ORM can automatically
create tables and columns that match a class and generate queries to read and
write the data**.** This allows application code to simply send and retrieve object
instances to the ORM, which takes care of all the SQL operations under the
hood**.**

SQLite-NET acts as a simple ORM that will allow you to save and retrieve your
classes in SQLite**.** It hides the complexity of cross platform SQLite access with
a combination of compiler directives and other tricks**.**

Features of SQLite-NET:

- Tables are defined by adding attributes to Model classes**.**
- A database instance is represented by a subclass of
  SQLiteConnection, the main class in the SQLite-Net library**.**
- Data can be inserted, queried and deleted using objects**.** No SQL
  statements are required (although you can write SQL statements if required)**.**
- Basic Linq queries can be performed on the collections returned by
  SQLite-NET**.**

The source code and documentation for SQLite-NET is available at [SQLite-Net on
github](https://github.com/praeclarum/sqlite-net)  and has been implemented in both case-studies**.** A simple example of
SQLite-NET code (from the *Tasky Pro* case study) is shown below**.**

First, the Task class uses attributes to define a field to be a
database primary key:

1  
2  
3  
4  
5  
6  
7  
8  
9

`public class Task : IBusinessEntity
{
public Task () {}
[PrimaryKey, AutoIncrement]
public int ID { get; set; }
public string Name { get; set; }
public string Notes { get; set; }
public bool Done { get; set; }
}`

This allows a “Task” table to be created with the following line of code
(and no SQL statements) on an SQLiteConnection instance:

```
CreateTable<Task> ();
```

Data in the table can also be manipulated with other methods on the
SQLiteConnection (again, without requiring SQL statements):

```
Insert (task); // 'task' is an instance with data populated in its properties
Update (task); // Primary Key field must be populated for Update to work
Table<Task>.ToList(); // returns all rows in a collection
```

See the case study source code for complete examples**.**

## 1.4. C# SQLite

The iOS and Android operating systems include a natively-compiled version of
SQLite in the operating system, however Windows Phone 7 does not include a
compatible database engine**.** SQLite has been ported to C# and is open-sourced on
[Google
Code](http://code.google.com/p/csharp-sqlite/) **.** This code has been downloaded and built as a Windows Phone assembly
that is included in the case studies, so that the same database (SQLite) can be
used across all three platforms.

The Windows Phone apps in the case studies must reference the
Community.CsharpSqlite**.**WP7.dll in their Core projects in order to
share the [SQLite-NET](https://github.com/praeclarum/sqlite-net)  implementation and database code**.**

# 2**.** File Access

File access is certain to be a key part of any application**.** Common examples
of files that might be part of an application include:

- SQLite database files**.**
- User-generated data (text, images, sound, video)**.**
- Downloaded data for caching (images, html or PDF files)**.**

## 2.1. SYSTEM.IO Direct Access

Both Xamarin.iOS and Xamarin.Android allow file system access using classes in
the System**.**IO namespace.

Each platform does have different access restrictions that must be taken into
consideration:

- iOS applications run in a sandbox with very restricted file-system
  access**.** Apple further dictates how you should use the file system by
  specifying certain locations that are backed-up (and others that are not)**.**
  Refer to the [Working
  with the File System in Xamarin.iOS](http://docs.xamarin.com/guides/ios/application_fundamentals/working_with_the_file_system)  guide for more
  details**.**
- Android also restricts access to certain directories related to the
  application, but it also supports external media (eg**.** SD cards) and accessing
  shared data.
- Windows Phone 7 does not allow direct file access – files can only be
  manipulated using isolated storage**.**

A trivial example that writes and reads a text file is shown below**.** Using
Environment.GetFolderPath allows the same code to run on iOS and
Android, which each return a valid directory based on their filesystem
conventions**.**

1  
2  
3  
4  
5

`string filePath = Path.Combine (
Environment.GetFolderPath (Environment.SpecialFolder.Personal),
"MyFile.txt");
System.IO.WriteAllText (filePath, "Contents of text file");
Console.WriteLine (System.IO.WriteAllText (filePath));`

Refer to the Xamarin.iOS [Working with
the File System](http://docs.xamarin.com/guides/ios/application_fundamentals/working_with_the_file_system)  document for more information on iOS-specific filesystem
functionality**.** When writing cross-platform file access code, remember that some
file-systems are case-sensitive and have different directory separators**.** It is
good practice to always use the same casing for filenames and the
Path.Combine() method when constructing file or directory
paths**.**

## 2.2**.** ISOLATED STORAGE

Isolated Storage is a common API for saving and loading files across all
three platforms.

It is the default mechanism for file access in Windows Phone that has been
implemented in Xamarin.iOS and Xamarin.Android to allow common file-access code
to be written**.** The System**.**IO.IsolatedStorage class can be
referenced across all three platforms in a shared-code project**.**

Refer to the [Isolated Storage Overview for Windows Phone](http://msdn.microsoft.com/en-us/library/ff402541(v=vs.92).aspx)  for more
information**.**

# 3. Network Operations

Most mobile applications will have networking component, for example:

- Downloading images, video and audio (eg**.** thumbnails, photos, music).
- Downloading documents (eg**.** HTML, PDF).
- Uploading user data (such as photos or text)**.**
- Accessing web services or 3rd party APIs (including SOAP, XML or JSON)**.**

The .NET Framework provides two main classes for accessing network resources:
WebClient and HttpWebRequest**.**

## 3.1**.** WebClient

The WebClient class provides a simple API to retrieve remote
data from remote servers**.**

Windows Phone operations *must* be async, even though Xamarin.iOS and
Xamarin.Android support synchronous operations (which can be done on background
threads)**.**

The code for a simple asychronous WebClient operation is:

1  
2  
3  
4  
5  
6  
7  
8

`var webClient = new WebClient ();
webClient.DownloadStringCompleted += (sender, e) =>
{
var resultString = e.Result;
// do something with downloaded string, do UI interaction on main thread
};
webClient.Encoding = System.Text.Encoding.UTF8;
webClient.DownloadStringAsync (new Uri ("http://some-server.com/file.xml"));`

WebClient also has DownloadFileCompleted and
DownloadFileAsync for retrieving binary data**.**

The *MWC 2012* case study uses WebClient to download
conference data**.** The code is in the Core project and is shared across iOS,
Android and Windows Phone (refer to the MwcSiteParser class)**.**

## 3**.**2. HttpWebRequest

HttpWebRequest offers more customization than
WebClient and as a result requires more code to use**.**

The code for a simple synchronous HttpWebRequest operation
is:

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13

`var request = HttpWebRequest.Create(@"http://some-server.com/file.xml ");
request.ContentType = "text/xml";
request.Method = "GET";
using (HttpWebResponse response = request.GetResponse() as HttpWebResponse)
{
if (response.StatusCode != HttpStatusCode.OK)
Console.WriteLine("Error fetching data. Server returned status code: {0}", response.StatusCode);
using (StreamReader reader = new StreamReader(response.GetResponseStream()))
{
var content = reader.ReadToEnd();
// do something with downloaded string, do UI interaction on main thread
}
}`

There is an example in our [Web Services documentation](http://docs.xamarin.com/guides/cross-platform/application_fundamentals/introduction_to_web_services#USING_HTTPWEBREQUEST), and you can read about the class for [Windows Phone on MSDN](http://msdn.microsoft.com/en-us/library/ff637320(v=vs.95).aspx) **.**

## 3.3**.** Reachability

Mobile devices operate under a variety of network conditions from fast Wi-Fi
or 4G connections to poor reception areas and slow EDGE data links**.** Because of
this, it is good practice to detect whether the network is available and if so,
what type of network is available, before attempting to connect to remote
servers**.**

Actions a mobile app might take in these situations include:

- If the network is unavailable, advise the user**.** If they have manually
  disabled it (eg**.** Airplane mode or turning off Wi-Fi) then they can resolve
  the issue**.**
- If the connection is 3G, applications may behave differently (for
  example, Apple does not allow apps larger than 20Mb to be downloaded over
  3G)**.** Applications could use this information to warn the user about excessive
  download times when retrieving large files**.**
- Even if the network is available, it is good practice to verify
  connectivity with the target server before initiating other requests**.** This
  will prevent the app’s network operations from timing out repeatedly and also
  allow a more informative error message to be displayed to the user**.**

There is a [Xamarin.iOS sample](https://github.com/xamarin/monotouch-samples/tree/master/ReachabilitySample)  available (which is based on Apple’s
[Reachability sample code](http://developer.apple.com/library/ios/#samplecode/Reachability/Introduction/Intro.html)
) to help detect network availability**.** The
*MWC 2012* case study iOS app includes an example of the reachability
code**.**

# 4**.** WebServices

See our documentation on [Working with
Web Services](http://docs.xamarin.com/guides/cross-platform/application_fundamentals/introduction_to_web_services) , which covers accessing REST, SOAP and WCF endpoints using
Xamarin.iOS**.** It is possible to hand-craft web service requests and parse the
responses, however there are libraries available to make this much simpler,
including RestSharp and ServiceStack**.** Even basic WCF operations can be accessed
in Xamarin apps**.**

## 4**.**1. RestSharp

RestSharp is a .NET library that can be included in mobile applications to
provide a REST client that simplifies access to web services**.** It helps by
providing a simple API to request data and parse the REST response**.** RestSharp
can be useful

The [RestSharp website](http://restsharp.org/) 
contains [documentation](https://github.com/restsharp/RestSharp/wiki)  on how to implement a REST client using RestSharp**.**
RestSharp provides Xamarin.iOS and Xamarin.Android examples on [github](https://github.com/restsharp/RestSharp/) **.**

There is also a Xamarin.iOS code snippet in our [Web Services documentation](http://docs.xamarin.com/guides/cross-platform/application_fundamentals/introduction_to_web_services#USING_RESTSHARP)**.**

## 4.2**.** ServiceStack

Unlike RestSharp, ServiceStack is both a server-side solution to host a web
service as well as a client library that can be implemented in mobile
applications to access those services**.**

The [ServiceStack
website](http://servicestack.net/)  explains the purpose of the project and links to document and code
samples**.** The examples include a complete server-side implementation of a web
service as well as various client-side applications that can access it**.**

There is a [Xamarin.iOS example](http://www.servicestack.net/monotouch/remote-info/)  on the ServiceStack website, and a code
snippet in our [Web Services documentation](http://docs.xamarin.com/guides/cross-platform/application_fundamentals/introduction_to_web_services#USING_SERVICESTACK_CLIENT)**.**

## 4.3. WCF

Xamarin tools can help you consume the same Windows Communication Foundation
(WCF) services as similar .NET clients**.** In general, Xamarin supports the same
client-side subset of WCF that ships with the Silverlight runtime**.** This includes
the most common encoding and protocol implementations of WCF: text-encoded SOAP
messages over the HTTP transport protocol using the BasicHttpBinding**.**

Due to the size and complexity of the WCF framework, there may be current and
future service implementations that will fall outside of the scope supported by
Xamarin’s client-subset domain**.** In addition, WCF support requires the use of
tools only available in a Windows environment to generate the proxy**.** Therefore,
WCF support should currently be considered “in preview**.**”

# 5. Threading

Application responsiveness is important for mobile applications – users
expect applications to load and perform quickly**.** A ‘frozen’ screen that
stops accepting user-input will appear to indicate the application has crashed,
so it is important not to tie up the UI thread with long-running blocking calls
such as network requests or slow local operations (such as unzipping a file)**.** In
particular the startup process should not contain long-running tasks – all
mobile platforms will kill an app that takes too long to load**.**

This means your user interface should implement a ‘progress indicator’ or
otherwise ‘useable’ UI that is quick to display, and asynchronous tasks to
perform background operations**.** Executing background tasks requires the use of
threads, which means the background tasks needs a way to communicate back to the
main thread to indicate progress or when they have completed**.**

## 5.1. Parallel Task Library

Tasks created with the Parallel Task Library can run asynchronously and
return on their calling thread, making them very useful for triggering
long-running operations without blocking the user interface**.**

A simple parallel task operation might look like this:

1  
2  
3  
4  
5  
6  
7

`using System.Threading.Tasks;
void MainThreadMethod ()
{
Task.Factory.StartNew (() => wc.DownloadString ("http://...")).ContinueWith (
t => label.Text = t.Result, TaskScheduler.FromCurrentSynchronizationContext()
);
}`

The key is TaskScheduler.FromCurrentSynchronizationContext()
which will reuse the SynchronizationContext.Current of the thread calling the
method (here the main thread that is running MainThreadMethod) as a
way to marshal back calls to that thread**.** This means if the method is called on
the UI thread, it will run the ContinueWith operation back on the
UI thread**.**

If the code is starting tasks from other threads, use the following pattern
to create a reference to the UI thread and the task can still call back to
it:

```
static Context uiContext = TaskScheduler.FromCurrentSynchronizationContext();
```

## 5**.**2. Invoking on the UI Thread

For code that doesn’t utilize the Parallel Task Library, each platform has
its own syntax for marshaling operations back to the UI thread:

- iOS: owner.BeginInvokeOnMainThread(new NSAction(action));
- Android: owner.RunOnUiThread(action);
- Windows: Deployment.Current.Dispatcher.BeginInvoke(action);

Both the iOS and Android syntax requires a ‘context’ class to be
available which means the code needs to pass this object into any methods that
require a callback on the UI thread**.**

To make UI thread calls in shared code, follow the [IDispatchOnUIThread example](http://www.slideshare.net/follesoe/cross-platform-mobile-apps-using-net)  (courtesy of [@follesoe](http://jonas.follesoe.no/) )**.** Declare and program
to an IDispatchOnUIThread interface in the shared code and then
implement the platform-specific classes as shown here:

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30

`// program to the interface in shared code
public interface IDispatchOnUIThread {
void Invoke (Action action);
}
// iOS
public class DispatchAdapter : IDispatchOnUIThread {
public readonly NSObject owner;
public DispatchAdapter (NSObject owner) {
this.owner = owner;
}
public void Invoke (Action action) {
owner.BeginInvokeOnMainThread(new NSAction(action));
}
}
// Android
public class DispatchAdapter : IDispatchOnUIThread {
public readonly Activity owner;
public DispatchAdapter (Activity owner) {
this.owner = owner;
}
public void Invoke (Action action) {
owner.RunOnUiThread(action);
}
}
// WP7
public class DispatchAdapter : IDispatchOnUIThread {
public void Invoke (Action action) {
Deployment.Current.Dispatcher.BeginInvoke(action);
}
}`

# 6**.** Platform and Device Capabilities and Degradation

Further specific examples of dealing with different capabilities are given in
the Platform Capabilities documentation**.** It deals with detecting different
capabilities and how to gracefully degrade an application to provide a good user
experience, even when the app can’t operate to its full potential**.**

[Part 6 - Testing and App Store Approvals](http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_6_-_testing_and_app_store_approvals)  >>
