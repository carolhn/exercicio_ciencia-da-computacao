from dataclasses import dataclass


@dataclass
class Address:
    # Podemos colocar um valor padrão
    street = "Street"
    number = 0
    # Ou especificar o tipo do campo com anotações de tipo
    district: str


address = Address(district="District")

print(address.street, address.number, address.district)
# Street 0 District

# A classe Address sugerida anteriormente serve basicamente para salvar dados.
# Ela não possui vários métodos e comporta-se como um repositório de dados,
#  tornand sua semântica um pouco diferente daquela com qual já nos habituamos.

# Convém ressaltar que as dataclasses também podem conter métodos,
#  dispor de herança, composição e outros conceitos comuns à orientação a obj
