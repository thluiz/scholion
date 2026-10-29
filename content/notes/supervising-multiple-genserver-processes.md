---
title: "Supervising multiple GenServer processes"
date: '2016-04-17T17:11:26-03:00'
category: webclip
summary: 'The post refactors a single board monitor into one GenServer per board, supervised by a module-based Supervisor, so a failure in one board does not wipe the state of the others.'
tags: ["elixir", "genserver", "supervisor", "phoenix"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Supervising multiple GenServer processes - Code, Love & Boards"
    url: "http://codeloveandboards.com/blog/2016/03/20/supervising-multiple-genserver-processes/?utm_campaign=elixir_radar_45&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/codeloveandboards-com--supervising-multiple-genserver-processes.md"
    kind: repo
---

The article explains a refactoring in the Trello tribute series: instead of keeping all connected board members in one GenServer, it creates one process per board and puts them under a supervisor. That way, if one process dies or restarts, the state of the other boards is not lost.

## Reading notes

- A single `PhoenixTrello.BoardChannel.Monitor` kept a map of connected users by board, but a restart would lose that state.
- The proposed fix is to split the state into multiple processes, one for each board.
- A module-based `Supervisor` starts and restarts the monitor processes.
- The supervisor uses `restart: :transient` so a child restarts only after an abnormal termination.
- The setup uses `:simple_one_for_one` so only the child process that fails is restarted.
- `PhoenixTrello.BoardChannel.Monitor` gets a dynamic name from `board_id` through `ref(board_id)`.
- `create(board_id)` checks whether a process already exists for that board before calling `Supervisor.start_child/2`.
- `user_joined/2`, `users_in_board/1`, and `user_left/2` call the correct process through `try_call/2`.
- The application supervision tree is updated to include the new board-channel supervisor instead of the old monitor worker.
