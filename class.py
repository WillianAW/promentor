from pydantic import BaseModel

class Pessoa: 
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
        

# adriano = Pessoa('Adriano', 32, 98)

# print(adriano.idade)

class pydPessoa(BaseModel):
    nome: str
    idade: int 
    peso: float
    

adriano = Pessoa(nome='Adriano', idade=32, peso=65)

print(adriano)_