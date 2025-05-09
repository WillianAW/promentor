

from langchain_core.runnables import RunnablePassthrough, RunnableLambda

def entrada_para_letras_maiusculas(entrada: str):
    saida = entrada.upper()
    return saida

chain = RunnablePassthrough () | RunnableLambda(entrada_para_letras_maiusculas) | RunnablePassthrough()

resposta0 = chain.invoke("olá")

print(resposta0)


runnable = RunnablePassthrough() | RunnablePassthrough.assign(multiplica_3=lambda x: x["num"]*3)

resposta = runnable.invoke({"num":1})

print(resposta)