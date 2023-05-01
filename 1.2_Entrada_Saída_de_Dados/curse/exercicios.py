# Exercicio1: Faça um programa que solicite o nome de uma pessoa
# usuária e imprima-o na vertical.
nome = input("digite seu nome: ")


for index in nome:
    print(index)

# Exercício 2:
numeros = input("insira valores aqui, separados por espaços:")
numeros = numeros.split(" ")

sum = 0
for index in numeros:
    if not index.isdigit():
        print(f"ERROR AO SOMAR VALORESM, {index} NÃO É UM NÚMERO")
    else:
        sum += int(index)

print(f"A soma dos valores é: {sum}")
