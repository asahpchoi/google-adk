from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.toolsets.fastmcp import FastMCPToolset

mcp_config = {
    'mcpServers': {
        'chrome-devtools': {
            'command': 'npx',
            'args': ['-y', 
                     'chrome-devtools-mcp@latest', 
                    # '--headless=true', 
                     '--isolated=true'
                    ]
        }
    }
}

provider = GoogleProvider(vertexai=True)
model = GoogleModel('gemini-2.5-flash', provider=provider)
agent = Agent(model, toolsets=[FastMCPToolset(mcp_config)])

async def search_fund(fundname: str, search_url: str = "https://investment.fwd.com.ph/") -> str:
    with open('ops_agent/prompts/search_fund_instruction.txt', 'r') as f:
        instruction = f.read().format(search_url=search_url, fundname=fundname)
    print(instruction)
    try:
        result = await agent.run(instruction)
        return result.output
    except Exception as e:
        return f"An error occurred: {e}"


async def search_doctor(dr_name: str, search_url: str = "https://www.mchk.org.hk/english/list_register/advanced_search.php?type=O") -> str:
    with open('ops_agent/prompts/search_doctor_instruction.txt', 'r') as f:
        instruction = f.read().format(search_url=search_url, dr_name=dr_name)
    print(instruction)
    try:
        result = await agent.run(instruction)
        return result.output
    except Exception as e:
        return f"An error occurred: {e}"
    

async def search_swissre(illness: str, search_url: str = "https://www.mchk.org.hk/english/list_register/advanced_search.php?type=O") -> str:
    with open('ops_agent/prompts/search_swissre_instruction.txt', 'r') as f:
        instruction = f.read().format(search_url=search_url, illness=illness)
    print(instruction)
    try:
        result = await agent.run(instruction)
        return result.output
    except Exception as e:
        return f"An error occurred: {e}"

