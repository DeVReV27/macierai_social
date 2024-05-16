from crewai_tools import BaseTool

class ContentCreationTool(BaseTool):
    name: str = "Content Creation Tool"
    description: str = "Generates social media posts based on the gathered information."

    def _run(self, info_snippets: str, topic: str) -> str:
        title = f"Latest Insights on {topic}"
        body = f"Here are some interesting facts and insights on {topic}:\n\n{info_snippets}"
        call_to_action = f"Schedule your appointment today:"
        hashtags = f"#{topic.replace(' ', '')} #SocialMedia #Trends"

        post = {
            "title": title,
            "body": body,
            "CTA": call_to_action,
            "hashtags": hashtags
        }
        
        return post
