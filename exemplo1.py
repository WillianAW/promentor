from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

##chat model 

model = ChatOpenAI(model='gpt-4o-mini', temperature=0.1)

conversa = [
    SystemMessage(content="Você é um assistente de imobiliária que faz o pré-atendimento dos clientes que entram em contato")
]


#condição verdadeira até que seja falsa 
while True:
    entrada = input("Entrada Usuário (digite 'q' para parar.):")
    if entrada.lower() == 'q':
        break

    conversa.append(HumanMessage(content=entrada))

    resultado = model.invoke(conversa)
    resposta  = resultado.content
    conversa.append(AIMessage(content=resposta))

    print(f"Resposta AI: {resposta}")

    print(conversa)


    