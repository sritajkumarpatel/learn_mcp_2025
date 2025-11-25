from mcp.server.fastmcp import FastMCP
import os

# Initialize the MCP server for managing local notes
mcp = FastMCP("Local Notes")

@mcp.tool()
def add_note(content: str) -> str:
    """
    Add a note with the given content.
    
    This function writes the provided content to notes.txt, replacing any existing content.
    
    Args:
        content: The content of the note to add
        
    Returns:
        A confirmation message indicating the note was added
    """
    file_path = "notes.txt"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist")
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return f"Note added: {content}"

@mcp.tool()
def get_notes() -> str:
    """
    Retrieve all notes from the notes file.
    
    Returns:
        A string containing all notes, or a message if no notes exist
    """
    file_path = "notes.txt"
    
    if not os.path.exists(file_path):
        return "No notes found."
    
    with open(file_path, 'r') as f:
        notes = f.read()
    
    return notes

if __name__ == "__main__":
    # Start the MCP server and listen for requests
    mcp.run()
    