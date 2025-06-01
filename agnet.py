from langchain.agents import initialize_agent, Tool
from langchain_core.tools import StructuredTool
from langchain.prompts import PromptTemplate
import asyncio
import os
from webscrape import transform
from searchduck import search
from Rag import add_docs, retrieve
from handler import ThoughtCaptureHandler
from prompt import prompt 

search_tool = Tool(
    name="WebSearch",
    func=search,
    description="Use this to search the web for recent pages related to a topic. Input should be a search query string."
)

# scrape_tool = Tool(
#     name="ScrapeWebpage",
#     func=transform,
#     coroutine=transform,
#     description="Use this to scrape and extract useful text content from a given URL. Input should be a URL string."
    
# )

scrape_tool=Tool(
    func=transform,
    name="ScrapeWebpage",
    description="Use this to scrape and extract useful text content from a given URL. Input should be a URL string.",
    coroutine=transform  
)


store_tool = Tool(
    name="StoreInRAG",
    func=add_docs,
    description="Use this to store a list of documents into the retrieval system. Input should be LangChain Document objects."
)

retrieve_tool = Tool(
    name="RetrieveFromRAG",
    func=retrieve,
    description="Use this to answer a question from stored knowledge. Input should be a question."
)



from langchain_groq import ChatGroq
groq_api_key = os.environ.get("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)



tools = [search_tool, scrape_tool, store_tool, retrieve_tool]

def initagent():
    thoughts=ThoughtCaptureHandler()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        handle_parsing_errors=True,
        callback_manager=[thoughts]
    )
    return agent,thoughts
    






