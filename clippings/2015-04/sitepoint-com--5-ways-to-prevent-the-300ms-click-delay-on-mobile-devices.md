---
url: "http://www.sitepoint.com/5-ways-prevent-300ms-click-delay-mobile-devices/"
captured_at: "2015-04-02T19:33:11-03:00"
title: "5 Ways to Prevent the 300ms Click Delay on Mobile Devices"
domain: "sitepoint-com"
---

# 5 Ways to Prevent the 300ms Click Delay on Mobile Devices

Published January 8, 2014

Most touch-based mobile browsers wait 300ms between your tap on the screen and the browser firing the appropriate handler for that event. It was implemented because you could be double-tapping to zoom the page to full width. Therefore, the browser waits for a third of a second — if you don’t tap again, the “click” is activated.

The delay was a sensible precaution in the days before Responsive Web Design and multi-touch pinch zooming. Unfortunately, it’s now one of the primary reasons users consider web applications to be slower and less capable than native alternatives. So what can we do about the delay?

## 1. Don’t Fret About it

Whether the 300ms delay is a problem will largely depend on your application and target audience. For example, a content-only website with a standard navigation menu is unlikely to be adversely affected because users spend more time reading text than interacting with controls.

## 2. Disable Zooming (Chrome and Firefox)

Chrome and Firefox on Android will not wait for 300ms if zooming has been disabled using the following viewport setting in your HTML `head`:

|  |  |
| --- | --- |
|  | `<``meta` `name``=``"viewport"` `content``=``"width=device-width, user-scalable=no"``>` |

|  |  |
| --- | --- |
|  | `<``meta` `name``=``"viewport"` `content``=``"width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"``>` |

However, this solution fails on Safari and raises several accessibility concerns for those with visual or motor impairments. Fortunately, the vendors have begun to address that issue…

## 3. Set the viewport to the device-width (Chrome 32+)

In Chrome 32, setting the viewport width to anything less than or equal to the device-width will disable the double-tap zooming. You probably already have an appropriate setting in the HTML `head` of your responsive website, e.g.

|  |  |
| --- | --- |
|  | `<``meta` `name``=``"viewport"` `content``=``"width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=3"``>` |

## 4. Use PointerEvents (IE10+)

Microsoft has solved many touch-based issues in the [PointerEvents specification](https://dvcs.w3.org/hg/pointerevents/raw-file/tip/pointerEvents.html). For example, the `pointerup` event won’t be fired if the user is scrolling the page.

There is also a non-standard [CSS touch-action](http://msdn.microsoft.com/en-us/library/windows/apps/Hh767313.aspx) property which allows you to remove the delay on specific elements or the whole document without disabling pinch-zooming:

|  |  |
| --- | --- |
|  | `a, button, .myelements`  `{`  `-ms-touch-action: manipulation;` `/* IE10  */`  `touch-action: manipulation;` `/* IE11+ */`  `}` |

I hope other vendors adopt PointerEvents but don’t hold your breath.

## 5. Implement touchend Event Handlers

Unlike `click` and `touchstart`, `touchend` events are fired instantly without a 300ms delay. This may be practical if you’re developing a touch-only WebGL or canvas-based game, however, you cannot rely solely on `touchend` in standard web pages since:

1. A user firing `touchstart` on a different element to `touchend` should not fire the click.
2. A user firing `touchstart` then a *reasonably large* `touchmove` before the `touchend` event is scrolling — a click should not be fired.
3. You still require standard `click` handlers for those using non-touch devices — but be wary about firing the same event twice.

There’s a lot to contend with but the hard work’s been done for us:

- [**FastClick**](https://github.com/ftlabs/fastclick) from FT Labs attaches appropriate listeners on mobile browsers when they’re required, i.e. solutions 2 to 4 above have not been used. The script compresses to around 10Kb.
- [**Tappy!**](https://github.com/filamentgroup/tappy/) from the Filament Group is a normalized tap event library, similar in concept to PointerEvents, which compresses to 1Kb.

Be warned that adding event handlers to multiple elements will have a negative impact on performance. It may be worse than the 300ms delay problem you’re attempting to solve.

## An Optimal Solution?

The situation is a mess and it’s not easy for developers to build a cross-browser solution. I’m not convinced it’s something we need to solve in every application since it’s a browser-specific policy which should be addressed by vendors.

Setting the viewport width to device-width is the easiest option since you’ve probably done it already. It won’t work until Chrome 32 is released but Opera, Firefox and possibly IE will follow. I’d hope to see it in Webkit but it could take several years before the many millions of iPhone and iPad users receive it.

There’s little harm adding `touch-action: manipulation;` properties to CSS — it’ll degrade gracefully. Had PointerEvents been devised by anyone other than Microsoft, I’m sure the remaining vendors would have followed immediately. It is a W3C specification and part of the [HTML5test](http://html5test.com/) so perhaps we won’t need to wait too much longer.

If you’re only concerned about a handful of links or buttons, your own custom `touchend` handlers may be effective. For everything else, it’s worth considering [FastClick](https://github.com/ftlabs/fastclick).
