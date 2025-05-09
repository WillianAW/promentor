from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel

#estanciando uma classe q passa os dados adiante sem fazer nenhuma alteração | transparencia em uma cadeia chain
part_1_runnable = RunnablePassthrough() 

#def function conta_caracteres -> parametro = entrada: dicionario (dict)
def conta_caracteres(entrada:dict) -> int: # retorna um valor inteiro(comprimento da str associada á chave "input")
    return len(entrada["input"])

convert_funcao = RunnableLambda(conta_caracteres)

part_2_runnable = RunnablePassthrough.assign(num_caract=convert_funcao)

#parte 1 o que são runnables e o que são runnableslamda


#parte3 

def transforma(entrada: dict) -> str:
    resultado = entrada["input"] + "Conseguiu"
    return resultado

parte_3_transforma_entrada = RunnableLambda(transforma)
parte_3_passa_p_frente = RunnablePassthrough()

parte_3_runnable = RunnableParallel({
    "transformar_entrada": parte_3_transforma_entrada,
    "passa_p_frente": parte_3_passa_p_frente
})
    

#parte 4 

parte_4_runnable = RunnablePassthrough()

#unindo tudo monsta-se uma cadeia (executavel)
chain = part_1_runnable | part_2_runnable | parte_3_runnable | parte_4_runnable 

#invocar

resposta = chain.invoke({"input": "Parabéns Você "})

print(resposta)