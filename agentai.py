from langchain.pydanc_v1 import BaseModel, Field
from typing import List


text='''
    A apple foi fundada em 1 de abril de 1976 por Steve Wozniak, Steve Jobs e Ronald Wayne com o nome de Apple 
    Computers, na Califórnia. O nome foi escolhido por Jobs após a visita do pomar de maças da fazendo Robert 
    Frieland também pelo fato do nome soar bem e ficar antes do Atari nas listas telefônicas.
    
    O primeiro protótipo da empresa foi a Apple que foi demonstrada na Home brew Computer Club em 1975, as vendas 
    começaram em julho de de 1976 com o preço  de U$ 666,66 aproximadamente 200 unidades foram vendidas, [21] em 1977 
    a empresa conseguiu a porte de mike markkula  
'''

class Acontecimento(BaseModel):
    '''Informação sobre um acontecimento'''
    data: str = Field(description='Data do acontecimento')
    acontecimento = Field(description='Acontecimento extraido do texto')
    

class ListaAcontecimento(BaseModel):
    """Aconteceu a extração"""
    acontecimentos: List[Acontecimento] = Field(description='Acontecimento extraido do texto')


    
    
    


 