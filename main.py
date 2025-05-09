from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os


# 🔑 LLM configurado
llm = ChatOpenAI(model="gpt-4o", temperature=0)
parser = JsonOutputParser()

# 🎯 Prompt atualizado com "localizacao"
prompt = ChatPromptTemplate.from_template("""
Você é um assistente de uma imobiliária.
Classifique os elementos da seguinte mensagem do cliente nas categorias:

- tipo_imovel: apartamento, casa, sala comercial, etc.
- operacao: alugar, comprar ou vender
- valor: valores mencionados (ex: até 2000, 500 mil)
- caracteristicas: número de quartos, varanda, vagas, metragem etc.
- localizacao: bairro, cidade, região, zona ou ponto de referência

Mensagem:
"{mensagem}"

Responda SOMENTE em JSON com essas 5 chaves.
""")

# 🔗 Monta a chain
chain = prompt | llm | parser

# 💬 Início da conversa
def classificar_mensagem():
    print("\n🤖 Olá, sou Mia, assistente virtual da Exemplo Imob!")
    print("Em que posso ajudá-lo?\n")

    entrada = input("👤 Você: ")
    resultado = chain.invoke({"mensagem": entrada})

    resultado = completar_classificacao_vazia(resultado)

    print("\n📋 Aqui está o que eu entendi:")
    for chave, valor in resultado.items():
        print(f"🔹 {chave.replace('_', ' ').capitalize()}: {valor.strip().capitalize()}")

# 🧠 Verifica campos vazios e pergunta ao cliente
def completar_classificacao_vazia(resultado: dict) -> dict:
    perguntas = {
        "tipo_imovel": "Qual o tipo de imóvel que você procura? (Ex: apartamento, casa, sala comercial)",
        "operacao": "Você quer alugar, comprar ou vender o imóvel?",
        "valor": "Qual é o valor aproximado que pretende pagar ou investir?",
        "caracteristicas": "Pode me informar alguma característica do imóvel? (quartos, metragem, etc.)",
        "localizacao": "Qual bairro ou região você tem preferência?"
    }

    for campo, pergunta in perguntas.items():
        if campo not in resultado or not resultado[campo] or resultado[campo].strip() == "":
            resposta_usuario = input(f"🤖 {pergunta}\n👤 Você: ")
            nova_classificacao = chain.invoke({"mensagem": resposta_usuario})
            resultado[campo] = nova_classificacao.get(campo, "")

    return resultado

if __name__ == "__main__":
    classificar_mensagem()
