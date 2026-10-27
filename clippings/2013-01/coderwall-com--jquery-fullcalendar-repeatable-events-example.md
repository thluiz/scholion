---
url: "https://coderwall.com/p/rti-rg"
captured_at: "2013-01-03T22:57:39-03:00"
title: "jQuey fullCalendar plugin and repeatable events and tasks (Example)"
domain: "coderwall-com"
---

**[fullCalendar](http://arshaw.com/fullcalendar/)** is amazing jQuey plugin to visually display and manage events and tasks. It allows you to use AJAX to fetch events/task on-the-fly and is easily configured to use your own feed format (an extension is provided for Google Calendar). It is visually customizable and exposes hooks for user-triggered events (like clicking or dragging an event). It is open source and dual licensed under the MIT or GPL Version 2 licenses.

To add events to the calendar, pass an [events source object](http://arshaw.com/fullcalendar/docs/event_data/Event_Source_Object/) to the plugin:

```
$('#calendar').fullCalendar({
    events: [
        {
            title  : 'event1',
            start  : '2012-01-01'
        },
        {
            title  : 'event2',
            start  : '2012-01-05',
            end    : '2012-01-07'
        },
        {
            title  : 'task',
            start  : '2012-01-09 12:30:00',
            allDay : false // will make the time show
        }
    ]
});
```

But what if you want to create a special infinitely repeatable event or task? Actually is straightforward to do. Just use an [event source function](http://arshaw.com/fullcalendar/docs/event_data/events_function/). Source function will dynamically create the desired repeatable event.

fullCalendar will call this event source function whenever it needs new event data. This is triggered when the user clicks prev/next or switches views.

This function will be given _start_ and _end_ parameters, which are **Date** objects denoting the range the calendar needs events for. It will also be given _callback_, a function that must be called when the custom event function has generated its events.

Now, let's create a repeatable event. It will be a every monday meeting at 10:00 am.

```
$('#calendar').fullCalendar( 'addEventSource',        
    function(start, end, callback) {
        // When requested, dynamically generate a
        // repeatable event for every monday.
        var events = [];
        var monday = 1;
        var one_day = (24 * 60 * 60 * 1000);

        for (loop = start.getTime();
             loop <= end.getTime();
             loop = loop + one_day) {

            var column_date = new Date(loop);

            if (column_date.getDay() == monday) {
                // we're in Moday, create the event
                events.push({
                    title: 'Morning Meeting',
                    start: new Date(column_date.setHours(10, 00)),
                    end: new Date(column_date.setHours(10, 40)),
                    allDay: false
                });
            }
        } // for loop

        // return events generated
        callback( events );
    }
);
```

#### Related protips:

[jQuery: When to use $(document).ready() and when $(window).load()  
](https://coderwall.com/p/_jothq/jquery-when-to-use-document-ready-and-when-window-load)
