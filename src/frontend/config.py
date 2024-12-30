from starlette.config import Config

APP_VERSION = "0.0.1"
APP_NAME = "LawBot_front"

config = Config(".env") 


SUGGEST_QUESTION_ENDPOINT: str = config("SUGGEST_QUESTION_ENDPOINT")
QUESTION_ANSWER_ENDPOINT: str = config("QUESTION_ANSWER_ENDPOINT")