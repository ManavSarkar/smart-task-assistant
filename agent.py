from .mytools.web_scrapper import web_scrapper
from .mytools.todo import add_todo, list_todos
from google.adk.agents import LlmAgent
import os
from dotenv import load_dotenv

load_dotenv() 

web_researcher_agent = LlmAgent(
    model = "gemini-2.0-flash",
    name = "web_researcher",
    description="An agent that can search the web and extract information from it.",
    instruction="You are a web researcher. You can search the web and extract information from it. Use the tool to search the web for information and extract it. You can also add to-do items to your list. You can also list your to-do items. You can also search the web for information and extract it, and summarize it.",
    tools=[web_scrapper],
    disallow_transfer_to_peers=False,
)

todo_manager_agent = LlmAgent(
    model = "gemini-2.0-flash",
    name = "todo_manager",
    description="An agent that can manage your to-do list.",
    instruction="You are a to-do manager. You can add to-do items to your list. You can also list your to-do items.",
    tools=[add_todo, list_todos],
    disallow_transfer_to_peers=False,
)

root_agent = LlmAgent(
    model = "gemini-2.0-flash",
    name = "root_agent",
    instruction="""
    You are a smart personal assistant. You acccomplish various tasks by using specialized agents.
    - You can use the Web Researcher agent to search the web and extract information from it. Then present a summary of the information.
    - You can use the To-Do Manager agent to manage your to-do list such as adding and viewing todos.
    - Present the results in a clear and concise manner.
    """,
    sub_agents=[web_researcher_agent, todo_manager_agent],
)