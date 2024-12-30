from pydantic import BaseModel

class UserResults(BaseModel):
    question_list: list[str]

class ItemResults(BaseModel):
    response: str