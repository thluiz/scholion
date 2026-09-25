---
title: "Local-first software: You own your data, in spite of the cloud"
date: '2025-07-17T13:19:57+01:00'
category: webclip
summary: 'The essay argues that software can keep cloud-like collaboration and access from any device while giving users local ownership, offline use, longevity, privacy, and control over their data.'
tags: ["local-first", "data-ownership", "collaboration", "crdts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Local-first software: You own your data, in spite of the cloud"
    url: "https://www.inkandswitch.com/essay/local-first/?ref=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/inkandswitch-com--local-first-software-you-own-your-data-in-spite-of-the-cloud.md"
    kind: repo
---

The essay argues that cloud apps and old-fashioned local apps each capture only part of what users need. Cloud services make collaboration and cross-device access easy, while local software gives users ownership, offline use, longevity, privacy, and control. It proposes local-first software as a model that keeps the primary copy of data on the user’s device and uses servers only as support.

## Reading notes

- Cloud apps make it easy to collaborate and access data from any device, but they depend on the provider’s server and limit user control over the data.
- Creative users often want to keep the files they make for future reference, portfolios, or archives, and the essay treats that as a matter of ownership.
- In cloud apps, access goes through the server, so if the service is unavailable or shuts down, the user can lose access to both the software and the data.
- Local apps store files on the user’s disk, which lets users back them up, archive them, edit them with other tools, and delete them without asking permission.
- Local-first software keeps the local copy as the primary one, while servers hold secondary copies to help with multi-device access and sync.
- One ideal is fast response without spinners, because local reads and writes avoid waiting for a server round-trip.
- Another ideal is multi-device use without trapping work on one device, with synchronization across laptop, tablet, and phone.
- Local-first software should work offline, including on mobile devices and in places with poor connectivity.
- It should support seamless collaboration with multiple people, including real-time editing and other workflows such as suggestions or pull-request-style review.
- It should support long-term access, so work can still be opened and modified even if the original company or service is gone.
- It should provide security and privacy by default, avoiding centralized databases that collect everyone’s data in one place.
- It should give users ultimate ownership and control, meaning they can copy, modify, back up, and manage their data freely.
- The essay compares several models, including files and email attachments, web apps, file-sync services like Dropbox, and Git/GitHub.
- Files and email give strong offline use, longevity, and control, but weak collaboration.
- Pure web apps score well on collaboration and multi-device access, but poorly on offline use, longevity, privacy, and control.
- File-sync services work well for local files and backups, but real-time collaboration is weak and conflicts are common.
- Git and GitHub come close to local-first for code, with offline use and user control, but they are weak for real-time collaboration and non-text file formats.
- The essay also compares app-development backends such as thin web apps, thick mobile clients, Firebase, CloudKit, Realm, and CouchDB.
- It finds that no existing storage layer fully satisfies the seven ideals.
- The proposed technical direction is CRDTs, which allow concurrent edits to merge automatically and can support real-time collaboration across devices.
- The prototypes Trellis, Pixelpusher, and PushPin are presented as experiments built with CRDTs.
- The findings say the technology works, offline work feels good, conflicts are less common than expected, and visualizing history is important.
- The essay also says URLs are a good way to share documents, while peer-to-peer systems still need better networking and usability.
- It concludes that local-first software is possible, but still needs better tools, research, and products before it can replace server-centered systems.
