---
name: agent-coordination
description: Delegate tasks to specialized sub-agents with isolated contexts for complex problem solving
license: MIT
allowed-tools: task think_tool
---

# Agent Coordination Skill

## Tools Available
- **task(description, subagent_type)**: Delegate to specialized sub-agents
- **think_tool(reflection)**: Reflect on delegated task results

## When to Use
- Complex tasks requiring specialized expertise
- Multiple independent research directions
- Need to isolate context for focused work

## Sub-agent Types
- **research-agent**: For web research tasks

## Delegation Guidelines
- Provide complete, standalone instructions to sub-agents
- Sub-agents can't see each other's work
- Use clear, specific language - avoid acronyms

## Parallel Execution
- For comparisons: use 1 sub-agent per item
- For multi-faceted research: use 1 sub-agent per aspect
- Maximum {max_concurrent_research_units} parallel agents per iteration

## Hard Limits
- **Bias towards focused research** - Use single agent for simple questions
- **Stop when adequate** - Don't over-research
- **Limit iterations** - Stop after {max_researcher_iterations} delegations

## Important Reminders
- Each task call creates a dedicated agent with isolated context
- Always use think_tool to reflect on results before proceeding