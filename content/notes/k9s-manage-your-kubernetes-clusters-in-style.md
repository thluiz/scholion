---
title: "K9s - Manage Your Kubernetes Clusters In Style"
date: '2020-10-30T08:39:54-03:00'
category: webclip
summary: 'K9s is a terminal UI for Kubernetes that watches cluster changes in real time and adds commands for navigating, observing, and managing resources, with support for RBAC, plugins, metrics, and benchmarking.'
tags: ["kubernetes", "terminal-ui", "cluster-management", "rbac"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "K9s - Manage Your Kubernetes Clusters In Style"
    url: "https://k9scli.io/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/k9scli-io--k9s-manage-your-kubernetes-clusters-in-style.md"
    kind: repo
---

K9s is a terminal-based UI for interacting with Kubernetes clusters. It is meant to make it easier to navigate, observe, and manage deployed applications, while continually watching Kubernetes for changes and offering commands for the resources it sees.

## Reading notes

- It tracks resource activity in real time inside a Kubernetes cluster.
- It supports both standard Kubernetes resources and custom resource definitions.
- It shows real-time metrics for pods, containers, and nodes.
- It includes cluster management commands such as logs, scaling, port-forwards, and restarts.
- Users can define command shortcuts with aliases and hotkeys.
- Plugin support extends K9s with custom cluster commands.
- Filtering mode helps users drill down into workload-related resources.
- It provides views for errors, resource overviews, and resource traversal.
- It supports RBAC viewing and reverse lookup for what a user, group, or ServiceAccount can do.
- It can benchmark HTTP services or pods from inside K9s.
