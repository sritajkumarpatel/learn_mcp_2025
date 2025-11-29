from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List

# Create Server
mcp = FastMCP("Other Inputs")

class Person(BaseModel):
    name: str = Field(..., description="The person's full name")
    age: int = Field(..., description="The person's age in years")
    email: str = Field(..., description="The person's email address")
    years_of_experience: int = Field(..., description="Years of professional experience")

@mcp.tool()
def process_person(person: Person) -> str:
    """
    Process a single person and save their details to log.txt.
    
    If log.txt does not exist, it will be created. If it exists, its contents will be cleared before writing the new data.
    
    Args:
        person: A Person object containing name, age, email, and years_of_experience.
    
    Returns:
        A confirmation message indicating the save was successful.
    """
    try:
        with open('log.txt', 'w') as f:
            f.write(f"Name: {person.name}\n")
            f.write(f"Age: {person.age}\n")
            f.write(f"Email: {person.email}\n")
            f.write(f"Years of Experience: {person.years_of_experience}\n")
        return f"Successfully saved details for {person.name} to log.txt."
    except Exception as e:
        return f"Error saving to log.txt: {str(e)}"

if __name__ == "__main__":
    mcp.run()