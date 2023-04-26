languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# um loop for geralmente é escrito como um loop sobre um objeto iterável.
# Isso significa que você não precisa de uma variável de contagem para acessar
#  itens no iterável.

# Você também pode desestruturar (unpack) os itens da lista ou tupla:
for index, language in enumerate(['Python', 'Java']):
    print(f'{index} - {language}')

#  A letra f usada dentro do print é chamada de f-string. Ela fornece uma
# maneira de incorporar expressões dentro de strings literais, usando uma
# sintaxe mínima.
