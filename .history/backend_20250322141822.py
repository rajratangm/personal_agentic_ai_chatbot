from pydantic import BaseModel

class RequestState(BaseModel):
    state: str