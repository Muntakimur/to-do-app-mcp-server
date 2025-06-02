# Task Manager MCP Server

## Overview

This project is a **Task Manager MCP Server** designed to manage tasks efficiently using tools connected to a database. It provides APIs for adding, viewing, completing, and deleting tasks, and integrates with LangChain for AI-driven task management.

## Features

- **Task Management**: Add, list, complete, and remove tasks.
- **Streamlit Integration**: A user-friendly interface for interacting with the task manager.
- **AI Assistance**: Uses LangChain to provide intelligent responses and manage tasks.
- **Tool Integration**: Connects to external tools for enhanced functionality.

## Project Structure

```
├── agent.py          # Handles AI interactions and tool calls.
├── client.py         # Connects to the server using SSE.
├── config.py         # Configuration settings for models and server.
├── logger.py         # Logging utility for debugging.
├── models.py         # Creates and configures language models.
├── server.py         # Implements the MCP server and task management tools.
├── streamlit.py      # Streamlit-based UI for task management.
├── task.py           # Defines the Task model using Pydantic.
├── task_manager.py   # Manages the task list and operations.
├── tools.py          # Handles tool loading and execution.
├── requirements.txt  # Lists project dependencies.
├── .gitignore        # Specifies files to ignore in version control.
├── .vscode/          # VS Code configuration for debugging.
└── README.md         # Project documentation.
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and configure necessary variables.

## Usage

### Running the Server

Start the MCP server:

```sh
python server.py
```

### Running the Streamlit UI

Launch the Streamlit interface:

```sh
streamlit run streamlit.py
```

### Debugging

Use the VS Code debugger configurations in `.vscode/launch.json`.

## Key Components

### Server

The server ([server.py](server.py)) provides tools for task management:

- `list_tasks`: Lists all tasks.
- `add_task`: Adds a new task.
- `remove_task`: Removes a task by ID.
- `mark_complete`: Marks a task as complete.

### Streamlit UI

The Streamlit interface ([streamlit.py](streamlit.py)) allows users to interact with the task manager visually.

### AI Agent

The AI agent ([agent.py](agent.py)) uses LangChain to process user queries and interact with tools.

## Dependencies

See [requirements.txt](requirements.txt) for a complete list of dependencies.

## License

This project is licensed under [Your License].

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for discussion.

## Contact

For questions or support, contact [Your Email/Contact Info].
