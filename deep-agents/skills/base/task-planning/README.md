---
name: task-planning
description: Create and manage structured task lists for tracking progress through complex workflows
license: MIT
allowed-tools: write_todos read_todos
---

# Task Planning Skill

## When to Use
- Multi-step or non-trivial tasks requiring coordination
- When user provides multiple tasks or explicitly requests todo list  
- Avoid for single, trivial actions unless directed otherwise

## Structure
- Maintain one list containing multiple todo objects (content, status, id)
- Use clear, actionable content descriptions
- Status must be: pending, in_progress, or completed

## Best Practices  
- Only one in_progress task at a time
- Mark completed immediately when task is fully done
- Always send the full updated list when making changes
- Prune irrelevant items to keep list focused

## Workflow Process
1. Use write_todos to create TODO at the start of a user request
2. After accomplishing a TODO, use read_todos to remind yourself of the plan
3. Reflect on what you've done and the TODO
4. Mark task as completed, and proceed to the next TODO
5. Continue until all TODOs are completed

IMPORTANT: Always create a research plan of TODOs for ANY user request.