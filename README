# mcp-filesystem

The mcp-filesystem is a simple Python-based MCP server that exposes filesystem operations to AI models via the MCP protocol. It currently provides two core functions:

- Listing files in a directory
- Reading the contents of a file

### Usage
The handler runs as an MCP service that communicates via standard input/output. It can be integrated into any system that implements the MCP protocol.

### Available Tools

`list_files(path: str) -> list`

Lists all files in the specified directory.

_Parameters:_

- `path`: Relative path from the home directory


_Returns:_

A list of filenames in the directory


_Errors:_

Raises an error if the path is not a valid directory



`read_file(path: str) -> str`

Reads the contents of the specified file.

_Parameters:_

`path`: Relative path from the home directory


_Returns:_

The contents of the file as a string


_Errors:_

### Security

Raises an error if the path is not a valid file. 

All paths are resolved relative to the user's home directory
The component performs validation to ensure only directories are listed and only files are read. 

### Setting Up

#### Dependencies

Install the FastMCP server

`pip install mcp`

Using a python environment is recommended. 

#### Configure agent: using Claude Desktop

- Open the Settings menu from the tool bar or use the shortcut `Ctrl+,`. 
- Navigate to Developer tab and click `Edit Config`. This will open the parent directory of the `claude_desktop_config.json` file in the file explorer. 

- Add the following to the `claude_desktop_config.json` file. If it does not exist create it. 

```json
{
  "mcpServers": {
    "filesystemHandler": {
      "command": "<absolute path to python executable>",
      "args": ["<absoulet path to>/mcp-filesystem/filesystem-handler.py"]
    }
  }
}
```
Then exit and reopen the Claude Desktop app. 

### Note

The tool is in development and more file system tools are incoming with the goal of enabling the agent to fully handle coding and other tasks similiar to copilot. 
