from datetime import datetime, timezone
from langchain_core.tools import tool


import re
import os
from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from typing import Annotated

@tool(parse_docstring=True)
def constitution_search(
    query: str,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    """
    Perform full-text search over the Russian Constitution.
    
    Searches for relevant articles containing the query terms and returns excerpts with article numbers.
    
    Args:
        query: Legal question or keywords to search for in the Constitution
        
    """
    try:
        # Загружаем конституцию (можно закэшировать при первом вызове)
        with open("data/constitution.txt", "r", encoding="utf-8") as f:
            constitution_text = f.read()
        
        # Разбиваем на статьи
        articles = re.split(r'\nСтатья (\d+)', constitution_text)
        # articles[0] — преамбула, далее: [номер, текст, номер, текст, ...]
        
        results = []
        raw_content = ""
        
        # Ищем по всем статьям
        for i in range(1, len(articles), 2):
            article_num = articles[i].strip()
            article_content = articles[i+1].strip() if i+1 < len(articles) else ""
            
            # Проверяем, содержит ли статья запрос (регистронезависимо)
            if query.lower() in article_content.lower():
                # Создаём краткий excerpt
                lines = article_content.split('\n')
                excerpt = " ".join(lines[:2]) + "..." if len(lines) > 2 else article_content
                results.append(f"Article {article_num}: {excerpt}")
                raw_content += f"\n\n--- Article {article_num} ---\n{article_content}"
        
        if not results:
            result_text = f"No relevant articles found in the Russian Constitution for query: '{query}'"
            raw_content = "No results"
        else:
            result_text = f"Found {len(results)} relevant articles:\n" + "\n".join(results)
        
        # Сохраняем сырые данные в файл (как в tavily_search)
        filename = f"const_search_{hash(query) % 10000}.md"
        file_content = f"# Constitution Search Results\n\nQuery: {query}\n\n{raw_content}"
        
        files = state.get("files", {})
        files[filename] = file_content
        
        return Command(
            update={
                "files": files,
                "messages": [ToolMessage(result_text, tool_call_id=tool_call_id)]
            }
        )
        
    except Exception as e:
        error_msg = f"Error during constitution search: {str(e)}"
        return Command(
            update={
                "messages": [ToolMessage(error_msg, tool_call_id=tool_call_id)]
            }
        )
    
@tool
def get_current_datetime() -> str:
    """Get current date and time in ISO format (UTC)."""
    return datetime.now(timezone.utc).isoformat()