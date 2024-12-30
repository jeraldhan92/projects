import sys
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from core.config import CHAIN_VERSION, CHAIN_KEY


class OpenAIConnector:
    def __init__(self, cfg):
        self._cfg = cfg
        try:
            self._load_model()
        except Exception as e:
            print(e)
            print("Unable to load openai model")
            sys.exit()

    def _load_model(self):
        """
        Load openai models.
        """
        selected_openai_model = self._cfg["openai"]["selector"]
        selected_embedding_model = self._cfg["embedding"]["selector"]

        if selected_openai_model == "gpt3.5":
            openai_version = "gpt3.5"
            base_url = self._cfg["endpoint"]
            deployment_type = self._cfg["openai"][openai_version]["model"]
            maximum_token = self._cfg["openai"][openai_version]["max_tokens"]
            temperature = self._cfg["openai"][openai_version]["temperature"]
            top_p = self._cfg["openai"][openai_version]["top_p"]

            self.chat_model = ChatOpenAI(
                openai_api_key=CHAIN_KEY,
                model=deployment_type,
                max_tokens=maximum_token,
                temperature=temperature,
                top_p=top_p,
            )

        if selected_embedding_model == "embedding-3-small":
            embedding_version = "embedding-3-small"
            embedding_type = self._cfg["embedding"][embedding_version]["model"]

            self.embedding_model = OpenAIEmbeddings(
                openai_api_key=CHAIN_KEY, model=embedding_type
            )


# Testing ..
if __name__ == "__main__":
    conn = OpenAIConnector()
    chat = conn.chat_model

    messages = [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."
        ),
        HumanMessage(
            content="Translate this sentence from English to French. I love programming."
        ),
    ]
    print(chat.invoke(messages))

    embedding = conn.embedding
    print(embedding.embed_query("What is my name?")[:5])
