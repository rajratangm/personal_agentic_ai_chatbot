from pydantic import BaseModel

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages:List
    query: str
