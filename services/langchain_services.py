# Setup do LLM, memória e prompt

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

def get_chat_chain():
    llm = ChatOpenAI(
        temperature=0.5,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    memory = ConversationBufferMemory()

    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    return chain
