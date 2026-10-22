---
title: "Building a Real-time Kanban Board with Phoenix LiveView"
date: '2021-02-18T09:07:53-03:00'
category: webclip
summary: 'The post walks through building a minimal Kanban board with Phoenix LiveView, from project setup and Ecto schemas to LiveView events, PubSub broadcasts, and drag-and-drop updates.'
tags: ["phoenix-liveview", "kanban", "elixir", "pubsub"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Real-time Kanban Board with Phoenix LiveView | by Léonard Hetsch | The Startup | Feb, 2021 | Medium"
    url: "https://medium.com/swlh/building-a-real-time-kanban-board-with-phoenix-liveview-e9b718ac185"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/medium-com--building-a-real-time-kanban-board-with-phoenix-liveview.md"
    kind: repo
---

The article explains how to build a minimal Kanban board with Phoenix LiveView. It starts from project scaffolding and database schemas, then shows how LiveView mounts state, re-renders on updates, and keeps multiple clients in sync through PubSub.

## Reading notes

- LiveView uses a declarative model: events update state, and the relevant HTML is re-rendered and pushed to the browser.
- The project is set up with `mix phx.new --live`, PostgreSQL, Ecto schemas for boards, columns, and cards, and seed data.
- A board page is rendered through `live_render`, while the LiveView process fetches the board by ID and stores it in socket assigns.
- The front end uses borrowed Kanban UI code, Bootstrap, and Dragula for drag-and-drop behavior.
- The “Add card” button uses `phx-click` and `phx-value-column` to send an `add_card` event with the target column ID.
- The LiveView handler creates the card, saves it, reloads the board, and reassigns the socket so the page updates.
- LiveView can subscribe to a topic such as `boards:<board ID>` so updates can be broadcast to every connected client.
- When a card changes, the process handles the message with `handle_info`, reassigns the board, and re-renders the page.
- Card content updates are triggered with `phx-blur` on the `textarea`, passing the card ID and the new value.
- Moving a card to another column is handled through a controller route and a broadcast after the database update.
- Dragula detects the drop on the front end, and `fetch` sends the change to the API endpoint.
