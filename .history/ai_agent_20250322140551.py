import os 

GROQ_API_KEY= os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY= os.environ.get('TAVILY_API_KEY')
OPENAI_API_KEY= None 


 from langchain_groq import ChatGroq 
 from langchain_community.tools.tavily_search import TavilySearchResults 
 
 groq_llm = ChatGroq(model='deepseek-r1-distill-qwen-32b')

 search = TavilySearchResults(max_results=5, api_key=TAVILY_API_KEY)


 from langgraph.prebuilt import create_react_agent 

 agent = create_react_agent(groq_llm, 
 
 
 )