---
title: "Switch easily between VirtualBox and Hyper-V with a BCDEdit boot Entry in Windows 8.1"
date: '2014-06-24T10:12:37-03:00'
category: webclip
summary: 'Scott Hanselman explains how to keep Hyper-V available while using VirtualBox-based GenyMotion by adding a separate boot entry that turns the hypervisor off on demand.'
tags: ["windows-8-1", "hyper-v", "virtualbox", "bcdedit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Switch easily between VirtualBox and Hyper-V with a BCDEdit boot Entry in Windows 8.1 - Scott Hanselman"
    url: "http://www.hanselman.com/blog/SwitchEasilyBetweenVirtualBoxAndHyperVWithABCDEditBootEntryInWindows81.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/hanselman-com--switch-easily-between-virtualbox-and-hyper-v-with-bcdedit-bo.md"
    kind: repo
---

Hanselman describes a way to switch between Hyper-V and VirtualBox without disabling Hyper-V through Add/Remove Features. He creates a boot menu copy named “No Hyper-V” with BCDEdit, then uses that entry when he needs GenyMotion and VirtualBox.

## Reading notes

- He uses GenyMotion for Android development with Visual Studio and Xamarin, but GenyMotion depends on VirtualBox.
- VirtualBox and Hyper-V cannot both be active at the same time.
- Instead of removing Hyper-V support through Windows features, he copies the current boot entry from an administrative command prompt and names it “No Hyper-V.”
- He changes that copied entry with `hypervisorlaunchtype off`.
- Because Windows 8.x starts very quickly, he says you need a full shutdown path to reach the alternate boot menu.
- To get there, he opens Settings, then Power, then Restart while holding Shift.
- In the blue recovery-style screen, he chooses Other Operating Systems and then the “No Hyper-V” entry.
- With that boot choice, VirtualBox works and the Acceleration tab in VM system settings is no longer grayed out.
- A normal reboot brings Hyper-V back.
- He shows Android running in VirtualBox through GenyMotion and notes that touch support works too.
