from google.adk.agents.llm_agent import Agent
from .tool import search_fund, search_doctor, search_swissre
from google.adk.tools import FunctionTool

search_fund_tool = FunctionTool(func=search_fund)
search_doctor_tool = FunctionTool(func=search_doctor)
search_swissre_tool = FunctionTool(func=search_swissre)

with open('ops_agent/prompts/root_agent_instruction.txt', 'r') as f:
    instruction = f.read()

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for answering questions about financial funds and doctor registration.',
    instruction=instruction,
    tools = [search_fund_tool, search_doctor_tool, search_swissre_tool]
)
