from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carregamento das variáveis de ambiente presentes em .env
load_dotenv()

# Criando o componente de langchain que iterage com os LLMs
model = ChatOpenAI(model="gpt-4o")

### Exemplo 1:
# PART 1: Criando ChatPromptTemplate
print("-----Exemplo Chain 1 -----")

prompt_template = ChatPromptTemplate([
    ("user", "Escreva um script sobre o tema: {assunto}")
]
)

# PART 2: Criando a chain
chain1 = prompt_template | model

# PART 3: Invoke da chain passando as variáveis.
resposta = chain1.invoke({"lingua": "pt-br", "assunto":"pré-atendiento imobiliário"})

print(resposta.content)


### Exemplo 2:
# PART 1: Criando ChatPromptTemplate já com mensagem de sistema:
print("-----Exemplo Chain 2 -----")

mensagens = [
    ("system", "Você é um agent do setor imobiliário"),
    ("human", "Escreva para mim um script sobre {assunto}."),
]

prompt_template = ChatPromptTemplate(mensagens)

# PART 2: Criando a chain
chain2 = prompt_template | model

# PART 3: Invoke da chain passando as variáveis.
resposta = chain2.invoke({"n_versos": "10", "assunto":"imóveis"})

print(resposta.content)
