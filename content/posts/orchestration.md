---
title: "Orchestration"
date: 2025-03-17T20:22:44+08:00
# bookComments: false
# bookSearchExclude: false
---

# Agent Orchestration

Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how do they decide what happens next? There are two main ways to orchestrate agents:

- Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
- Orchestrating via code: determining the flow of agents via your code.


## Orchestrating via LLM

An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents.

This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:

- Invest in good prompts. Make it clear what tools are available, how to use them, and what parameters it must operate within.
- Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
- Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
- Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
- Invest in evals. This lets you train your agents to improve and get better at tasks.


## Orchestrating via code

Common patterns here are:

- Using structured outputs to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
- Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
- Running the agent that performs the task in a while loop with an agent that evaluates and provides feedback, until the evaluator says the output passes certain criteria.
- Running multiple agents in parallel, e.g. via Python primitives like asyncio.gather. This is useful for speed when you have multiple tasks that don't depend on each other.

