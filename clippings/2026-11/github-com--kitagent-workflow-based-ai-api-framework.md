---
url: "https://github.com/Drakezair/kitagent"
captured_at: "2026-11-18T11:07:50+00:00"
title: "GitHub - Drakezair/kitagent"
domain: "github-com"
---

KitAgent is a workflow-based API framework powered by YAML and AI agents. Create extensible tools, workflows, and intelligent agents with zero boilerplate.

[![KitAgent Banner](https://github.com/Drakezair/kitagent/raw/main/kitagent.png)](https://github.com/Drakezair/kitagent/blob/main/kitagent.png)

## 🚀 Getting Started

[](#-getting-started)

The easiest way to get started with KitAgent is to use our CLI tool:

# Create a new project
npx create-kitagent my-kitagent-project

# Navigate to the project directory
cd my-kitagent-project

# Copy .env.example to .env and add your OpenAI API key
cp .env.example .env

# Start the development server
npm run dev

## 📝 Description

[](#-description)

KitAgent is a modern backend framework designed to create AI-powered applications with minimal effort. It leverages YAML for configuration and provides a clean architecture for developing tools, workflows, and agents. KitAgent enables developers to focus on business logic rather than boilerplate code.

### ✨ Why Use KitAgent?

[](#-why-use-kitagent)

*   🧰 **Tools System**: Create reusable and composable tools with a simple API
*   🔄 **Workflow Engine**: Define complex workflows with YAML
*   🤖 **AI Agent Integration**: Seamlessly integrate AI models into your applications
*   📨 **HTTP Interface**: Expose your workflows and agents via HTTP endpoints
*   🧩 **Model Context Protocol**: Support for the Model Context Protocol (MCP) for better interoperability
*   🔌 **Extensible**: Easy to extend with custom functionality

### 🧠 Philosophy

[](#-philosophy)

KitAgent follows these core principles:

1.  **Declarative over Imperative**: Use YAML to declare workflows instead of writing procedural code
2.  **Convention over Configuration**: Follow simple patterns to get started quickly
3.  **Modular Architecture**: Build applications with reusable components
4.  **AI-First Approach**: Designed with AI integration in mind from the beginning
5.  **Developer Experience**: Focus on making the framework easy to use and understand

## 🏗️ Architecture

[](#️-architecture)

KitAgent is built around several key components:

### Tools

[](#tools)

A tool is a reusable function that performs a specific task. Tools can be composed together to create more complex functionality.

Example of a tool:

// weatherTool.ts
import { z } from 'zod';
import { registerTool } from 'kitagent';

registerTool({
  name: 'weather',
  description: 'Get current weather for a location',
  parameters: {
    location: z.string().describe('The city and country')
  },
  execute: async ({ params }) \=> {
    // Implementation to fetch weather
    return { temperature: 22, conditions: 'Sunny' };
  }
});

### Workflows

[](#workflows)

Workflows define a sequence of steps that can include tools or agents. They are defined using YAML files.

Example of a workflow:

# travel-planner.wf.yml
name: travel-planner
steps:
  - name: getWeather
    tool: weather
  - name: suggestActivities
    agent: activities
http:
  method: post
  path: /api/travel-planner

### Agents

[](#agents)

Agents are AI-powered components that can use tools to accomplish tasks. They are defined similar to tools but with additional AI capabilities.

Example of an agent:

// activitiesAgent.ts
import { z } from 'zod';
import { registerAgent } from 'kitagent';

registerAgent({
  name: 'activities',
  description: 'Suggests activities based on weather',
  parameters: {
    weather: z.object({
      temperature: z.number(),
      conditions: z.string()
    })
  },
  tools: \['googleMaps', 'tripAdvisor'\],
  task: async ({ params, tools, context }) \=> {
    // Use AI to suggest activities based on weather
    return { activities: \['Visit the park', 'Go to a cafe'\] };
  }
});

### Chat Interface

[](#chat-interface)

KitAgent provides a chat interface for interactive AI experiences.

Example of a chat configuration:

# travel-assistant.chat.yml
name: travel-assistant
type: chat
client: openai
tools:
  - weather
  - activities
http:
  path: /api/chat/travel-assistant

### Model Context Protocol (MCP)

[](#model-context-protocol-mcp)

Support for the Model Context Protocol enables better integration with different AI models.

Example of an MCP configuration:

// travelPlanner.mcp.ts
import { registerMCP } from 'kitagent';

registerMCP({
  name: 'travel-planner',
  description: 'A travel planning assistant',
  version: '1.0.0',
  path: '/api/mcp/travel-planner',
  tools: \['weather', 'activities'\],
  server: async ({ server }) \=> {
    // Configure MCP server
  }
});

## 🔍 Use Cases

[](#-use-cases)

KitAgent is ideal for:

*   🤖 **AI-powered APIs**: Create endpoints that leverage AI models
*   🔄 **Workflow Automation**: Automate complex business processes
*   💬 **Chatbots and Assistants**: Build intelligent conversational agents
*   🧩 **API Orchestration**: Combine multiple APIs into cohesive workflows
*   🔍 **Data Processing Pipelines**: Process and transform data with AI augmentation

## 🛠️ Tools & Resources

[](#️-tools--resources)

*   **create-kitagent**: Our official CLI tool for scaffolding new projects
*   **Ticket Manager Template**: A complete ticket management system example included in the CLI
*   **Documentation**: Coming soon!

## 🛣️ Roadmap

[](#️-roadmap)

*   Build a CLI for scaffolding new KitAgent projects
*   Create simple interface for integration with OpenAI
*   Create simple interface for integration with different AI models and chat providers
*   Develop a visual UI for creating workflows, MCP, and chat systems with drag-and-drop functionality
*   Add real-time capabilities with WebSocket support
*   Implement database adapters for persistent storage
*   Create a plugin system for extending functionality
*   Add authentication and authorization mechanisms
*   Develop comprehensive testing utilities
*   Create deployment templates for various cloud providers

## 📚 Examples

[](#-examples)

Check out the [examples directory](https://github.com/Drakezair/ticket-manager-kitagent) for complete samples of:

*   Tools implementation
*   Workflow definitions
*   Agent configurations
*   Chat setups
*   MCP implementations

Or simply create a new project with our CLI to see a fully implemented ticket management system:

npx create-kitagent ticket-system

## 📄 License

[](#-license)

KitAgent is open source software licensed under the [MIT license](https://github.com/Drakezair/kitagent/blob/main/LICENSE.md).

## 👥 Contributing

[](#-contributing)

We welcome contributions! Please see our [Contributing Guide](https://github.com/Drakezair/kitagent/blob/main/CONTRIBUTING.md) for details on how to get started.

## 🙏 Acknowledgements

[](#-acknowledgements)

KitAgent is inspired by frameworks like Express, NestJS, and Langchain, aiming to combine the best aspects of these tools with a focus on AI integration.
