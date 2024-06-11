import os
import re

import dotenv
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_openai_tools_agent
from langchain.chains import RetrievalQA
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from pydantic.v1 import BaseModel, Field

from common.format_profile import format_profile_message


class DocumentInput(BaseModel):
    question: str = Field()


class QA_Agent:
    def __init__(self, model, embedding, profile, question: str, dir_path: str) -> None:
        self.model = model
        self.embeddings = embedding
        self.profile = profile
        self.question = question
        self.data_dir = dir_path

    def generate_tools(self) -> Tool:
        """Generates tools object to be passed as parameter in agent initalization function.

        Returns:
            Tool: Tools object
        """
        tools = []
        pdf_files = [
            file for file in os.listdir(self.data_dir) if file.lower().endswith(".pdf")
        ]

        for i in pdf_files:
            file_path = self.data_dir + i
            loader_pdf = PyPDFLoader(file_path)
            pages = loader_pdf.load_and_split()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            docs = text_splitter.split_documents(pages)
            retriever = Chroma.from_documents(docs, self.embeddings).as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5},
                return_source_documents=True,
            )
            tools.append(
                Tool(
                    args_schema=DocumentInput,
                    name=re.match(r"^[^.]*", i).group(0),
                    description=f"useful when you want answers on {i}",
                    func=RetrievalQA.from_chain_type(
                        llm=self.model, retriever=retriever, chain_type="stuff"
                    ),
                )
            )

        return tools

    def create_agent(self) -> AgentExecutor:
        """Creates Agent Executor to generate responses.

        Returns:
            AgentExecutor: Executor to generate responses
        """
        tools = self.generate_tools()
        prompt = hub.pull("hwchase17/openai-tools-agent")

        agent_obj = create_openai_tools_agent(self.model, tools, prompt)
        agent_executor = AgentExecutor(agent=agent_obj, tools=tools)
        return agent_executor

    def respond(self) -> str:
        agent_exec = self.create_agent()
        profile_message = format_profile_message(self.profile)
        return agent_exec.invoke({"input": profile_message + self.question})["output"]
