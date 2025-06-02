from mcp.server.fastmcp import FastMCP
from config import Config
from task import Task
from task_manager import TaskManager
from typing import Union

mcp = FastMCP(
             name ="TestMCP",
             host=Config.Server.HOST,
             port=Config.Server.PORT,
            )


manager = TaskManager()

@mcp.tool()
def list_tasks() -> Union[list[Task], str]:
    """ List all tasks. """
    task_list = manager.get_tasks()
    return task_list or "No tasks available."


@mcp.tool()
def add_task(name: str) -> list[Task]:
    """ Add a new task

    args:
        name (str): The name of the task to add.

    Returns:
        list[Task]: A updated list of tasks.

    """
    manager.add_task(name)
    return manager.get_tasks()

@mcp.tool()
def remove_task(task_id: str) -> list[Task]:
    """ Remove a task by its ID.

    args:
        task_id (str): The ID of the task to remove.

    Returns:
        list[Task]: A updated list of tasks.
    """
    manager.remove_task(task_id)
    return manager.get_tasks()

@mcp.tool()
def mark_complete(task_id: str) -> list[Task]:
    """ Mark a task as complete

    args:
        task_id (str): The ID of the task to mark as complete.

    Returns:
        list[Task]: A updated list of tasks.
    """
    manager.mark_complete(task_id)
    return manager.get_tasks()


if __name__ == "__main__":
    mcp.run(transport='streamable-http')