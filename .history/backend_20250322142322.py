from pydantic import BaseModel
from typing import List 
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


from fastapi import FastAPI

app=FastAPI(title='LangGraph AI Agent')
ALLOWED_MODEL_NAMES=[]
@app.post('/chat')
def chat_endpoint(request: RequestState):

