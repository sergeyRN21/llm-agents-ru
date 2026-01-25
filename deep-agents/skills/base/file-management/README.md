---
name: file-management
description: Manage files in the virtual filesystem for context offloading and data persistence
license: MIT
allowed-tools: ls read_file write_file
---

# File Management Skill

## Tools Available
- **ls()**: List all files in the virtual filesystem (no parameters required)
- **read_file(file_path, offset=0, limit=2000)**: Read file content with pagination
- **write_file(file_path, content)**: Create new file or overwrite existing file

## When to Use
- Save user requests to files for later reference
- Store intermediate results from tool calls
- Read previously saved data for context recovery
- List available files to orient yourself

## Best Practices
- Always save user request at the beginning of complex tasks
- Use descriptive filenames (e.g., `research_mcp_findings.md`)
- Read files before answering to ensure context accuracy
- Use pagination for large files to avoid context overflow

## Workflow Process
1. **Orient**: Use ls() to see existing files before starting work
2. **Save**: Use write_file() to store the user's request
3. **Research**: Proceed with research (search tools will write files)
4. **Read**: Once satisfied with sources, read files to answer user's question