from crewai import Agent, Task, Crew
from tools.authentication_tool import AuthenticationTool
from tools.web_browsing_tool import WebBrowsingTool
from tools.content_creation_tool import ContentCreationTool

# Authentication Tool and Agent
authentication_tool = AuthenticationTool()
auth_agent = Agent(
    role='Authenticator',
    goal='Securely log in using credentials stored in environment variables.',
    tools=[authentication_tool],
    verbose=True
)
auth_task = Task(
    description="Authenticate to social media platforms securely.",
    expected_output="Session details or error message.",
    tools=[authentication_tool],
    agent=auth_agent
)

# Web Browsing Tool and Agent
web_browsing_tool = WebBrowsingTool()
web_browsing_agent = Agent(
    role='Researcher',
    goal='Gather relevant information on the given topic by performing web searches.',
    tools=[web_browsing_tool],
    verbose=True
)
web_browsing_task = Task(
    description="Perform a web search to gather information on the topic.",
    expected_output="A comprehensive set of information snippets related to the topic.",
    tools=[web_browsing_tool],
    agent=web_browsing_agent
)

# Content Creation Tool and Agent
content_creation_tool = ContentCreationTool()
content_creation_agent = Agent(
    role='Content Creator',
    goal='Create compelling social media posts based on the gathered information.',
    tools=[content_creation_tool],
    verbose=True
)
content_creation_task = Task(
    description="Use the gathered information to create a social media post.",
    expected_output="A formatted social media post including title, body, and hashtags.",
    tools=[content_creation_tool],
    agent=content_creation_agent
)

# Initialize Crew with agents and tasks
social_media_crew = Crew(
    agents=[auth_agent, web_browsing_agent, content_creation_agent],
    tasks=[auth_task, web_browsing_task, content_creation_task]
)

def kickoff(topic, platform):
    inputs = {'topic': topic, 'platform': platform}
    result = social_media_crew.kickoff(inputs)
    return result
