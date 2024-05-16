import requests
import os
from crewai_tools import BaseTool

class WebBrowsingTool(BaseTool):
    name: str = "Web Browsing Tool"
    description: str = "Performs web searches to gather information on a given topic."

    def _run(self, topic: str) -> str:
        api_key = os.getenv('SERPER_API_KEY')
        url = f'https://api.serper.dev/search?q={topic}'
        
        headers = {
            'X-API-KEY': api_key
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            results = response.json()
            snippets = [item['snippet'] for item in results['organic']]
            return ' '.join(snippets)
        else:
            return "Failed to retrieve information."
