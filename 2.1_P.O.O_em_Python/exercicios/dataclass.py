# @dataclass permite criar classes com menos código
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float


flavio = Pessoa("Flavio", 37, 1.8)
print(flavio)
print(flavio.nome)
print(flavio.idade)
print(flavio.altura)
