import os 

GROQ_API_KEY= os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY= os.environ.get('TAVILY_API_KEY')
OPENAI_API_KEY= None 


from langchain_groq import ChatGroq 
from langchain_community.tools.tavily_search import TavilySearchResults 

groq_llm = ChatGroq(model='deepseek-r1-distill-qwen-32b')

search = TavilySearchResults(max_results=5, api_key=TAVILY_API_KEY)


from langgraph.prebuilt import create_react_agent 
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_se)
system_prmpt = 'act as an AI chatbot who is smart and friendly'
agent = create_react_agent(model=groq_llm, 
tools=[search],
state_modifier=system_prmpt

)

query = 'who is author name rajratan more also know as r.g.morey?'
state={'message': query}
response = agent.invoke(state)
messages = response.get('messages')
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages)