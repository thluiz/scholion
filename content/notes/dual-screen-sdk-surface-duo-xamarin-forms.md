---
title: "Dual Screen SDK for Surface Duo with Xamarin.Forms"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The page shows XAML for a Xamarin.Forms dual-screen layout using TwoPaneView, a CarouselView for slide content, and a CollectionView of indicators wired to carousel selection.'
tags: ["xamarin-forms", "surface-duo", "dual-screen", "xaml"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dual Screen SDK for Surface Duo with Xamarin.Forms | Xamarin Blog"
    url: "https://web.archive.org/web/20200311045529id_/https://devblogs.microsoft.com/xamarin/xamarin-goes-dual-screen/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--dual-screen-sdk-surface-duo-xamarin-forms.md"
    kind: repo
---

The page presents a Xamarin.Forms layout built with TwoPaneView. One pane contains a CarouselView whose item template renders slide content, and the other pane contains a CollectionView used as indicators, with selection tied to carousel state.

## Reading notes

- The layout uses `local:TwoPaneView` as the root container.
- `CarouselView` is named `cv` and has a `PositionChanged` handler called `OnCarouselViewPositionChanged`.
- The carousel height is bound to `FormsWindow.Pane1.Height`.
- Each carousel item uses a `Frame` sized to the first pane and shows a centered label with `Slide Content {0}`.
- The `CollectionView` is named `indicators` and has a `SelectionChanged` handler called `OnIndicatorsSelectionChanged`.
- The indicators list uses single selection and binds its `ItemsSource` to `cv.ItemsSource`.
- A style sets the border color to green when a `Frame` enters the selected visual state.
- The indicators use a vertical `LinearItemsLayout` with `ItemSpacing` set to `10`.
- Each indicator item is a `Frame` with rounded corners and a horizontal `StackLayout`.
- The indicator template shows `Slide Content {0}` and `Slide {0}` in separate labels.
