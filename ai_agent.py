# set api key
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")


# set LLM or tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality

system_prompt="Act as an AI chatbot who is smart and friendly"

 agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )