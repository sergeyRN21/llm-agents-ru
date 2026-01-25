---
name: research-assistant
description: Conduct web research using Tavily search with structured reflection and context offloading
license: MIT
allowed-tools: tavily_search think_tool
---

# Research Assistant Skill

## Tools Available
- **tavily_search(query)**: Conduct web searches and save raw results to files
- **think_tool(reflection)**: Structured reflection between search iterations

## When to Use
- User asks for factual information, overviews, comparisons, or current status
- Need to gather comprehensive information from multiple sources
- Query requires up-to-date or detailed technical information

## Workflow
1. **Read the question carefully** - What specific information does the user need?
2. **Start with broader searches** - Use broad, comprehensive queries first
3. **After each search, pause and assess** - Do I have enough to answer?
4. **Execute narrower searches** - Fill in the gaps
5. **Stop when confident** - Don't search for perfection

## Hard Limits
- **Simple queries**: 1-2 search tool calls maximum
- **Normal queries**: 2-3 search tool calls maximum  
- **Complex queries**: Up to 5 search tool calls maximum
- **Always stop**: After 5 searches if right sources not found

## Critical Rule
**ALWAYS use think_tool after each search** to reflect on results and plan next steps.

## Output Handling
- Raw search results are automatically saved to files like `findings_topic_xyz.md`
- Summaries are returned in tool messages
- Use read_file() to access full content when needed