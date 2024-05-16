import os
from crewai_tools import BaseTool

class AuthenticationTool(BaseTool):
    name: str = "Authentication Tool"
    description: str = "Handles secure authentication by reading credentials for different platforms from environment variables."

    def _run(self, platform: str) -> str:
        username = os.getenv(f'{platform.upper()}_USERNAME')
        password = os.getenv(f'{platform.upper()}_PASSWORD')
        
        if username and password:
            session = f"Session started for {platform} user {username} with token xxxxxxxx"
            return session
        else:
            return f"Authentication failed for {platform}: Missing credentials."
