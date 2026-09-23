---
url: "https://agentjido.xyz/blog/weather-agent"
captured_at: "2025-04-03T09:15:39-03:00"
title: "Agent Jido · Agent Jido"
domain: "agentjido-xyz"
---

Jido has been under active development for the past few months. Most of that work has been foundational, focused on building a solid framework that makes it easy to build complex AI agents in Elixir.

Today, I'm excited to finally share a "real" example of what can be done with Jido. There's a lot more to come, but this will give you a taste of what's possible.

### The Weather Agent

We're going to build a simple agent that can answer natural language questions about the weather. It will understand the request, use a tool to fetch weather data, and then provide a response, all orchestrated by Jido and an LLM.

### The Code

Let's break down the components involved in building this agent.

#### 1. The Weather Tool (Action)

The first component is the `Jido.Tools.Weather` Action. This Action uses the `weather` package from @spencerolson to get the weather for a given location. It utilizes the OpenWeatherMap API to fetch the weather data. For demonstration purposes in the Livebook, we default to using test data (`test: true`) so you don't need an API key immediately.

```
defmodule Jido.Tools.Weather do
  use Jido.Action,
    name: "weather",
    description: "Get the weather for a given location via the OpenWeatherMap API",
    category: "Weather",
    tags: ["weather"],
    vsn: "1.0.0",
    schema: [
      location: [type: :string, doc: "The location to get the weather for"],
      units: [type: :string, doc: "Units to use (metric/imperial)", default: "metric"],
      hours: [type: :integer, doc: "Number of hours to forecast", default: 24],
      format: [type: :string, doc: "Output format (text/map)", default: "text"],
      test: [type: :boolean, doc: "Whether to use test data instead of real API", default: true]
    ]

  def run(params, _context) do
    with {:ok, opts} <- build_opts(params),
         {:ok, response} <- Weather.API.fetch_weather(opts) do
      {:ok, format_response(response.body, params)}
    else
      {:error, error} -> {:error, "Failed to fetch weather: #{inspect(error)}"}
    end
  end
end
```

The full code for the Weather Action is available on GitHub.

Actions are the fundamental building blocks in Jido. They encapsulate a single, reusable piece of functionality. By using `use Jido.Action`, we get:

- Schema Validation: The `schema` defines the expected input parameters, their types, and documentation. Jido validates incoming parameters against this schema automatically.
- Metadata: `name`, `description`, `category`, etc., provide context for humans and potentially for AI agents to understand what the Action does.
- Standard Interface: The `run/2` function is the entry point for executing the Action's logic.
- Tool Conversion: Crucially, `Jido.Action` includes functionality (like `to_tool/0`) that converts the Action's definition into a format compatible with LLM frameworks like Langchain, including generating a JSON schema for the parameters.

#### 2. The Weather Agent Module

Next, we define the agent itself. This module brings together the configuration and provides the user-facing interface.

```
defmodule WeatherAgent do
  use Jido.Agent, name: "weather_agent"

  def start_link(_opts \\ []) do
    Jido.AI.Agent.start_link(
      agent: __MODULE__,
      ai: [
        model: {:openai, model: "gpt-4o-mini"},
        prompt: """
        You are an enthusiastic weather reporter.
        <%= @message %>
        """,
        tools: [
          Jido.Tools.Weather
        ]
      ]
    )
  end

  defdelegate chat_response(pid, message), to: Jido.AI.Agent
  defdelegate tool_response(pid, message), to: Jido.AI.Agent
end

{:ok, pid} = WeatherAgent.start_link()
```

This module uses `Jido.Agent`, marking it as a Jido agent process. The key part is `Jido.AI.Agent.start_link/1`. This function, provided by the `jido_ai` package, sets up a specialized Jido Agent GenServer pre-configured with AI capabilities. We pass it the agent module, and an `ai` keyword list specifying the model, the base prompt template, and the list of `Jido.Action` modules the agent is allowed to use as tools.

#### 3. The Jido AI Agent & Skill (jido_ai)

The `Jido.AI.Agent` module provides the core implementation for AI-powered agents. It builds upon the standard `Jido.Agent` and integrates the `Jido.AI.Skill`.

When `WeatherAgent.tool_response/2` is called, it delegates to `Jido.AI.Agent.tool_response/2`. This function wraps the user's message into a `Jido.Signal` with the type `"jido.ai.tool.response"` and sends it to the agent process using `Jido.Agent.call/2`.

Signals are the standard messaging format within Jido. The agent process receives this signal, and this is where the `Jido.AI.Skill` comes in. Its `router/1` function maps the incoming signal type `"jido.ai.tool.response"` to an Instruction to execute the `Jido.AI.Actions.Langchain.ToolResponse` Action.

Before the action runs, the skill's `handle_signal/2` callback intercepts the signal. It takes the configuration passed during `start_link` (like the model, base prompt, and list of tools) and the incoming message from the signal data. It renders the user's message into the EEx prompt template and packages everything neatly as parameters for the next step: the `ToolResponse` Action.

#### 4. The Tool Response Action (jido_ai)

This is where the core LLM interaction happens, coordinated by Langchain.

This action receives the prepared parameters from the `Jido.AI.Skill`. Its main job is to:

1. Package the `model`, the final `prompt` (with the user message injected), and the list of available `tools` (`[Jido.Tools.Weather]`).
2. Call the underlying `Jido.AI.Actions.Langchain.run/2` function. This lower-level action handles the actual communication with the LLM via the `langchain` hex package.
3. `Jido.AI.Actions.Langchain` takes the list of Jido `tools`, converts them into the format the LLM expects (using `YourAction.to_tool()`), and enables Langchain's function/tool-calling mechanism.
4. The LLM receives the prompt and the descriptions of the available tools. It decides if a tool is needed. If yes, it determines which tool (`weather`) and what parameters to use (e.g., `%{location: "Tokyo"}`).
5. Langchain receives this decision back from the LLM. It then finds the corresponding Jido Action (`Jido.Tools.Weather`) and executes its `run/2` function with the parameters provided by the LLM.
6. The result from `Jido.Tools.Weather.run/2` (the weather data) is sent back to the LLM.
7. The LLM uses this result, combined with the original prompt, to generate the final, user-friendly text response.
8. This final text response is returned by `LangchainAction.run/2` and then by `ToolResponse.run/2`.

### Pulling It All Together

So, when you call `WeatherAgent.tool_response(pid, "What is the weather like in Tokyo right now?")`:

1. `WeatherAgent` -> `Jido.AI.Agent`: The call delegates, creating a Signal type `"jido.ai.tool.response"` with the message.
2. `Jido.Agent.Server`: Receives the signal.
3. `Jido.AI.Skill`: The router maps the signal type to `Jido.AI.Actions.Langchain.ToolResponse`. `handle_signal` prepares the parameters (rendered prompt, model, tools).
4. `Jido.AI.Actions.Langchain.ToolResponse`: Executes its `run` function with the prepared params.
5. `Jido.AI.Actions.Langchain`: Called by `ToolResponse`. It talks to the LLM (GPT-4o Mini), providing the prompt and the `Jido.Tools.Weather` tool definition.
6. LLM Decision: The LLM decides to call the `weather` tool with `location: "Tokyo"`.
7. Langchain Execution: Langchain triggers `Jido.Tools.Weather.run(%{location: "Tokyo"}, _context)`.
8. `Jido.Tools.Weather`: Fetches (test) weather data and returns it.
9. LLM Formatting: The weather data goes back to the LLM.
10. Final Response: The LLM generates the enthusiastic weather report based on the data and the initial prompt.
11. Return: The final text bubbles back up through the actions, skill, and agent server to the original caller.

The power here is how Jido components (Agents, Skills, Actions) and `jido_ai` provide the structure and orchestration, letting Langchain and the LLM handle the complex natural language understanding and tool coordination.

### Agent Showcase

Let's see it handle a few more questions, just like in the Livebook:

```
WeatherAgent.tool_response(pid, "Will I need an umbrella in Paris tomorrow?")
WeatherAgent.tool_response(pid, "Compare the weather in New York and San Francisco today.")
WeatherAgent.tool_response(pid, "Is it a good day for hiking in the mountains near Seattle?")
```

### Conclusion

This Weather Agent example, while simple, demonstrates the core concepts of building AI-powered agents with Jido and `jido_ai`. By composing Actions (like `Jido.Tools.Weather`) and leveraging the pre-built `Jido.AI.Agent` and `Jido.AI.Skill`, we can quickly create agents that understand natural language, use tools to interact with the world (or APIs), and respond intelligently.

The separation of concerns – Actions for specific tasks, Skills for capability management, and Agents for state and process lifecycle – makes the system modular and extensible.

### Additional Resources

- Website: https://agentjido.xyz
- Jido Documentation: https://hexdocs.pm/jido
- Jido AI Documentation: https://hexdocs.pm/jido_ai
- Jido Tools Documentation: https://hexdocs.pm/jido_tools
