from pydantic import BaseModel
from typing import List 
from ai_agent import get_response_from_ai_agent
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


from fastapi import FastAPI

app=FastAPI(title='LangGraph AI Agent')
ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]
@app.post('/chat')
def chat_endpoint(request: RequestState):

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {'error': 'Invalid model name'}
    
    response =get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )
    return response
    
if __name