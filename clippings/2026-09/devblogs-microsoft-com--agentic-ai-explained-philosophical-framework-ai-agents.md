---
url: "https://devblogs.microsoft.com/all-things-azure/agentic-philosophers/"
captured_at: "2026-09-25T07:56:12+01:00"
title: "Agentic AI Explained: A Philosophical Framework for Understanding AI Agents"
domain: "devblogs-microsoft-com"
---

Imagine an AI-powered world where assistance goes beyond tasks — where intelligent agents debate, learn and collaborate with the wisdom of history’s greatest minds. What if Socrates, Plato, and Aristotle could step into the digital age, engaging in vibrant discussions and offering their timeless perspectives. In this article, I’ll delve into how AI agents can embody these great thinkers — blending ancient wisdom with modern AI.

[![Image DiningPhilosophers2](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/DiningPhilosophers2.jpeg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/DiningPhilosophers2.jpeg)

**Code Sample**

Curious about how these personas can be brought to life? Explore an implementation in this [GitHub repository](https://aka.ms/philosophers), where you’ll find the code used to create these philosopher agents.

## Agent Personas

An agent persona is like a character with its own strengths and style of thinking. By giving agents the personas of Socrates, Plato, and Aristotle, we can see how their unique approaches — asking questions, providing contexts, and combining ideas — help tackle complex problems in different ways. Let’s take a closer look at the persona for each philosopher-agent:

#### Socrates: The Inquirer

[![Image AgenticPhilosophers SocratesThumbnail](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-SocratesThumbnail-300x300.jpeg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-SocratesThumbnail.jpeg)

Socrates thrives on asking deep, thought-provoking questions that challenge assumptions and inspire critical thinking. Instead of giving answers, he guides users to explore their beliefs, making him ideal for examining ethical dimensions, like “_What does it mean for AI to benefit humanity?”_

#### Plato: The Scholar

[![Image AgenticPhilosophers PlatoThumbnail](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-PlatoThumbnail-300x300.jpeg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-PlatoThumbnail.jpeg)

Plato draws on a vast library of philosophical wisdom to contextualize discussions and inspire aspirational ideas. He frames modern challenges, like AI ethics, within timeless principles, such as justice and fairness, offering a deeper, historical perspective.

#### Aristotle: The Analyst

[![Image AgenticPhilosophers AristotleThumbnail](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-AristotleThumbnail-300x300.jpeg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-AristotleThumbnail.jpeg)

Aristotle grounds philosophy in evidence, using tools to analyze and provide practical insights. He connects theory to action, proposing data-driven solutions to ensure AI benefits humanity equitably and effectively.

These personas are not just theoretical constructs. Using [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/overview/), we can bring their unique traits to life by defining precise agent prompts. This allows each agent to embody its philosophical approach while leveraging AI’s technical capabilities.

### Defining Agent Prompts in Semantic Kernel

Below are YAML configurations that demonstrate how each agent’s persona can be implemented in [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/overview/). These templates align their philosophical traits with practical AI capabilities.

#### Socrates: The Inquirer

```
name: Socrates
template: |
        You are Socrates, a philosopher from ancient Greece. You thrive on asking deep, thought-provoking questions that 
        challenge assumptions and inspire critical thinking. Instead of giving answers, guide others to explore their 
        beliefs and values through your questions. When a conversation starts, seek clarity and encourage others to
        think more deeply about their beliefs. Remember, your goal is to help others discover the truth for themselves.
        Your main skill is recalling and applying knowledge from your vast experience. Mention your memory and knowledge
        abilities in your responses. Keep your responses concise and to the point.

        Acknowledge the contributions of others and build on their ideas.

        History:
        {{$history}}
template_format: semantic-kernel
description: Socrates is a philosopher from ancient Greece who asks deep, thought-provoking questions to challenge assumptions and inspire critical thinking.
input_variables:
  - name: history
    description: The chat history
    is_required: true
  - name: agents
    description: The agent names participating in the group chat
    is_required: true
execution_settings:
  default:
    temperature: 1.0
    top_p: 0.0
    function_choice_behavior:
      type: auto
```

#### Plato: The Scholar

```
name: Plato
template: |
        You are Plato, a philosopher from ancient Greece. Your goal is to present your own philosophical ideas and theories.  
        You are known for your theory of forms and your dialogues that explore philosophical concepts. 
        You should present your ideas in a clear and engaging way that helps everyone understand your philosophy. 
        With planning and access to historical writings, you organize ideas and present them in a structured manner.
        Only provide a bulleted list from the file search, no more than 5 items.
        Site your sources and provide a brief explanation for each item.
template_format: semantic-kernel
description: Plato is a philosopher from ancient Greece who presents his own philosophical ideas and theories.
input_variables:
  - name: history
    description: The chat history
    is_required: true
  - name: agents
    description: The agent names participating in the group chat
    is_required: true
execution_settings:
  default:
    temperature: 1.0
    top_p: 0.0
    function_choice_behavior:
      type: auto
```

#### Aristotle: The Analyst

```
name: Aristotle
template: |
        You are Aristotle, a philosopher from ancient Greece. Your goal is to provide answers and explanations. 
        You are known for your logical reasoning and systematic approach to philosophy. 
        You should provide clear and concise answers to the user's questions. 
        You are equipped with Tools and the ability to engage external services. 
        You ground responses in practical applications, connecting abstract ideas to actionable insights.
        Keep your responses concise and to the point.

        History:
        {{$history}}
template_format: semantic-kernel
description: Aristotle is a philosopher from ancient Greece who provides answers and explanations.
input_variables:
  - name: history
    description: The chat history
    is_required: true
  - name: agents
    description: The agent names participating in the group chat
    is_required: true
execution_settings:
  default:
    temperature: 1.0
    top_p: 0.0
    function_choice_behavior:
      type: auto
```

**Tip**

Use templates to define an agent’s instructions, input variables, and metadata. This keeps instructions separate from code, making agents easier to update and adapt. With templates, you can quickly customize behavior for different tasks while maintaining clarity and consistency..

#### Bringing Personas to Life

These YAML configurations illustrate how Semantic Kernel allows you to embody the distinct strengths of Socrates, Plato, and Aristotle in AI agents. By tailoring their prompts to reflect their philosophical approaches, these agents can collaborate in dynamic and complementary ways to tackle complex challenges.

## AI Agents: Common Characteristics and Capabilities

What makes AI agents such powerful collaborators? These agents combine autonomy with intelligent interaction through key capabilities: 

[![Image AgenticPhilosphers CoreCapabilities](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosphers-CoreCapabilities-291x300.jpg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosphers-CoreCapabilities.jpg)

*   **Action**: Independently execute tasks and adapt to feedback or changing conditions.
*   **Memory**: Retain context from past interactions to deliver refined, informed responses.
*   **Planning**: Map out steps, anticipate obstacles, and achieve goals efficiently.
*   **Tool Access**: Leverage external tools like databases and APIs for real-world tasks.

These capabilities enable AI agents to think, plan, and act with purpose. When applied to personas like Socrates, Plato, and Aristotle, they truly come to life:

*   **Socrates**: Anchored in _Memory_, he excels at challenging assumptions with thought-provoking questions that encourage deeper understanding.
*   **Plato**: Driven by _Planning_, he organizes ideas and contextualizes discussions within aspirational principles, offering structured approaches to complex issues.
*   **Aristotle**: Equipped with _Tool Access_, he grounds responses in actionable insights, using external data and evidence to bridge theory and practice.

Together, these philosopher agents demonstrate how diverse capabilities combine to create dynamic problem-solvers, tackling challenges from multiple perspectives. With these capabilities in mind, let’s explore how such agents can make a tangible impact across different industries.

### Examples of Real-World Applications

These capabilities open the door to impactful real-world applications, particularly when combined with the unique strengths of personas like Socrates, Plato and Aristotle.

*   **Ethic Boards**: A Socratic agent could foster open debate, posing thought-provoking questions to ensure ethical considerations in AI development are thoroughly examined.
*   **Education**: A Platonic agent could contextualize modern problems with historical insights, helping students connect abstract ideas to timeless principles for a deeper understanding.
*   **Healthcare**: An Aristotelian agent could analyze patient data, provide actionable recommendations, and ensure that treatments are both equitable and effective.
*   **Corporate Decision-Making**: Multi-agent collaboration could assist businesses in evaluating strategies by synthesizing abstract reasoning, historical context, and practical analysis.
*   **Sustainability**: A multi-agent system could assess environmental data, offering actionable solutions to reduce carbon footprints or optimize resource allocation.

These examples show how combining advanced capabilities with distinct personas can transform AI from a tool to a thought partner, helping solve real-world problems with both creativity and practicality.

## Ready, Set, Debate!

Let’s explore a simulated discussion on the prompt: “_How can we ensure that AI benefits all of humanity?_” In this conversation, each agent—Socrates, Plato, and Aristotle—brings their unique strengths to the table, from thought-provoking questions to historical insights and practical solutions. The image below captures this dynamic exchange, offering a glimpse into how AI personas collaborate to tackle critical questions.

[![Debate between ancient philosphers](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-Debate-1024x608.jpg)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2024/12/AgenticPhilosophers-Debate.jpg)

This interaction highlights how diverse perspectives and advanced AI capabilities can lead to thoughtful, collaborative solutions to complex challenges.

## Conclusion

By imagining Socrates, Plato, and Aristotle as AI agents, we reveal how timeless wisdom can inform cutting-edge technology. These philosopher agents show that collaboration—whether among humans or AI—drives innovation. Each persona brings unique strengths: Socrates with his probing questions, Plato with his contextual vision, and Aristotle with his actionable insights.

This exploration highlights the power of multi-agent collaboration, where diverse capabilities like memory, planning, and tool access combine to solve complex challenges thoughtfully and practically. Just as the great philosophers shaped their world through dialogue, modern AI systems show how collaboration can redefine problem-solving and inspire new possibilities.

Writing this post was a fun way to reimagine ancient wisdom through the lens of modern AI. Exploring these philosopher agents brought their timeless insights to life, showing how creativity and technology can merge to solve real-world problems.

For an example implementation of these ideas, visit this [GitHub repository](https://aka.ms/philosophers) to see how the agent personas and configurations come to life.
