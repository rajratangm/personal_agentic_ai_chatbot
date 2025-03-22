from pydantic import BaseModel

class RequestState(BaseModel):
    model_name: str
    model_provider
    query: str
