#variaveis de ambiente
from dotenv import load_dotenv
load_dotenv()

#importações 

from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# class rota erda todas as bases de todos os modelos Pydantic
# class rota permite: validar dados automaticamente
# class rota permite: conversão para js
# class rota permite: Langchain para estruturar inputs e output em runnables, agents, ou api 

class Rota(BaseModel):
    escolha: int=Field(description="Rota escolhida")#define o campo escolha do tipo int(field usadao para adicionar o metado[description])
    pensamento: str=Field(description="Campo para o pensamento que levou a decisão da rota escolhida")
    #description é usado quando se gera schema de entrada de ferramentas

#criando o analisador de saida 
