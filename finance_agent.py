from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv

Groq.api_key=os.getenv("GROQ_API_KEYs")

##agent for web search purpose
Web_search_agent= Agent(
    name="Web Search Agent",
    role="search the web for the information",
    model = Groq(id="llama3-8b-8192"),
    tools=[DuckDuckGo()], #whenever there is a query the model will go to duckduckgo using groq
    instructions=["Always Include the sources"],# saying that where it fetches have to be included#
    markdown=True,
)

##financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model = Groq(id="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True, #this basically shows what are the tools are present
    markdown=True,   
)

#create multi moodel to integrate agent 1 and agent 2 in same
multi_model_agent=Agent(
    team=[Web_search_agent,finance_agent],
    instructions=["Always Include the sources","Use tables to display the data"],
    model=Groq(id="llama3-8b-8192"),
    #show_tool_calls=True,
    markdown=True,

)
