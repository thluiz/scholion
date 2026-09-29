---
url: "https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1"
captured_at: "2022-05-30T16:10:26-03:00"
title: "Resources for F# Onboarding"
domain: "gist-github-com"
---

[Skip to content](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1#start-of-content)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='24' viewBox='0 0 16 16' version='1.1' width='24' data-view-component='true' class='octicon octicon-mark-github v-align-middle d-inline-block d-md-none js-evernote-checked' data-evernote-id='169'%3e %3cpath fill-rule='evenodd' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z' data-evernote-id='490' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='24' viewBox='0 0 45 16' version='1.1' width='67' data-view-component='true' class='octicon octicon-logo-github v-align-middle d-none d-md-inline-block js-evernote-checked' data-evernote-id='170'%3e %3cpath fill-rule='evenodd' d='M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 00-.146-.18zM42.23 9.84c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61h-2.1c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z' data-evernote-id='491' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='24' viewBox='0 0 25 16' version='1.1' width='37' data-view-component='true' class='octicon octicon-logo-gist v-align-middle d-none d-md-inline-block js-evernote-checked' data-evernote-id='171'%3e %3cpath fill-rule='evenodd' d='M4.7 8.73h2.45v4.02c-.55.27-1.64.34-2.53.34-2.56 0-3.47-2.2-3.47-5.05 0-2.85.91-5.06 3.48-5.06 1.28 0 2.06.23 3.28.73V2.66C7.27 2.33 6.25 2 4.63 2 1.13 2 0 4.69 0 8.03c0 3.34 1.11 6.03 4.63 6.03 1.64 0 2.81-.27 3.59-.64V7.73H4.7v1zm6.39 3.72V6.06h-1.05v6.28c0 1.25.58 1.72 1.72 1.72v-.89c-.48 0-.67-.16-.67-.7v-.02zm.25-8.72c0-.44-.33-.78-.78-.78s-.77.34-.77.78.33.78.77.78.78-.34.78-.78zm4.34 5.69c-1.5-.13-1.78-.48-1.78-1.17 0-.77.33-1.34 1.88-1.34 1.05 0 1.66.16 2.27.36v-.94c-.69-.3-1.52-.39-2.25-.39-2.2 0-2.92 1.2-2.92 2.31 0 1.08.47 1.88 2.73 2.08 1.55.13 1.77.63 1.77 1.34 0 .73-.44 1.42-2.06 1.42-1.11 0-1.86-.19-2.33-.36v.94c.5.2 1.58.39 2.33.39 2.38 0 3.14-1.2 3.14-2.41 0-1.28-.53-2.03-2.75-2.23h-.03zm8.58-2.47v-.86h-2.42v-2.5l-1.08.31v2.11l-1.56.44v.48h1.56v5c0 1.53 1.19 2.13 2.5 2.13.19 0 .52-.02.69-.05v-.89c-.19.03-.41.03-.61.03-.97 0-1.5-.39-1.5-1.34V6.94h2.42v.02-.01z' data-evernote-id='492' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://gist.github.com/)

[All gists](https://gist.github.com/discover)
[Back to GitHub](https://github.com/)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-bell js-evernote-checked' data-evernote-id='177'%3e %3cpath d='M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z' data-evernote-id='508' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill-rule='evenodd' d='M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z' data-evernote-id='509' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
You have unread notifications](https://github.com/notifications)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-plus d-md-none js-evernote-checked' data-evernote-id='178'%3e %3cpath fill-rule='evenodd' d='M7.75 2a.75.75 0 01.75.75V7h4.25a.75.75 0 110 1.5H8.5v4.25a.75.75 0 11-1.5 0V8.5H2.75a.75.75 0 010-1.5H7V2.75A.75.75 0 017.75 2z' data-evernote-id='511' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-plus d-none d-md-inline-block js-evernote-checked' data-evernote-id='179'%3e %3cpath fill-rule='evenodd' d='M7.75 2a.75.75 0 01.75.75V7h4.25a.75.75 0 110 1.5H8.5v4.25a.75.75 0 11-1.5 0V8.5H2.75a.75.75 0 010-1.5H7V2.75A.75.75 0 017.75 2z' data-evernote-id='512' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://gist.github.com/)

![362263](gist-github-com--resources-for-f-sharp-onboarding/f5426f79658f3433dfc76cb2ce926536.png)

[![11332444](gist-github-com--resources-for-f-sharp-onboarding/9390d9b6e45ba30539b02b17f9e3baa6.jpg)](https://gist.github.com/natalie-o-perret)

# [natalie-o-perret](https://gist.github.com/natalie-o-perret)/**[README.md](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1)**

Last active 3 hours ago
•
[Report abuse](https://gist.github.com/contact/report-content?content_url=https%3A%2F%2Fgist.github.com%2F19bf6e1e9d48a493919b78aa0bc7cdd1&report=natalie-o-perret+%28user%29)

- [55](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/stargazers)
- [3](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/forks)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-code UnderlineNav-octicon js-evernote-checked' data-evernote-id='217'%3e %3cpath fill-rule='evenodd' d='M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z' data-evernote-id='846' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Code](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1)
[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-git-commit js-evernote-checked' data-evernote-id='218'%3e %3cpath fill-rule='evenodd' d='M10.5 7.75a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zm1.43.75a4.002 4.002 0 01-7.86 0H.75a.75.75 0 110-1.5h3.32a4.001 4.001 0 017.86 0h3.32a.75.75 0 110 1.5h-3.32z' data-evernote-id='847' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Revisions
5](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/revisions)
[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-star js-evernote-checked' data-evernote-id='219'%3e %3cpath fill-rule='evenodd' d='M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z' data-evernote-id='849' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Stars
55](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/stargazers)
[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-git-branch js-evernote-checked' data-evernote-id='220'%3e %3cpath fill-rule='evenodd' d='M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z' data-evernote-id='851' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Forks
3](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/forks)

Embed

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-copy js-evernote-checked' data-evernote-id='226'%3e %3cpath fill-rule='evenodd' d='M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z' data-evernote-id='885' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill-rule='evenodd' d='M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z' data-evernote-id='886' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-desktop-download js-evernote-checked' data-evernote-id='227'%3e %3cpath d='M4.927 5.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 5H8.75V.75a.75.75 0 10-1.5 0V5H5.104a.25.25 0 00-.177.427z' data-evernote-id='888' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M1.573 2.573a.25.25 0 00-.073.177v7.5a.25.25 0 00.25.25h12.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-3a.75.75 0 110-1.5h3A1.75 1.75 0 0116 2.75v7.5A1.75 1.75 0 0114.25 12h-3.727c.099 1.041.52 1.872 1.292 2.757A.75.75 0 0111.25 16h-6.5a.75.75 0 01-.565-1.243c.772-.885 1.192-1.716 1.292-2.757H1.75A1.75 1.75 0 010 10.25v-7.5A1.75 1.75 0 011.75 1h3a.75.75 0 010 1.5h-3a.25.25 0 00-.177.073zM6.982 12a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5H6.982z' data-evernote-id='889' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)Save natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1 to your computer and use it in GitHub Desktop.](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1x-github-client://openRepo/https://gist.github.com/19bf6e1e9d48a493919b78aa0bc7cdd1)

[Download ZIP](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/archive/fa5449391947986eb6c5fe5fd0fa187eedcd1e95.zip)

Resources for F# Onboarding

[Raw](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1/raw/fa5449391947986eb6c5fe5fd0fa187eedcd1e95/README.md)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-code-square color-fg-muted js-evernote-checked' data-evernote-id='228'%3e %3cpath fill-rule='evenodd' d='M1.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V1.75a.25.25 0 00-.25-.25H1.75zM0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0114.25 16H1.75A1.75 1.75 0 010 14.25V1.75zm9.22 3.72a.75.75 0 000 1.06L10.69 8 9.22 9.47a.75.75 0 101.06 1.06l2-2a.75.75 0 000-1.06l-2-2a.75.75 0 00-1.06 0zM6.78 6.53a.75.75 0 00-1.06-1.06l-2 2a.75.75 0 000 1.06l2 2a.75.75 0 101.06-1.06L5.31 8l1.47-1.47z' data-evernote-id='901' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
[**README.md**](https://gist.github.com/natalie-o-perret/19bf6e1e9d48a493919b78aa0bc7cdd1#file-readme-md)

# General Stuff ‍♀️

- [Website: The Official Documentation, by Microsoft](https://docs.microsoft.com/en-us/dotnet/fsharp)
- [Website: F# for Fun and Profit, by Scott Wlaschin](https://fsharpforfunandprofit.com/)
- [️ YouTube Playlist: Learn F#, by Ben Gobeil](https://www.youtube.com/playlist?list=PLWtGeD5k0ryjIR9tHtn3-oXKMeq4sdgYq)

# Practices-slash-Code Architecture

- [GitHub Gist: Effective F#, by Scott Wlaschin](https://gist.github.com/swlaschin/31d5a0a2c4478e82e3ed60d653c0206b)
- [Book: Domain Modeling Made Functional, by Scott Wlaschin](https://www.amazon.com/Domain-Modeling-Made-Functional-Domain-Driven/dp/1680502549)
- [️ YouTube Video: Property Based Testing, by Scott Wlaschin](https://www.youtube.com/watch?v=99oO-6EIyck)
- [️ YouTube Video: Active Patterns, by Paul Blasucci](https://www.youtube.com/watch?v=Q5KO-UDx5eA)
- [Website: Thoughts and Ramblings about F#, by Paul Blasucci](https://paul.blasuc.ci/)

# Functional Programming ✖️

- [️ YouTube Playlist: UiT INF-3910-5 - A (too?) slow-paced Course about Functional programming in F# by
  Jonas Juselius](https://www.youtube.com/playlist?list=PLiLMQyqbPyEMTGBoJ0Y1lG2SRv525dqq8)
- [️ YouTube Video: FSharpPlus by Josef Starýchfojtů](https://www.youtube.com/watch?v=pxJCHJgG8ws)
- [️ Vimeo Video: Applicatives IRL, by Jérémie Chassaing](https://vimeo.com/338449781)
- [Website: Think Before Coding, by Jérémie Chassaing](https://thinkbeforecoding.com/)
- [Essential Functional-First F#, by Ian Russell](https://leanpub.com/essential-fsharp)

# Performance / Optimization ‍♀️‍♂️⚡

- [️ YouTube Channel: Fast F#, by Matthew Crew](https://www.youtube.com/user/Wallhoode/videos)
- [️ YouTube Video: #NOMEMALLOC by Jérémie Chassaing](https://www.youtube.com/watch?v=eVJ5b1lwMJ8)

# Twitter

- [Don Syme](https://twitter.com/dsymetweets)
- [Vlæd Zá](https://twitter.com/vzarytovskii)
- [Jérémie Chassaing](https://twitter.com/thinkb4coding)
- [Scott Wlaschin](https://twitter.com/ScottWlaschin)
- [Matthew Crews](https://twitter.com/McCrews)
- [Paul Blasucci](https://twitter.com/pblasucci)
- [Ian Russell](https://twitter.com/ijrussell)

[![362263](gist-github-com--resources-for-f-sharp-onboarding/5ba2afd38d9254aaff585333fc73694d.png)](https://gist.github.com/thluiz)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-heading js-evernote-checked' data-evernote-id='237'%3e %3cpath fill-rule='evenodd' d='M3.75 2a.75.75 0 01.75.75V7h7V2.75a.75.75 0 011.5 0v10.5a.75.75 0 01-1.5 0V8.5h-7v4.75a.75.75 0 01-1.5 0V2.75A.75.75 0 013.75 2z' data-evernote-id='992' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-bold js-evernote-checked' data-evernote-id='238'%3e %3cpath fill-rule='evenodd' d='M4 2a1 1 0 00-1 1v10a1 1 0 001 1h5.5a3.5 3.5 0 001.852-6.47A3.5 3.5 0 008.5 2H4zm4.5 5a1.5 1.5 0 100-3H5v3h3.5zM5 9v3h4.5a1.5 1.5 0 000-3H5z' data-evernote-id='994' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-italic js-evernote-checked' data-evernote-id='239'%3e %3cpath fill-rule='evenodd' d='M6 2.75A.75.75 0 016.75 2h6.5a.75.75 0 010 1.5h-2.505l-3.858 9H9.25a.75.75 0 010 1.5h-6.5a.75.75 0 010-1.5h2.505l3.858-9H6.75A.75.75 0 016 2.75z' data-evernote-id='996' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-quote js-evernote-checked' data-evernote-id='240'%3e %3cpath fill-rule='evenodd' d='M1.75 2.5a.75.75 0 000 1.5h10.5a.75.75 0 000-1.5H1.75zm4 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zM2.5 7.75a.75.75 0 00-1.5 0v6a.75.75 0 001.5 0v-6z' data-evernote-id='999' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-code js-evernote-checked' data-evernote-id='241'%3e %3cpath fill-rule='evenodd' d='M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z' data-evernote-id='1001' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-link js-evernote-checked' data-evernote-id='243'%3e %3cpath fill-rule='evenodd' d='M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z' data-evernote-id='1004' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-list-unordered js-evernote-checked' data-evernote-id='244'%3e %3cpath fill-rule='evenodd' d='M2 4a1 1 0 100-2 1 1 0 000 2zm3.75-1.5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zM3 8a1 1 0 11-2 0 1 1 0 012 0zm-1 6a1 1 0 100-2 1 1 0 000 2z' data-evernote-id='1007' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-list-ordered js-evernote-checked' data-evernote-id='245'%3e %3cpath fill-rule='evenodd' d='M2.003 2.5a.5.5 0 00-.723-.447l-1.003.5a.5.5 0 00.446.895l.28-.14V6H.5a.5.5 0 000 1h2.006a.5.5 0 100-1h-.503V2.5zM5 3.25a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5A.75.75 0 015 3.25zm0 5a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5A.75.75 0 015 8.25zm0 5a.75.75 0 01.75-.75h8.5a.75.75 0 010 1.5h-8.5a.75.75 0 01-.75-.75zM.924 10.32l.003-.004a.851.851 0 01.144-.153A.66.66 0 011.5 10c.195 0 .306.068.374.146a.57.57 0 01.128.376c0 .453-.269.682-.8 1.078l-.035.025C.692 11.98 0 12.495 0 13.5a.5.5 0 00.5.5h2.003a.5.5 0 000-1H1.146c.132-.197.351-.372.654-.597l.047-.035c.47-.35 1.156-.858 1.156-1.845 0-.365-.118-.744-.377-1.038-.268-.303-.658-.484-1.126-.484-.48 0-.84.202-1.068.392a1.858 1.858 0 00-.348.384l-.007.011-.002.004-.001.002-.001.001a.5.5 0 00.851.525zM.5 10.055l-.427-.26.427.26z' data-evernote-id='1009' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-tasklist js-evernote-checked' data-evernote-id='246'%3e %3cpath fill-rule='evenodd' d='M2.5 2.75a.25.25 0 01.25-.25h10.5a.25.25 0 01.25.25v10.5a.25.25 0 01-.25.25H2.75a.25.25 0 01-.25-.25V2.75zM2.75 1A1.75 1.75 0 001 2.75v10.5c0 .966.784 1.75 1.75 1.75h10.5A1.75 1.75 0 0015 13.25V2.75A1.75 1.75 0 0013.25 1H2.75zm9.03 5.28a.75.75 0 00-1.06-1.06L6.75 9.19 5.28 7.72a.75.75 0 00-1.06 1.06l2 2a.75.75 0 001.06 0l4.5-4.5z' data-evernote-id='1011' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-mention js-evernote-checked' data-evernote-id='247'%3e %3cpath fill-rule='evenodd' d='M4.75 2.37a6.5 6.5 0 006.5 11.26.75.75 0 01.75 1.298 8 8 0 113.994-7.273.754.754 0 01.006.095v1.5a2.75 2.75 0 01-5.072 1.475A4 4 0 1112 8v1.25a1.25 1.25 0 002.5 0V7.867a6.5 6.5 0 00-9.75-5.496V2.37zM10.5 8a2.5 2.5 0 10-5 0 2.5 2.5 0 005 0z' data-evernote-id='1014' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-cross-reference js-evernote-checked' data-evernote-id='249'%3e %3cpath fill-rule='evenodd' d='M16 1.25v4.146a.25.25 0 01-.427.177L14.03 4.03l-3.75 3.75a.75.75 0 11-1.06-1.06l3.75-3.75-1.543-1.543A.25.25 0 0111.604 1h4.146a.25.25 0 01.25.25zM2.75 3.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 01.75.75v2.19l2.72-2.72a.75.75 0 01.53-.22h4.5a.25.25 0 00.25-.25v-2.5a.75.75 0 111.5 0v2.5A1.75 1.75 0 0113.25 13H9.06l-2.573 2.573A1.457 1.457 0 014 14.543V13H2.75A1.75 1.75 0 011 11.25v-7.5C1 2.784 1.784 2 2.75 2h5.5a.75.75 0 010 1.5h-5.5z' data-evernote-id='1018' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Attach files by dragging & dropping, selecting or pasting them.
[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' class='octicon octicon-markdown v-align-bottom js-evernote-checked' data-evernote-id='257'%3e %3cpath fill-rule='evenodd' d='M14.85 3H1.15C.52 3 0 3.52 0 4.15v7.69C0 12.48.52 13 1.15 13h13.69c.64 0 1.15-.52 1.15-1.15v-7.7C16 3.52 15.48 3 14.85 3zM9 11H7V8L5.5 9.92 4 8v3H2V5h2l1.5 2L7 5h2v6zm2.99.5L9.5 8H11V5h2v3h1.5l-2.51 3.5z' data-evernote-id='1062' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='24' viewBox='0 0 16 16' version='1.1' width='24' data-view-component='true' class='octicon octicon-mark-github js-evernote-checked' data-evernote-id='258'%3e %3cpath fill-rule='evenodd' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z' data-evernote-id='1071' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://github.com/ "GitHub") 
  © 2022 GitHub, Inc.

- [Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)
- [Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)
- [Security](https://github.com/security)
- [Status](https://www.githubstatus.com/)
- [Docs](https://docs.github.com/)
- [Contact GitHub](https://support.github.com/?tags=dotcom-footer)
- [Pricing](https://github.com/pricing)
- [API](https://docs.github.com/)
- [Training](https://services.github.com/)
- [Blog](https://github.blog/)
- [About](https://github.com/about)
