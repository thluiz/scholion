---
url: "https://brainhub.eu/blog/pwa-on-ios-13"
captured_at: "2026-11-16T02:23:00+00:00"
title: "PWA on iOS - Current Status & Limitations for Users [2025]"
domain: "brainhub-eu"
---

[

**\[REPORT\]** From Vision to Code: **A Guide to Aligning Business Strategy with Software Development Goals** is published!

GET IT here





](https://brainhub.eu/from-vision-to-code)

Apple couldn't stay behind anymore since PWAs are much more than a buzzword. What's the status now? Does iOS finally provide full support for PWAs? You'll find the answer below.

12 min read

–

Last updated on

June 5, 2025

**A QUICK SUMMARY – FOR THE BUSY ONES**

TABLE OF CONTENTS

## PWA on iOS - Current Status & Limitations for Users \[2025\]

### Introduction

Apple could care more about Progressive Web Apps, there’s no doubt about that. There’s not much documentation, the APIs are added slowly and most common things like Web App Manifest aren’t there for too long (at this point, I wonder if they will get there at all). On the other hand, **PWAs are a thing**. Maybe not as hyped as Machine Learning, but still, there’s a solid batch of those out there. And even Apple cannot ignore that fact forever.

## PWA on iOS - Current status \[2025\]

As of 2023-2024, Progressive Web Apps (PWAs) on iOS have evolved significantly, offering a more native app-like experience. While they still face certain limitations on iOS compared to Android, recent updates have brought improvements.

Key updates and features of PWAs on iOS include:

## **1\. Home screen addition**‍

Although Safari doesn't provide an automatic installation prompt, users can still add PWAs to their home screen. iOS 13 introduced a new Share Sheet design, making this process more intuitive with visual cues from the **apple-touch-icon** meta tag.

### Recent improvements

*   iOS 13 introduced changes to the Share Sheet, which affected how users add PWAs to their home screen. The design of the Share Sheet was updated, and it's recommended for developers to adjust their apps accordingly, particularly since Safari now uses the **apple-touch-icon** for the home screen icon, enhancing visual recognition for the user​​.

### Limitations

*   **No automatic prompt**: Unlike Android, iOS does not provide an automatic installation prompt from within Safari, so the process is less intuitive and relies on user action.
*   **Dependence on Safari's capabilities**: The functionality and appearance of the PWA when launched from the home screen depend on Safari's capabilities, as it is the underlying browser for PWAs on iOS.

### Importance

*   **User engagement**: Adding a PWA to the home screen can significantly increase user engagement and retention, as it makes the app more accessible and convenient to use.
*   **Branding opportunity**: The presence of the app icon on the home screen serves as a constant visual reminder of the app, reinforcing brand presence.

## **2\. Dark mode support**‍

PWAs on iOS 13 can support Dark Mode, aligning with the wider adoption of this feature across platforms.

*   **Consistency with device settings**: On iOS, PWAs that support Dark Mode can align with the system-wide Dark Mode settings of the device. This means the PWA can automatically switch between light and dark themes based on the user's system preferences.
*   **Implementation**: Implementing Dark Mode in a PWA involves using CSS media queries to detect the preferred color scheme of the user's device. Developers can then apply different styles or themes based on this preference. The relevant CSS feature is **prefers-color-scheme**, which can be set to **light** or **dark**.

### iOS-specific considerations

*   **Safari compatibility**: For PWAs on iOS, Dark Mode support hinges on Safari's support for the **prefers-color-scheme** media query. Fortunately, recent versions of Safari on iOS do support this feature.
*   **Limitations**: While PWAs can adapt their styles to match the Dark Mode setting, there are limitations in how far this integration goes. For example, it's not currently possible to change the app icon dynamically based on the theme.
*   **User preference respect**: An important aspect of implementing Dark Mode is respecting the user's system settings, providing a seamless experience that matches their overall device usage.

Read also: [5 Best PWA Examples](https://brainhub.eu/library/progressive-web-apps-examples)

## **3\. Motion sensor API**‍

From iOS 13 onwards, apps need to ask for permission to use motion sensors like the accelerometer and gyroscope, a change aimed at enhancing user privacy.

### iOS-specific considerations

*   **User permission**: One of the key aspects of using the Motion Sensor API on iOS is the requirement for explicit user permission. Due to privacy concerns and potential misuse, Apple mandates that apps request and obtain user consent before accessing motion sensor data.
*   **iOS 13 changes**: With iOS 13, there were significant changes to the Motion Sensor API usage. Previously, these sensors were freely accessible; however, the update introduced stricter controls, requiring apps to explicitly ask for permission​​.

### Impact on PWAs

*   **Enhanced interactivity**: For PWAs, the ability to use motion sensors opens up new possibilities for user interaction and engagement. It allows for more dynamic and responsive app designs, particularly in gaming, fitness apps, or any application where device movement can be a meaningful input.
*   **User privacy and security**: The requirement for explicit permission aligns with broader trends towards user privacy and security. While it adds an extra step in the user experience, it ensures users are aware of and consent to the data being used.
*   **Cross-platform considerations**: Developers need to be aware of how different platforms handle motion sensor access. While iOS requires explicit permission, the approach may differ on other platforms like Android.

## **4\. iPadOS distinctions**‍

With the introduction of iPadOS, iPads now offer a desktop-class browser experience. However, PWAs on iOS 13 do not automatically adjust their layout when switching to/from Split Mode on iPads.

iPadOS, while sharing a foundation with iOS, brought specific changes that impact the behavior and capabilities of PWAs on iPad devices.

### **Desktop-class browsing experience**‍

One of the major shifts with iPadOS is the provision of a desktop-class browsing experience in Safari. This means that websites and PWAs are rendered in a way that is more akin to the desktop version rather than the mobile version. This change enhances usability and functionality, especially for complex web applications.

### Development considerations

*   **Responsive design**: Developers need to ensure their PWAs are responsive and adaptable to different screen sizes and modes, especially considering the variable rendering between full-screen and Split View modes.
*   **Testing across modes and devices**: Thorough testing across various iPad models and configurations (including Split View and Slide Over) is crucial to ensure a consistent and user-friendly experience.
*   **Leveraging iPad features**: Developers should consider how to best use iPad-specific features like the Apple Pencil or trackpad support to enhance the functionality and appeal of their PWAs.

## **5\. Enhanced PWA installability and accessibility**‍

With updates like the "Add To Dock" button on desktop Safari and the "Add To Home Screen" button in in-app browsers using Safari View Controller, Apple has made installing and accessing PWAs more straightforward and user-friendly. These updates are part of a broader effort to improve the overall usability and appeal of PWAs on iOS platforms

1.  **Streamlined addition to home screen**: A key aspect of PWA installability on iOS is the ability for users to add these web apps to their home screen. While iOS traditionally hasn't provided an automatic installation prompt for PWAs like Android does, improvements in the ease of adding PWAs to the home screen have been noted. This involves using the Safari browser's share options to manually add the PWA to the home screen.
2.  **Improved web app manifest support**: The web app manifest is a crucial component for PWAs, as it defines the app's appearance when installed on the home screen, including icons, start URL, and display mode. Enhanced support for the web app manifest in Safari on iOS improves the overall installation and user experience, making PWAs feel more like native apps.
3.  **Full-screen and standalone modes**: Enhancements in full-screen and standalone modes for PWAs on iOS provide a more immersive user experience. When launched from the home screen, these PWAs can operate in a mode that's visually similar to native apps, without the typical browser UI elements.
4.  **Increased storage quotas**: Recent updates to Safari on iOS have included increases in the storage quotas assigned to web apps, including PWAs. This enhancement is significant for PWAs that need to store more data on the device, improving their functionality and user experience.
5.  **Safari improvements**: Ongoing updates to Safari, the primary browser for iOS, directly influence PWA capabilities. Enhanced support for modern web standards and APIs in Safari boosts the functionality and reliability of PWAs on iOS devices.
6.  **Greater focus on security and privacy**: With growing concerns around data security and user privacy, enhancements in these areas are also expected to continue, ensuring that PWAs offer a safe and secure experience for users.
7.  **Accessibility enhancements**: Improvements in accessibility features, ensuring PWAs are usable by people with various disabilities, are also a key focus. This includes better screen reader support, improved keyboard navigation, and adherence to WCAG guidelines.

## **6\. Improved user interaction**‍

Features like Pointer Events allow PWAs to detect whether interactions are made via finger, Apple Pencil, or mouse, particularly useful on iPadOS.

1.  **Touch and gesture controls**: Enhanced support for touch and gesture controls is crucial for PWAs on iOS. This includes smooth scrolling, pinch-to-zoom, and swipe gestures that are expected in a native app experience. Improvements in these areas make PWAs feel more natural and intuitive to use on touch-screen devices.
2.  **Responsive design and layouts**: With diverse iOS devices, including various models of iPhones and iPads, responsive design is essential. This means PWAs need to adapt seamlessly to different screen sizes and orientations, providing an optimal user experience across all devices.
3.  **Animation and transition effects**: Smooth and appealing animations and transition effects can significantly enhance user interaction in PWAs. These visual cues not only make the app more engaging but also help in guiding users through the app’s functionality.
4.  **Performance optimization**: Fast loading times and efficient performance are key aspects of user interaction. This includes optimizing images, scripts, and leveraging browser caching to ensure the PWA is responsive and efficient.
5.  **Improved offline capabilities**: Enhancements in offline functionality, such as better data caching and offline content availability, contribute significantly to user interaction. Users expect a degree of functionality even when they are not connected to the internet.

## **7\. Development and inspection tools**‍

PWAs are now inspectable on iOS, facilitating the development process.

### Development tools for PWAs on iOS

1.  **Web development IDEs**: Integrated Development Environments (IDEs) like Visual Studio Code, Sublime Text, and Atom are popular for PWA development. They offer features like syntax highlighting, code completion, and extensions/plugins specifically useful for web development.
2.  **Framework and library support**: Frameworks like React, Angular, and Vue.js, along with libraries like Ionic, are instrumental in PWA development. They provide a structured way to build dynamic web applications that can function as PWAs.
3.  **PWA builders**: Tools like PWABuilder or PWA Studio by Magento offer simplified ways to create PWAs. They can generate service workers, manifests, and even package PWAs for different platforms, including iOS.
4.  **Testing and debugging tools**: Tools like Lighthouse (for performance and quality auditing), Chrome DevTools (for debugging), and BrowserStack (for cross-browser testing) are essential in the PWA development lifecycle.

### Inspection tools for PWAs on iOS

1.  **Safari developer tools**: For PWAs on iOS, Safari's built-in developer tools are crucial. They allow developers to inspect, debug, and optimize their web applications for Safari on iOS devices.
2.  **Remote debugging**: Tools like Safari Web Inspector enable remote debugging of PWAs running on iOS devices. This is vital for testing and ensuring that the PWA behaves as expected on actual iOS hardware.
3.  **Performance monitoring tools**: Tools like Google's Lighthouse provide audits for performance, accessibility, progressive web apps, SEO, and more, offering valuable insights for optimizing PWAs for iOS.
4.  **Service worker testing tools**: Since service workers are a core component of PWAs, tools that facilitate testing and debugging of service workers are essential. This includes checking offline capabilities, caching strategies, and background sync functionality.

## **8\. Background running and app switcher integration**‍

PWAs on iOS now have improved background running capabilities. They can run in the background and reflect their state in the App Switcher, similar to native apps. This development, although still subject to certain restrictions, marks a significant step towards offering a more native app-like experience

### Background running in PWAs on iOS

**Limited background execution**‍

Traditionally, PWAs and web apps on iOS have had limited capabilities in running in the background compared to native apps. This is due to the restrictions iOS places on background processes to conserve battery life and maintain performance.

**Service Workers**‍

Service workers, a core technology behind PWAs, do run in the background, but their functionality is mainly focused on caching and push notifications (where supported). This enables some level of offline functionality and content updating in the background.

**Recent enhancements**‍

There have been improvements in how PWAs handle background tasks on iOS. For instance, more recent versions of iOS started to allow some form of background processing for web apps, but with certain limitations and conditions, especially regarding timers and resource management​​.

### App Switcher integration

**Enhanced User Experience**

Integration with the iOS app switcher is crucial for a seamless user experience. It allows users to view and switch between apps, including PWAs, as they would with native applications.

**App state preservation**‍

For a PWA to be practical and user-friendly, it should maintain its state when a user switches to another app and then returns. This means that the PWA should resume where the user left off, without reloading or losing progress.

**Visual representation**‍

In the app switcher, the PWA should ideally have a representative preview and icon, making it easily recognizable to the user. This visual representation is typically handled by the PWA's manifest settings and how the app is coded to behave in multitasking environments.

## Push notification support

With the release of iOS 16.4, Apple introduced support for push notifications in PWAs, allowing developers to send real-time alerts to users. However, this functionality requires users to grant explicit permission and is contingent upon the PWA being added to the home screen.

In response to the European Union's Digital Markets Act (DMA), Apple initially planned to limit PWA functionalities in the EU with the iOS 17.4 update. This decision would have reduced PWAs to mere web bookmarks without offline capabilities or push notifications. However, after receiving feedback, Apple reversed this decision and reinstated full PWA support in the EU.

## PWA on iOS - Limitations for users

The current limitations for users of Progressive Web Apps (PWAs) on iOS include:

### **Manual installation process**‍

Unlike native apps, PWAs don't have an automatic installation prompt in Safari. Users must manually add PWAs to their home screen, which may not be as intuitive as the installation process for native apps from the App Store.

### **Limited interaction with device features**‍

Certain device features and sensors may not be fully accessible or supported in PWAs on iOS. For example, while geolocation is supported, other functionalities like USB and Bluetooth connectivity are limited.

### **Variable performance across devices**‍

The performance and behavior of PWAs can vary across different iOS devices, particularly when considering the diverse capabilities and specifications of iPhones and iPads.

### **Limited offline capabilities**‍

While PWAs can work offline, their capabilities in this mode might be limited compared to native apps. The extent of offline functionality depends on how the PWA is designed and what data it caches.

### **App store discoverability**‍

While it's possible to submit PWAs to the App Store, they need to offer more than just a repackaged website. This can create a hurdle for PWA developers looking to leverage the App Store for discoverability.

### **Dependence on Safari**

PWAs on iOS rely heavily on Safari's capabilities and limitations, as it's the primary browser used for PWAs on Apple devices. Any limitations in Safari directly impact the capabilities of PWAs.

### **Limited support for advanced web features**‍

Safari's slower adoption of new web standards can limit the functionality of PWAs on iOS. For instance, features like Web Bluetooth or advanced payment options may not be available.

### **User Experience inconsistencies**‍

There can be inconsistencies in the user experience when using PWAs on iOS, especially when comparing them with their native app counterparts or their performance on other platforms like Android.

### **App state management**‍

Issues with managing the app state and layout changes, especially in the context of iPadOS and its Split Mode, can affect the usability of PWAs.

Read also: [Legacy Application Modernization Roadmap - a Step-by-Step Guide.](https://brainhub.eu/library/legacy-app-modernization-roadmap) Feel like the software in your company is no longer effective and has become a development blocker? That could mean it's time for a major update!

## Want to build a Progressive Web App? Here's what to consider

### Advantages of building a PWA for iOS

1.  **Broader reach and accessibility**: PWAs can be easily accessed via a web browser, without the need for downloading from an app store. This can expand your app's reach to a wider audience.
2.  **Reduced development costs**: Developing a PWA can be more cost-effective than creating a native app, especially if you aim to support multiple platforms. You can use a single codebase for both iOS and Android, reducing development and maintenance costs​​.
3.  **Improved performance and features**: Recent advancements in PWAs, such as the addition of push notifications, enhanced offline capabilities, and background running, make them more competitive with native apps in terms of functionality​​​​.
4.  **Ease of updating**: PWAs can be updated more easily than native apps. Updates are deployed on the server side, eliminating the need for users to download updates from the App Store.

### Considerations and challenges

1.  **User Experience**: While PWAs have improved significantly, there may still be some gaps in user experience compared to native apps, especially in terms of advanced features and integration with iOS-specific functionalities.
2.  **App store presence**: PWAs are not distributed through the App Store, which can be a significant channel for user discovery and trust. Depending on your target audience, not being on the App Store could be a limitation.
3.  **Limited access to iOS features**: PWAs may not have access to all iOS features and capabilities that native apps do, such as certain hardware integrations and advanced APIs.
4.  **Variable performance across devices**: PWAs can behave differently across various iOS devices, depending on factors like browser capabilities and hardware specifications.

### Tips for building a PWA for iOS

1.  **Focus on performance**: Ensure your PWA is optimized for performance, especially on mobile devices. This includes fast loading times, efficient use of data, and smooth animations.
2.  **Design for mobile-first**: Prioritize a responsive, mobile-first design to provide a seamless experience on iOS devices.
3.  **Test extensively**: Thoroughly test your PWA on multiple iOS devices and browsers to identify and fix any compatibility or performance issues.
4.  **Leverage latest web capabilities**: Stay updated with the latest web technologies and standards to enhance the capabilities of your PWA.
5.  **Consider user engagement strategies**: Since PWAs don't support all native features, think creatively about user engagement strategies. For example, consider alternative methods for push notifications if they are crucial for your app.
6.  **Prepare for offline use**: Implement service workers for offline support, which is a key feature of PWAs.

Read also: [DORA Metrics: 4 Ways to Measure Software Delivery Performance](https://brainhub.eu/library/devops-dora-metrics). Improved processes and fast, stable delivery ﹣that’s what you get after starting to measure your team’s performance with DORA metrics. Learn how each of the metrics works and set the path to boosting your team’s performance and business results.

## Progressive Web Apps + iOS – A slow evolution

As you can see, things are changing slowly. Even if they don’t say it out loud, Apple has moved a bit closer to Progressive Web Apps. While the development of Progressive Web Apps for iOS is still more difficult than for the Android-based phones, it gets better over time. And there’s no doubt your business can still benefit from PWAs. Even on iOS.

Our company invests time in Progressive Web Apps by developing and popularizing them. If you're actively exploring a PWA project and want expert support, check out our curated list of [top web app development companies](https://brainhub.eu/library/top-web-app-development-companies) trusted by tech leaders to build fast, modern, and cross-platform experiences.

## Frequently Asked Questions

No items found.

Our promise  

Every year, Brainhub helps founders, leaders and software engineers make smart tech decisions. We earn that trust by openly sharing our insights based on practical software engineering experience.

Authors

A serial entrepreneur, passionate R&D engineer, with 15 years of experience in the tech industry. Shares his expert knowledge about tech, startups, business development, and market analysis.

![](https://cdn.prod.website-files.com/622fa4d65a5fab0c3465af07/62692989e08e8651c846ce3f_author-olga.avif)

IT Outsourcing Market Analyst & Software Engineering Editor

Software development enthusiast with 7 years of professional experience in the tech industry. Experienced in outsourcing market analysis, with a special focus on nearshoring. In the meantime, our expert in explaining tech, business, and digital topics in an accessible way. Writer and translator after hours.

![](https://cdn.prod.website-files.com/622fa4d65a5fab0c3465af07/6269298a07f958627bd9dc7e_author-matt.avif)

Chief Growth Officer

A serial entrepreneur, passionate R&D engineer, with 15 years of experience in the tech industry. Shares his expert knowledge about tech, startups, business development, and market analysis.

![](https://cdn.prod.website-files.com/622fa4d65a5fab0c3465af07/62692989e08e8651c846ce3f_author-olga.avif)

IT Outsourcing Market Analyst & Software Engineering Editor

Software development enthusiast with 7 years of professional experience in the tech industry. Experienced in outsourcing market analysis, with a special focus on nearshoring. In the meantime, our expert in explaining tech, business, and digital topics in an accessible way. Writer and translator after hours.

Read next

No items found...

**Popular this month**

previous article in this collection

next article in this collection
