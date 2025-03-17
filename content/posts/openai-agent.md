---
title: "Openai Agent"
date: 2025-03-17T14:48:03+08:00
# bookComments: false
# bookSearchExclude: false
---

# OpenAI 新功能发布

2025/03/11 OpenAI 发布了新的功能

> We believe agents will soon become integral to the workforce, significantly enhancing productivity across industries. 

- Response API：是 Assistant API 的升级版
- 内置工具：WebSearch, File Search, Computer use agent, code interpreter
- Agents SDK: 用于编排 Agent 的workflow，支持 single agent 和 multi agent
- 监控工具：2个追踪 Agent 工作流，分别是 `Logs` 和 `Traces` <https://platform.openai.com/traces>


## Response API

The Responses API is our new API primitive for leveraging OpenAI’s built-in tools to build agents. It combines the simplicity of Chat Completions with the tool-use capabilities of the Assistants API. 


## CUA (Computer use Agent)

Developers can use the computer use tool to automate browser-based workflows like performing quality assurance on web apps or executing data-entry tasks across legacy systems. 


## Agents SKD

开源 Python 版本 <https://github.com/openai/openai-agents-python>
NodeJS 版本后续开源 ～

To orchestrate agentic workflows

Improvements include:

- Agents: Easily configurable LLMs with clear instructions and built-in tools.
- Handoffs: Intelligently transfer control between agents.
- Guardrails: Configurable safety checks for input and output validation.
- Tracing & Observability: Visualize agent execution traces to debug and optimize performance.

```sh
pip install openai-agents
```

```py
from agents import Agent, Runner, WebSearchTool, function_tool, guardrail

@function_tool
def submit_refund_request(item_id: str, reason: str):
    # Your refund logic goes here
    return "success"

support_agent = Agent(
    name="Support & Returns",
    instructions="You are a support agent who can submit refunds [...]",
    tools=[submit_refund_request],
)

shopping_agent = Agent(
    name="Shopping Assistant",
    instructions="You are a shopping assistant who can search the web [...]",
    tools=[WebSearchTool()],
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Route the user to the correct agent.",
    handoffs=[shopping_agent, support_agent],
)

output = Runner.run_sync(
    starting_agent=triage_agent,
    input="What shoes might work best with my outfit so far?",
)
```

The Agents SDK works with the Responses API and Chat Completions API. The SDK will also work with models from other providers, as long as they provide a Chat Completions style API endpoint. 

In designing the Agents SDK, our team was inspired by the excellent work of others in the community including **[Pydantic⁠](https://github.com/pydantic/pydantic)**, **Griffe⁠** and **[MkDocs](https://github.com/mkdocs/mkdocs)**. 

We’re committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.

### Why use the Agents SDK

The SDK has two driving design principles:

1. Enough features to be worth using, but few enough primitives to make it quick to learn.
2. Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

- Agent loop: Built-in agent loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
- Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
- Handoffs: A powerful feature to coordinate and delegate between multiple agents.
- Guardrails: Run input validations and checks in parallel to your agents, breaking early if the checks fail.
- Function tools: Turn any Python function into a tool, with automatic schema generation and Pydantic-powered validation.
- Tracing: Built-in tracing that lets you visualize, debug and monitor your workflows, as well as use the OpenAI suite of evaluation, fine-tuning and distillation tools.

## Reference
- [New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
- [GITHUB: openai-agents-python](https://github.com/openai/openai-agents-python)
- [Docs: OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

