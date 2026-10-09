---
url: "http://blogs.msdn.com/b/visualstudio/archive/2014/04/14/using-visual-studio-to-build-universal-xaml-apps.aspx"
captured_at: "2014-04-28T21:44:17-03:00"
title: "Using Visual Studio to build Universal XAML Apps - The Visual Studio Blog - Site Home - MSDN Blogs"
domain: "blogs-msdn-com"
---

# Using Visual Studio to build Universal XAML Apps

At the Build conference, we announced the release of the new converged Windows Phone 8.1 and Windows 8.1 platforms. As a developer, this means you can now build XAML and HTML universal apps that run on both Phone and Tablets by sharing a significant amount of code and content. To enable building universal apps, we added a number of new features to Visual Studio as part of the [Visual Studio Update 2 RC](http://www.microsoft.com/en-us/download/details.aspx?id=42307).

You have two ways to learn more about these features. One way is through this blog post. The other way is by watching my [Build talk](http://channel9.msdn.com/Events/Build/2014/3-591) that covers all of the material you will see here in more detail:

There is no right or wrong way here, so pick either the video or the blog depending on how much time you have. Without further delay, let’s take a quick look at universal apps!

# Creating Universal Apps

To help you get started with building universal apps in C#, C++, and JS, we created new project templates that contain the basic structure and behind-the-scenes configurations to allow you to share code and content:

[![New Project Templates](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/2744.NewProjectTemplates_5F00_thumb_5F00_69CCFC60.png "New Project Templates")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/8117.NewProjectTemplates_5F00_6071372C.png)

If you already have an existing Windows 8.1 application, you can use the “Add Windows Phone 8.1” command to add a new Windows Phone 8.1 project and a shared project to the solution. A similar option is also available if you have a Windows Phone 8.1 application, and wanted to add support for Windows 8.1.

[!['Add Windows Phone 8.1' command in Solution Explorer](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/1373.AddWindowsPhone8.1commandinSolutionExplorer_5F00_thumb_5F00_5B8E8370.png "'Add Windows Phone 8.1' command in Solution Explorer")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/5481.AddWindowsPhone8.1commandinSolutionExplorer_5F00_62ADBFE8.png)

# Structure of Universal Apps

A universal app is a collection of three projects – a Windows Store project, a Windows Phone project and a Shared project – enclosed in a solution folder that is optional. The Windows Store and Windows Phone projects are platform projects and are responsible for creating the application packages (.appx) targeting the respective platforms. These projects contain assets that are specific to the platform being targeted.

The Shared project contains assets that are shared between the Windows Store and Windows Phone projects. The set of item types (.cs, xaml, .xml, .png, .resw, etc.) supported by the shared projects is the same as the platform projects. Shared projects by themselves don’t have a binary output but their contents are imported by the platform projects and used as part of the build process to generate the Windows Store and Windows Phone application packages (.appx).

[![Separate projects for Windows 8.1 and Windows Phone 8.1](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/7506.SeparateprojectsforWindows8.1andWindowsPhone8.1_5F00_thumb_5F00_72505BAA.png "Separate projects for Windows 8.1 and Windows Phone 8.1")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/8463.SeparateprojectsforWindows8.1andWindowsPhone8.1_5F00_32867525.png)

# Writing code in the Shared project

While developing your universal app, you will mostly be writing code that runs on both platforms. If required, you can also write platform specific code in the Shared projects using #if and #endif directives. By default, we have predefined the following conditional compilation constants that you could use to write platform specific code.

|  |  |  |
| --- | --- | --- |
| C# | WINDOWS\_APP | WINDOWS\_PHONE\_APP |
| C++ | WINAPI\_FAMILY\_PC\_APP | WINAPI\_FAMILY\_PHONE\_APP |

# Context switcher in the editor

While writing code in a Shared project, you can use the project context switcher in the navigation bar to select the platform you are actively targeting, which in turn drives the intellisense experience in the code editor.

[![Project Context Switcher](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/7180.4ProjectContextSwitcher_5F00_thumb_5F00_6D6DA7EE.png "Project Context Switcher")](http://blogs.msdn.com/cfs-filesystemfile.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92/0564.UniversalAppsXAML_2D00_PrjStructure_2D00_Project-Context-Switcher.png)

[![Intellisense](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/6740.5Intellisense_5F00_thumb_5F00_2D378E74.png "Intellisense")](http://blogs.msdn.com/cfs-filesystemfile.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92/0020.UniversalAppsXAML_2D00_PrjStructure_2D00_Intellisense.png)

# Switching startup projects using debug target dropdown

We have also added the ability to quickly switch the startup projects in the debug target dropdown that now enumerates all the possible projects in the solution that you might want to deploy to a device or emulator/simulator.

[![Switch startup project in the debug target dropdown](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/6862.Switchstartupprojectinthedebugtargetdropdown_5F00_thumb_5F00_042F8029.png "Switch startup project in the debug target dropdown")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/8507.Switchstartupprojectinthedebugtargetdropdown_5F00_5405A4B4.png)

# Sharing code across Universal Apps

You can use class libraries to share your code across different universal apps. For C# and Visual Basic, we have improved the existing Portable Class Libraries (PCLs) to also support Windows Runtime and XAML when targeting Windows 8.1 and Windows Phone 8.1 platforms. Check out this [blog for more details on PCL improvements](http://blogs.msdn.com/b/dotnet/archive/2014/04/03/the-next-generation-of-net.aspx).

[![Improved Portable Class Libraries](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/8103.ImprovedPortableClassLibraries_5F00_thumb_5F00_0AE289AC.png "Improved Portable Class Libraries")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/4718.ImprovedPortableClassLibraries_5F00_7D1043B0.png)

For C++, you can use the new Class Library project templates under “Universal Apps” with shared projects to share your code between Windows 8.1 and Windows Phone 8.1 class libraries.

[![Class Library project templates for C  ](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/2577.ClassLibraryprojecttemplatesforC_5F00_thumb_5F00_1195932F.png "Class Library project templates for C  ")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-29-92-metablogapi/2555.ClassLibraryprojecttemplatesforC_5F00_03C34D34.png)

I hope you found this overview of building XAML universal apps useful. If you have any questions or comments, please feel free to post below or contact us via [forums](http://social.msdn.microsoft.com/Forums/wpapps/en-us/home?category=wpapps) or [UserVoice](http://visualstudio.uservoice.com/forums/121579-visual-studio/category/44115-xaml-tools) . Stay tuned for another blog explaining the new XAML tooling features we have added in Visual Studio to support Windows Phone 8.1 applications.

|  |  |
| --- | --- |
|  | **Author**: Navit Saxena, Program Manager  Navit Saxena is a Program Manager on the Visual Studio team. For over five years, Navit has been focused on XAML tooling in Visual Studio and Blend. He enjoys building Windows & Windows Phone apps and is always looking for ways to improve the XAML developer tools. |
