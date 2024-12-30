import yaml
from common.gpt import OpenAIConnector
from common.question_answering import QA_Agent
from common.question_generator import QuestionGenerator
from fastapi import HTTPException
from interface.payload import Payload, Profile
from interface.response import ItemResults, UserResults


class Predict:
    def __init__(self, cfg_filepath):
        self._cfg = None

        with open(cfg_filepath, "r") as ymlfile:
            self._cfg = yaml.safe_load(ymlfile)

        self.open_ai_connector = OpenAIConnector(self._cfg)

    def process_profile(self, payload: Profile):
        # Generate question list
        if payload is None:
            raise HTTPException(status_code=422, detail="Request payload is empty")

        # Load GPT model
        question_generator = QuestionGenerator(
            chat_model=self.open_ai_connector.chat_model, profile=payload
        )
        question_list = question_generator.generate_questions()
        
        return UserResults(question_list=question_list)

    def process_questions(self, payload: Payload):
        # Generate answer based on question
        if payload is None:
            raise HTTPException(status_code=422, detail="Request payload is empty")

        # Debugging ...
        # print(payload.profile, payload.question)

        question_answer_agent = QA_Agent(
            model=self.open_ai_connector.chat_model,
            embedding=self.open_ai_connector.embedding_model,
            profile=payload.profile,
            question=payload.question,
            dir_path="./services/",
        )

        response = question_answer_agent.respond()

        return ItemResults(response=response)
