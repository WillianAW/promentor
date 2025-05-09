from langchain.agents import tool

@tool

def retorna_temperatura_atual(lacalidade: str):
    '''Faz busca online de temperatura de uma localidade'''
    return '25°C'

retorna_temperatura_atual


retorna_temperatura_atual.name