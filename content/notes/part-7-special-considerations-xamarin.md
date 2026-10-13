---
title: "Part 7 - Special Considerations"
date: '2013-08-05T13:52:35-03:00'
category: webclip
summary: 'The page advises against dynamic code generation in shared code and against reusing the same UI design across iOS, Android, and Windows Phone. Xamarin apps should follow each platform’s native constraints and familiar UI metaphors.'
tags: ["xamarin", "cross-platform", "code-generation", "user-interface"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 7 - Special Considerations | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_7_-_special_considerations"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-7-special-considerations-xamarin.md"
    kind: repo
---

The page warns that shared code should avoid dynamic code generation with System.Reflection.Emit because it does not work across all products. It also notes that Apple’s kernel blocks on-the-fly code generation on iPhone and iPad, so Xamarin.iOS cannot use it, and that Dynamic Language Runtime features are not usable with Xamarin tools. Some reflection features still work, but not code generation.

It also advises against reusing the same user interface design across iOS, Android, and Windows Phone without adapting it for each platform. Xamarin’s strength is native UI on each platform, so the examples given are to avoid putting a "Back" button into Android or Windows Phone apps and to avoid an iOS tab control with tabs across the top of the screen.

## Reading notes

- Avoid dynamic code generation in shared code, including System.Reflection.Emit, because it is not supported across all Xamarin products.
- Apple blocks on-the-fly code generation on iPhone and iPad, so Xamarin.iOS cannot use it.
- Dynamic Language Runtime features cannot be used with Xamarin tools.
- Some reflection features still work, but not code generation.
- Do not reuse the same UI design across iOS, Android, and Windows Phone without platform-specific adjustments.
- Use the native UI metaphors users expect on each platform.
