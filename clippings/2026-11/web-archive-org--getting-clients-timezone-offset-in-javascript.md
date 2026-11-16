---
url: "https://web.archive.org/web/20200618140323id_/https://stackoverflow.com/questions/1091372/getting-the-clients-timezone-offset-in-javascript"
captured_at: "2026-11-16T08:07:01+00:00"
title: "Getting the client's timezone offset in JavaScript"
domain: "web-archive-org"
---

620

[](https://web.archive.org/posts/1091372/timeline "Show activity on this post.")

How can I gather the visitor's time zone information? I need the Timezone, as well as the GMT offset hours.

[

![](https://www.gravatar.com/avatar/90fd9ad4efef8eb93209f42183c48f3e?s=32&d=identicon&r=PG)

](https://web.archive.org/users/1235698/marcin-orlowski)

asked Jul 7 '09 at 9:48

[

![](https://www.gravatar.com/avatar/d6135480e3e6f86ab79632e0acaf8bed?s=32&d=identicon&r=PG)

](https://web.archive.org/users/131055/%c3%81rv%c3%adzt%c5%b1r%c5%91-t%c3%bck%c3%b6rf%c3%bar%c3%b3g%c3%a9p)

595

0

[](https://web.archive.org/posts/1091399/timeline "Show activity on this post.")

```
var offset = new Date().getTimezoneOffset();
console.log(offset);
```

> The time-zone offset is the difference, in minutes, between UTC and local time. Note that this means that the offset is positive if the local timezone is behind UTC and negative if it is ahead. For example, if your time zone is UTC+10 (Australian Eastern Standard Time), -600 will be returned. Daylight savings time prevents this value from being a constant even for a given locale

*   [Mozilla Date Object reference](https://developer.mozilla.org/en/Core_JavaScript_1.5_Reference/Global_Objects/Date/getTimezoneOffset)

Note that not all timezones are offset by whole hours: for example, Newfoundland is UTC minus 3h 30m (leaving Daylight Saving Time out of the equation).

[

![](https://www.gravatar.com/avatar/221feed0632157f764f50f3c087c5d38?s=32&d=identicon&r=PG)

](https://web.archive.org/users/6999690/ruslan-l%c3%b3pez)

[Ruslan López](https://web.archive.org/users/6999690/ruslan-l%c3%b3pez)

3,8281 gold badge18 silver badges29 bronze badges

answered Jul 7 '09 at 9:53

[

![](https://www.gravatar.com/avatar/b09e3490d1406cd1d752c774f9d5e711?s=32&d=identicon&r=PG)

](https://web.archive.org/users/16782/nickfitz)

487

0

[](https://web.archive.org/posts/34602679/timeline "Show activity on this post.")

Using an offset to calculate Timezone is a wrong approach, and you will always encounter problems. Time zones and daylight saving rules may change on several occasions during a year, and It's difficult to keep up with changes.

To get the system's [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) in JavaScript, you should use

```
console.log(Intl.DateTimeFormat().resolvedOptions().timeZone)
```

## As of September 2019, this [works in 95% of the browsers used globally](http://caniuse.com/#search=Intl).

### Old compatibility information

ecma-402/1.0 says that `timeZone` may be undefined if not provided to constructor. However, future draft (3.0) fixed that issue by changing to system default timezone.

> **In this version of the ECMAScript Internationalization API, the `timeZone` property will remain undefined if no `timeZone` property was provided in the options object provided to the `Intl.DateTimeFormat` constructor**. However, applications should not rely on this, as future versions may return a String value identifying the host environment’s current time zone instead.

in ecma-402/3.0 which is still in a draft it changed to

> In this version of the ECMAScript 2015 Internationalization API, the `timeZone` property will be the name of the default time zone if no `timeZone` property was provided in the options object provided to the `Intl.DateTimeFormat` constructor. The previous version left the `timeZone` property undefined in this case.

[

![](https://www.gravatar.com/avatar/23fc4556be14017796d38579dd4778ab?s=32&d=identicon&r=PG)

](https://web.archive.org/users/123671/mikemaccana)

[mikemaccana](https://web.archive.org/users/123671/mikemaccana)

70.1k58 gold badges280 silver badges354 bronze badges

answered Jan 5 '16 at 1:07

[

![](https://www.gravatar.com/avatar/d1ec450e05f4d167ad0c200956ece265?s=32&d=identicon&r=PG&f=1)

](https://web.archive.org/users/706466/pawel-dubiel)

[Pawel Dubiel](https://web.archive.org/users/706466/pawel-dubiel)Pawel Dubiel

11.4k3 gold badges35 silver badges54 bronze badges

123

0

[](https://web.archive.org/posts/15304657/timeline "Show activity on this post.")

I realize this answer is a bit off topic but I imagine many of us looking for an answer also wanted to format the time zone for display and perhaps get the zone abbreviation too. So here it goes...

If you want the client timezone nicely formatted you can rely on the JavaScript Date.toString method and do:

```
var split = new Date().toString().split(" ");
var timeZoneFormatted = split[split.length - 2] + " " + split[split.length - 1];
```

This will give you "GMT-0400 (EST)" for example, including the timezone minutes when applicable.

Alternatively, with regex you can extract any desired part:

For "GMT-0400 (EDT)" :

```
new Date().toString().match(/([A-Z]+[\+-][0-9]+.*)/)[1]
```

For "GMT-0400" :

```
new Date().toString().match(/([A-Z]+[\+-][0-9]+)/)[1]
```

For just "EDT" :

```
new Date().toString().match(/\(([A-Za-z\s].*)\)/)[1]
```

For just "-0400":

```
new Date().toString().match(/([-\+][0-9]+)\s/)[1]
```

Date.toString reference: [https://developer.mozilla.org/en/JavaScript/Reference/Global\_Objects/Date/toString](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Date/toString)

answered Mar 8 '13 at 22:50

[

![](https://www.gravatar.com/avatar/42f8ee3a69ff7ae402514a8332b04c6b?s=32&d=identicon&r=PG)

](https://web.archive.org/users/927737/marquez)

[Marquez](https://web.archive.org/users/927737/marquez)Marquez

4,8123 gold badges23 silver badges32 bronze badges

71

0

[](https://web.archive.org/posts/5114625/timeline "Show activity on this post.")

It's already been answered how to get offset in minutes as an integer, but in case anyone wants the local GMT offset as a string e.g. `"+1130"`:

```
function pad(number, length){
    var str = "" + number
    while (str.length < length) {
        str = '0'+str
    }
    return str
}

var offset = new Date().getTimezoneOffset()
offset = ((offset<0? '+':'-')+ // Note the reversed sign!
          pad(parseInt(Math.abs(offset/60)), 2)+
          pad(Math.abs(offset%60), 2))
```

answered Feb 25 '11 at 7:17

[

![](https://www.gravatar.com/avatar/38e5b8aa19ef92d3309ec3f64d816de2?s=32&d=identicon&r=PG)

](https://web.archive.org/users/304185/cryo)

[cryo](https://web.archive.org/users/304185/cryo)cryo

12.2k4 gold badges28 silver badges33 bronze badges

67

0

[](https://web.archive.org/posts/40435316/timeline "Show activity on this post.")

You can use:

## moment-timezone

```
<script src="moment.js"></script>
<script src="moment-timezone-with-data.js"></script>

// retrieve timezone by name (i.e. "America/Chicago")
moment.tz.guess();
```

Browser time zone detection is rather tricky to get right, as there is little information provided by the browser.

Moment Timezone uses `Date.getTimezoneOffset()` and `Date.toString()` on a handful of moments around the current year to gather as much information about the browser environment as possible. It then compares that information with all the time zone data loaded and returns the closest match. In case of ties, the time zone with the city with largest population is returned.

```
console.log(moment.tz.guess()); // America/Chicago
```

[

![](https://www.gravatar.com/avatar/185aae2d842026d2eefa7528b00b394b?s=32&d=identicon&r=PG)

](https://web.archive.org/users/212378/alexis-wilke)

[Alexis Wilke](https://web.archive.org/users/212378/alexis-wilke)

13.6k6 gold badges50 silver badges94 bronze badges

answered Nov 5 '16 at 6:09

[

![](https://graph.facebook.com/944988695541509/picture?type=large)

](https://web.archive.org/users/4630756/sameer-ek)

[Sameer Ek](https://web.archive.org/users/4630756/sameer-ek)Sameer Ek

9056 silver badges13 bronze badges

43

0

[](https://web.archive.org/posts/30377368/timeline "Show activity on this post.")

I wrote a function in my project, which returns the timezone in `hh:mm` format. I hope this may help someone:

```
function getTimeZone() {
    var offset = new Date().getTimezoneOffset(), o = Math.abs(offset);
    return (offset < 0 ? "+" : "-") + ("00" + Math.floor(o / 60)).slice(-2) + ":" + ("00" + (o % 60)).slice(-2);
}
```

* * *

```
// Outputs: +5:00
```

**[Working Fiddle](http://jsfiddle.net/agzknz9L/)**

answered May 21 '15 at 14:55

[

![](https://www.gravatar.com/avatar/ef7a7186e7dce93cbcb3d6ee049d79cc?s=32&d=identicon&r=PG)

](https://web.archive.org/users/1577396/mr-green)

[Mr\_Green](https://web.archive.org/users/1577396/mr-green)Mr\_Green

34k38 gold badges135 silver badges228 bronze badges

15

0

[](https://web.archive.org/posts/55204472/timeline "Show activity on this post.")

A one-liner that gives both the offset and the time zone is to simply call [toTimeString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString) on a new Date object. From MDN:

> The `toTimeString()` method returns the time portion of a Date object in human readable form in American English.

The catch is that the timezone is not in the standard IANA format; it's somewhat more user-friendly, than the "continent/city" [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format. Try it out:

```
console.log(new Date().toTimeString().slice(9));
console.log(Intl.DateTimeFormat().resolvedOptions().timeZone);
console.log(new Date().getTimezoneOffset() / -60);
```

In California right now, `toTimeString()` returns `Pacific Daylight Time` while the Intl API returns `America/Los_Angeles`. In Colombia, you'd get `Colombia Standard Time`, vs. `America/Bogota`.

Note that many other answers to this question attempt to obtain the same information by calling Date.toString(). That approach is not that reliable, as [MDN explains](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString#Description):

> Date instances refer to a specific point in time. Calling toString() will return the date formatted in a human readable form in American English. \[...\] Sometimes it is desirable to obtain a string of the time portion; such a thing can be accomplished with the `toTimeString()` method.
> 
> The `toTimeString()` method is especially useful because compliant engines implementing ECMA-262 may differ in the string obtained from `toString()` for `Date` objects, as the format is implementation-dependent; simple string slicing approaches may not produce consistent results across multiple engines.

answered Mar 17 '19 at 6:36

[

![](https://i.stack.imgur.com/Os16n.jpg?s=32&g=1)

](https://web.archive.org/users/1269037/dan-dascalescu)

[Dan Dascalescu](https://web.archive.org/users/1269037/dan-dascalescu)Dan Dascalescu

93.4k33 gold badges259 silver badges320 bronze badges

13

0

[](https://web.archive.org/posts/1091387/timeline "Show activity on this post.")

try `getTimezoneOffset()` of the `Date` object:

```
var curdate = new Date()
var offset = curdate.getTimezoneOffset()
```

This method returns time zone offset in minutes which is the difference between GMT and local time in minutes.

[

![](https://www.gravatar.com/avatar/c5b57a2e31a8167f66f1a2fa64a01c26?s=32&d=identicon&r=PG)

](https://web.archive.org/users/744298/jchavannes)

answered Jul 7 '09 at 9:51

[

![](https://i.stack.imgur.com/DVUwx.jpg?s=32&g=1)

](https://web.archive.org/users/89266/dfa)

[dfa](https://web.archive.org/users/89266/dfa)dfa

103k28 gold badges183 silver badges220 bronze badges

9

0

[](https://web.archive.org/posts/37821282/timeline "Show activity on this post.")

JavaScript:

```
var d = new Date();
var n = d.getTimezoneOffset();
var timezone = n / -60;
console.log(timezone);
```

answered Jun 14 '16 at 20:14

[

![](https://lh6.googleusercontent.com/-SwMlFpyUAes/AAAAAAAAAAI/AAAAAAAAABo/lzdh16_dNNg/photo.jpg?sz=32)

](https://web.archive.org/users/6316770/%d8%b2%d9%8a%d8%a7%d8%af)

[زياد](https://web.archive.org/users/6316770/%d8%b2%d9%8a%d8%a7%d8%af)زياد

6807 silver badges10 bronze badges

7

0

[](https://web.archive.org/posts/24695635/timeline "Show activity on this post.")

With [moment.js](http://momentjs.com/):

```
moment().format('zz');
```

answered Jul 11 '14 at 10:30

[

![](https://www.gravatar.com/avatar/7890c1ec354236e430753556632f5b1b?s=32&d=identicon&r=PG)

](https://web.archive.org/users/134904/kolypto)

[kolypto](https://web.archive.org/users/134904/kolypto)kolypto

20.1k13 gold badges62 silver badges66 bronze badges

6

0

[](https://web.archive.org/posts/31390326/timeline "Show activity on this post.")

With [momentjs](https://web.archive.org/questions/tagged/momentjs "show questions tagged 'momentjs'"), you can find current timezone as

```
console.log(moment().utcOffset()); // (-240, -120, -60, 0, 60, 120, 240, etc.)
```

```
<script src="https://cdn.jsdelivr.net/momentjs/2.13.0/moment.min.js"></script>
```

* * *

With [dayjs](https://web.archive.org/questions/tagged/dayjs "show questions tagged 'dayjs'"), you can find current timezone as

```
console.log(dayjs().utcOffset()); // (-240, -120, -60, 0, 60, 120, 240, etc.)
```

```
<script src="https://unpkg.com/dayjs@1.8.10/dayjs.min.js"></script>
```

Both API returns utc offset in minutes.

*   [moment Doc](http://momentjs.com/docs/#/manipulating/utc-offset/)
*   [Dayjs Doc](https://github.com/iamkun/dayjs/blob/dev/docs/en/API-reference.md#utc-offset-minutes-utcoffset)

answered Jul 13 '15 at 18:02

[

![](https://i.stack.imgur.com/baIRy.jpg?s=32&g=1)

](https://web.archive.org/users/1154350/fizer-khan)

[Fizer Khan](https://web.archive.org/users/1154350/fizer-khan)Fizer Khan

64.1k25 gold badges128 silver badges143 bronze badges

4

0

[](https://web.archive.org/posts/42639871/timeline "Show activity on this post.")

Timezone in hours-

```
var offset = new Date().getTimezoneOffset();
if(offset<0)
    console.log( "Your timezone is- GMT+" + (offset/-60));
else
    console.log( "Your timezone is- GMT-" + offset/60);
```

If you want to be precise as you mentioned in comment, then you should try like this-

```
var offset = new Date().getTimezoneOffset();

if(offset<0)
{
    var extraZero = "";
    if(-offset%60<10)
      extraZero="0";

    console.log( "Your timezone is- GMT+" + Math.ceil(offset/-60)+":"+extraZero+(-offset%60));
}
else
{
    var extraZero = "";
    if(offset%60<10)
      extraZero="0";

    console.log( "Your timezone is- GMT-" + Math.floor(offset/60)+":"+extraZero+(offset%60));
}
```

answered Mar 7 '17 at 3:52

[

![](https://i.stack.imgur.com/mhLWP.jpg?s=32&g=1)

](https://web.archive.org/users/2193439/abrar-jahin)

[Abrar Jahin](https://web.archive.org/users/2193439/abrar-jahin)Abrar Jahin

10.6k17 gold badges83 silver badges133 bronze badges

3

0

[](https://web.archive.org/posts/41581138/timeline "Show activity on this post.")

If all you need is the "MST" or the "EST" time zone abbreviation:

```
function getTimeZone(){
    var now = new Date().toString();
    var timeZone = now.replace(/.*[(](.*)[)].*/,'$1');//extracts the content between parenthesis
    return timeZone;
}
```

answered Jan 11 '17 at 1:04

[

![](https://www.gravatar.com/avatar/2ef7db6a67ae411e322b4bffbb851598?s=32&d=identicon&r=PG)

](https://web.archive.org/users/1691651/johnp2)

[JohnP2](https://web.archive.org/users/1691651/johnp2)JohnP2

9858 silver badges11 bronze badges

3

0

[](https://web.archive.org/posts/45169182/timeline "Show activity on this post.")

See this resultant operator was opposite to the Timezone .So apply some math function then validate the num less or more.

[![enter image description here](https://i.stack.imgur.com/9wCMJ.png)](https://i.stack.imgur.com/9wCMJ.png)

[**See the MDN document**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)

```
var a = new Date().getTimezoneOffset();

var res = -Math.round(a/60)+':'+-(a%60);
res = res < 0 ?res : '+'+res;

console.log(res)
```

answered Jul 18 '17 at 14:07

[

![](https://i.stack.imgur.com/ilJRk.png?s=32&g=1)

](https://web.archive.org/users/6235047/prasanth)

[prasanth](https://web.archive.org/users/6235047/prasanth)prasanth

17.8k3 gold badges20 silver badges45 bronze badges

3

0

[](https://web.archive.org/posts/50969044/timeline "Show activity on this post.")

```
function getLocalTimeZone() {
    var dd = new Date();
    var ddStr = dd.toString();
    var ddArr = ddStr.split(' ');
    var tmznSTr = ddArr[5];
    tmznSTr = tmznSTr.substring(3, tmznSTr.length);
    return tmznSTr;
}
```

Example : Thu Jun 21 2018 18:12:50 GMT+0530 (India Standard Time)

O/P : +0530

answered Jun 21 '18 at 12:51

[

![](https://graph.facebook.com/100001805818937/picture?type=large)

](https://web.archive.org/users/2870623/chandrakanth-gowda)

3

0

[](https://web.archive.org/posts/55418517/timeline "Show activity on this post.")

Try this,

```
new Date().toString().split("GMT")[1].split(" (")[0]
```

answered Mar 29 '19 at 13:28

[

![](https://lh3.googleusercontent.com/-1b6CwyFl9mo/AAAAAAAAAAI/AAAAAAAAACE/0Cs9zHNFI8g/photo.jpg?sz=32)

](https://web.archive.org/users/4393627/srinivasan-sekar)

2

0

[](https://web.archive.org/posts/30412924/timeline "Show activity on this post.")

This value is from user's machine and it can be changed anytime so I think it doesn't matter, I just want to get an approximate value and then convert it to GMT in my server.

For example, I am from Taiwan and it returns "+8" for me.

[Working example](https://jsfiddle.net/9maczqyy/3/)

**JS**

```
function timezone() {
    var offset = new Date().getTimezoneOffset();
    var minutes = Math.abs(offset);
    var hours = Math.floor(minutes / 60);
    var prefix = offset < 0 ? "+" : "-";
    return prefix+hours;
}


$('#result').html(timezone());
```

**HTML**

```
<div id="result"></div>
```

**Result**

```
+8
```

answered May 23 '15 at 12:55

[

![](https://www.gravatar.com/avatar/2dd912088ae45f2693789b6c9f105763?s=32&d=identicon&r=PG)

](https://web.archive.org/users/1839495/terry-lin)

[Terry Lin](https://web.archive.org/users/1839495/terry-lin)Terry Lin

1,94914 silver badges19 bronze badges

2

0

[](https://web.archive.org/posts/50236918/timeline "Show activity on this post.")

On the `new Date(`) you can get the offset, to get the timezone name you may do:

`new Date().toString().replace(/(.*\((.*)\).*)/, '$2');`

you get the value between `()` in the end of the date, that is the name of the timezone.

[

![](https://www.gravatar.com/avatar/ff0dec229b9e82a5a37420bdbcef6266?s=32&d=identicon&r=PG&f=1)

](https://web.archive.org/users/3411556/alamoot)

[alamoot](https://web.archive.org/users/3411556/alamoot)

1,2854 gold badges20 silver badges33 bronze badges

answered May 8 '18 at 15:13

[

![](https://www.gravatar.com/avatar/53e49c54de568b11098b7b29032352d5?s=32&d=identicon&r=PG&f=1)

](https://web.archive.org/users/4901213/moys%c3%a9s-lacerda)

2

0

[](https://web.archive.org/posts/58963540/timeline "Show activity on this post.")

This would be my solution:

```


    // For time zone:
    const timeZone = /\((.*)\)/.exec(new Date().toString())[1];
    
    // Offset hours:
    const offsetHours = new Date().getTimezoneOffset() / 60;
    
    console.log(`${timeZone}, ${offsetHours}hrs`);



```

answered Nov 20 '19 at 21:18

[

![](https://lh5.googleusercontent.com/-HUdBCST0fFA/AAAAAAAAAAI/AAAAAAAAEhc/PlU_jVGfcHE/photo.jpg?sz=32)

](https://web.archive.org/users/9737567/abhish-abraham)

1

0

[](https://web.archive.org/posts/30758146/timeline "Show activity on this post.")

As an alternative to `new Date().getTimezoneOffset()` and `moment().format('zz')`, you can also use [momentjs](https://web.archive.org/questions/tagged/momentjs "show questions tagged 'momentjs'"):

```
var offset = moment.parseZone(Date.now()).utcOffset() / 60
console.log(offset);
```

```
<script src="https://cdn.jsdelivr.net/momentjs/2.13.0/moment.min.js"></script>
```

jstimezone is also quite buggy and unmaintained ([https://bitbucket.org/pellepim/jstimezonedetect/issues?status=new&status=open](https://bitbucket.org/pellepim/jstimezonedetect/issues?status=new&status=open))

[

![](https://www.gravatar.com/avatar/221feed0632157f764f50f3c087c5d38?s=32&d=identicon&r=PG)

](https://web.archive.org/users/6999690/ruslan-l%c3%b3pez)

[Ruslan López](https://web.archive.org/users/6999690/ruslan-l%c3%b3pez)

3,8281 gold badge18 silver badges29 bronze badges

answered Jun 10 '15 at 13:42

[

![](https://www.gravatar.com/avatar/cd3fcb7a417c8acb989fc320b604a2a8?s=32&d=identicon&r=PG)

](https://web.archive.org/users/670229/brauliobo)

[brauliobo](https://web.archive.org/users/670229/brauliobo)brauliobo

4,0184 gold badges23 silver badges31 bronze badges

1

0

[](https://web.archive.org/posts/42994392/timeline "Show activity on this post.")

Use this to convert OffSet to postive:

```
var offset = new Date().getTimezoneOffset();
console.log(offset);
this.timeOffSet = offset + (-2*offset);
console.log(this.timeOffSet);
```

answered Mar 24 '17 at 8:09

[

![](https://graph.facebook.com/10208442126798178/picture?type=large)

](https://web.archive.org/users/6333529/kumal-pereira)

\-2

0

[](https://web.archive.org/posts/36027773/timeline "Show activity on this post.")

I was looking for just the 3 letter string (like "PDT") and tried Marquez's answer but had to tweak it a bit for cross browser support. Luckily, the string is the last potential match :)

Here's what I did, in CoffeeScript:

```
browserTimezone = ->
  userDate = new Date()
  zoneMatches = userDate.toString().match(/([A-Z][A-Z][A-Z])/g)
  userZone = zoneMatches[zoneMatches.length - 1]
```

Works in IE8, IE9, Safari 9, Firefox 44, and Chrome 48

answered Mar 16 '16 at 5:54

[

![](https://i.stack.imgur.com/MCrk0.jpg?s=32&g=1)

](https://web.archive.org/users/1116825/ari-gold)

[ari gold](https://web.archive.org/users/1116825/ari-gold)ari gold

1,8263 gold badges23 silver badges46 bronze badges

\-3

0

[](https://web.archive.org/posts/41224326/timeline "Show activity on this post.")

You just to to include moment.js and jstz.js

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.6/jstz.min.js"></script>
```

and after that

```
<script>
$(function(){
 var currentTimezone = jstz.determine();
 var timezone = currentTimezone.name();
 alert(timezone);
});

</script>
```

answered Dec 19 '16 at 14:04

[

![](https://i.stack.imgur.com/6XVRh.jpg?s=32&g=1)

](https://web.archive.org/users/7194235/dayachand-patel)

\-3

0

[](https://web.archive.org/posts/43576520/timeline "Show activity on this post.")

This is very good work for me:

```
// Translation to offset in Unix Timestamp
let timeZoneOffset = ((new Date().getTimezoneOffset())/60)*3600;
```

answered Apr 23 '17 at 21:08

[

![](https://i.stack.imgur.com/GAlWx.jpg?s=32&g=1)

](https://web.archive.org/users/5716979/alexander)

\-4

0

[](https://web.archive.org/posts/44187148/timeline "Show activity on this post.")

you can simply try this. it will return you current machine time

> `var _d = new Date(), t = 0, d = new Date(t*1000 + _d.getTime())`

answered May 25 '17 at 18:10

[

![](https://www.gravatar.com/avatar/ae57f9af73e167ead750ee770902f6a7?s=32&d=identicon&r=PG&f=1)

](https://web.archive.org/users/8066707/user8066707)

\-4

0

[](https://web.archive.org/posts/44187578/timeline "Show activity on this post.")

This will do the job.

* * *

```
var time = new Date(),
timestamp = Date(1000 + time.getTime());
console.log(timestamp);
```

* * *

```
Thu May 25 2017 21:35:14 GMT+0300 (IDT)
```

undefined

answered May 25 '17 at 18:35

[

![](https://i.stack.imgur.com/lRJ4k.png?s=32&g=1)

](https://web.archive.org/users/6801045/sysmurff)

[SysMurff](https://web.archive.org/users/6801045/sysmurff)SysMurff

1321 silver badge13 bronze badges

## Not the answer you're looking for? Browse other questions tagged [javascript](https://web.archive.org/questions/tagged/javascript "show questions tagged 'javascript'") [timezone](https://web.archive.org/questions/tagged/timezone "show questions tagged 'timezone'") or [ask your own question](https://web.archive.org/questions/ask).
