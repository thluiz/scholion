---
title: "Ember Gotcha: Controllers Are Singletons"
date: '2014-06-30T10:02:05-03:00'
category: webclip
summary: 'The post explains that Ember controllers persist across route transitions, so controller state can leak between artists. The fix is to reset controller properties when the `artist` changes.'
tags: ["ember", "controllers", "route-transitions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ember gotcha: Controllers are singletons - Balint Erdi"
    url: "http://balinterdi.com/2014/06/26/ember-gotcha-controllers-are-singletons.html?utm_source=Ember+Weekly&utm_campaign=963a48fa79-Ember_Weekly_Issue_64&utm_medium=email&utm_term=0_e96229d21d-963a48fa79-99490097"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/balinterdi-com--ember-gotcha-controllers-are-singletons.md"
    kind: repo
---

The article describes a bug in an Ember app where starting song creation for one artist and then switching to another leaves the creation UI and partially entered title in place. The reason is that the same controller instance survives route changes, so unrelated controller state does not reset automatically.

## Reading notes

- Controllers in Ember are singletons and are not torn down when leaving a route.
- In the example, `songCreationStarted` stays true after moving from one artist to another.
- The route changes from one `ArtistSongsRoute` to another, but the same `ArtistSongsController` remains in use.
- Data bound to the `artist` property rerenders when the artist changes, but other controller properties stay as they were.
- `canCreateSong` depends on `songCreationStarted` or on existing songs.
- Because `songCreationStarted` stays true, the text input remains visible for the next artist.
- One fix is to reset controller properties in `setupController`.
- The author prefers resetting in the controller with an `artistDidChange` observer.
- The observer clears `newTitle` and sets `songCreationStarted` back to false when `artist` changes.
