from common.format_profile import format_profile_message
from langchain.output_parsers import NumberedListOutputParser
from langchain_core.messages import HumanMessage, SystemMessage


class QuestionGenerator:
    def __init__(self, chat_model, profile):
        self.chat_model = chat_model
        self.profile = profile

    def generate_questions(self):
        output_parser = NumberedListOutputParser()
        format_instructions = output_parser.get_format_instructions()
        profile_message = format_profile_message(self.profile)
        human_message = (
            profile_message + "What questions should I ask about employment law."
        )
        human_message += "\n"
        human_message += format_instructions
        messages = [
            SystemMessage(
                content="You are a helpful Law Advisor bot. "
                "Given sentences describing the client's profile,"
                "list some questions about employment law that the client may ask."
            ),
            HumanMessage(content=human_message),
        ]
        question_list = output_parser.parse(self.chat_model.invoke(messages).content)
        return question_list


# test

from langchain_openai import ChatOpenAI

if __name__ == "__main__":

    class Profile:
        name = "Mary"
        age = 25
        employment_status = "Employer"
        occupation = "Software Engineer"
        industry = "Tech"

    OPENAI_API_KEY = "insert open api key"
    model_name = "gpt-3.5-turbo"
    chat_model = ChatOpenAI(
        temperature=0, openai_api_key=OPENAI_API_KEY, model_name=model_name
    )
    question_generator = QuestionGenerator(chat_model=chat_model, profile=Profile())
    question_list = question_generator.generate_questions()
    print(question_list)
