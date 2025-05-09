from operator import itemgetter


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini", temperature = 0.1)

prompt_template_inicial=ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um agente especialista em pré-atendimento imobiliário")
        ("user", "")
    ]
)


