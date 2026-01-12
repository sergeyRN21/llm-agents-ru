
import asyncio
import sys
from pprint import pprint
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
import os

load_dotenv()


if sys.platform == "win32":
    import asyncio
    if not isinstance(asyncio.get_event_loop_policy(), asyncio.WindowsProactorEventLoopPolicy):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def main():

    client = MultiServerMCPClient({
        "local_server": {
            "transport": "stdio",
            "command": "python",
            "args": ["resources/2.1_mcp_server.py"],
        }
    })
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not OPENROUTER_API_KEY:
        raise EnvironmentError("Установите OPENROUTER_API_KEY в файле .env")

    llm = ChatOpenAI(
        model="google/gemini-2.5-flash",
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY
    )

    # 2. Получаем инструменты, ресурсы и промпт
    tools = await client.get_tools()
    resources = await client.get_resources("local_server")
    prompt_list = await client.get_prompt("local_server", "prompt")
    prompt = prompt_list[0].content

    print("Инструменты загружены:", [t.name for t in tools])
    print("Промпт получен (первые 100 символов):", prompt[:100] + "...")

    # 3. Создаём агента
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=prompt
    )

    # 4. Задаём вопрос
    config = {"configurable": {"thread_id": "1"}}
    question = HumanMessage(content="Tell me about the langchain-mcp-adapters library")

    response = await agent.ainvoke(
        {"messages": [question]},
        config=config
    )

    # 5. Выводим результат
    print("\nОтвет агента:")
    print(response["messages"][-1].content)

    # Опционально: полный вывод для отладки
    # pprint(response)

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(main())