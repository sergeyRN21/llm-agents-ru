---
name: russian-constitution-rag
description: Perform RAG-based search over the Russian Constitution to answer legal questions with precise article references
license: MIT
allowed-tools: constitution_search think_tool read_file write_file
---

# Russian Constitution RAG Skill

## When to Use
- User asks about rights, obligations, or structure of government in Russia
- Question requires citation of specific articles from the Russian Constitution
- Need to verify legal facts or interpret constitutional provisions
- User mentions "Constitution of Russia", "Конституция РФ", "статья конституции"

## Workflow
1. **Analyze the question**: Identify key legal concepts and required information
2. **Search**: Use `constitution_search` with precise query formulation
3. **Verify**: Cross-check results against multiple relevant articles if needed
4. **Cite**: Always provide exact article numbers and quotes from the Constitution
5. **Reflect**: Use `think_tool` to ensure completeness and accuracy

## Best Practices
- Always cite article numbers (e.g., "Article 19, Part 2")
- Include direct quotes from the Constitution when possible
- Distinguish between different parts of the same article
- If uncertain, state limitations clearly rather than speculate
- Save complex queries and results to files for traceability

## Tools Available
- `constitution_search`: Performs full-text search over Russian Constitution
- `think_tool`: Structured reflection on legal interpretation and completeness
- `read_file`/`write_file`: Save intermediate results or complex analyses

## Example Queries
- "What rights does the Russian Constitution guarantee regarding freedom of speech?"
- "Какие статьи Конституции РФ регулируют права человека?"
- "What is the procedure for amending the Russian Constitution?"