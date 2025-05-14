from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("FilesystemHandler")


@mcp.tool()
def list_files(path: str) -> list:
    """
    List all files in a directory.
    """
    home_dir = os.environ.get("HOME")
    print(f"Home directory: {home_dir}")
    full_path = os.path.join(home_dir, path)
    if not os.path.isdir(full_path):
        raise ValueError(f"Path {full_path} is not a directory.")

    files = os.listdir(full_path)
    return files


@mcp.tool()
def read_file(path: str) -> str:
    """
    Read the contents of a file.
    """
    home_dir = os.environ.get("HOME")
    print(f"Home directory: {home_dir}")
    full_path = os.path.join(home_dir, path)
    if not os.path.isfile(full_path):
        raise ValueError(f"Path {full_path} is not a file.")

    with open(full_path, "r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    mcp.run(transport="stdio")
