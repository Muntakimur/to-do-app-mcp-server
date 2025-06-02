from langchain_core.language_models.chat_models import BaseChatModel 
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage 
from langchain_core.tools import BaseTool 
from config import Config 
from tools import call_tool 
from logger import get_logger


log = get_logger(__name__)
SYSTEM_PROMPT = """
You are a helpful personal productivity assistant that manages a user's task list using tools connected to a database. Your goal is to help the user add, view, complete, and delete tasks efficiently.

TOOLS:
You have access to the following tools:
- `add_task`: Add a new task.
- `list_tasks`: Show all tasks.
- `complete_task`: Mark a task as completed.
- `remove_task`: Delete a task.

INSTRUCTIONS:
- **Always use tools to interact with tasks** (tasks are stored in a database).
- **Only use ONE tool per user request.**
- **Never call the same tool more than once per request.**
- When listing tasks, **display the task ID, name, and completion status**.
- Use ✅ for completed tasks and 🟡 for tasks that are not complete.
- When presenting tasks, use **Markdown** formatting. Prefer tables or bullet points when appropriate.
- If a user asks for something unrelated to task management, respond with:
  > "I can help you manage your tasks. You can ask me to add, view, complete, or remove tasks."

FORMAT:
Respond clearly and concisely. If a tool is needed, respond with a structured tool call. Otherwise, reply with a plain response formatted in Markdown.
""".strip()


def create_history() -> list[BaseMessage]:
    return [SystemMessage(content=SYSTEM_PROMPT)]

async def ask(
    query:str,
    history:list[BaseMessage],
    llm:BaseChatModel,
    available_tools:list[BaseTool],
    max_iterations:int = Config.Agent.MAX_ITERATIONS,
) -> str:
    
    log.info(f"User Request: {query}")   
    
    n_iterations = 0
    messages = history.copy()
    messages.append(HumanMessage(content=query))

    while n_iterations < max_iterations:
        response = await llm.ainvoke(messages)
        messages.append(response)

        if not response.tool_calls:
           return response.content
        
        for tool_call in response.tool_calls:
            log.info(f"Tool Call: {tool_call}") 
            response = await call_tool(tool_call, available_tools)
            messages.append(response)
        
        n_iterations += 1
    raise RuntimeError("Max iterations reached")