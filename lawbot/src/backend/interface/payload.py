from pydantic import BaseModel


class Profile(BaseModel):
    name: str 
    age: int 
    employment_status: str
    occupation: str
    industry: str

class Payload(BaseModel):
    profile: Profile | None = None
    question: str | None = None