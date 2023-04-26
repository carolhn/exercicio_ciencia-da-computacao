# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def max_number(n1, n2):
    return n1 if n1 > n2 else n2


print(max_number(10, 20))


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def average(list):
    average_list = sum(list) / len(list)
    return int(average_list)


print(average([1, 2, 3, 4, 5]))


# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n
def square(n):
    for i in range(n):
        print('*' * n)


print(square(2))


#  Exercício 4: Crie uma função que receba uma lista de nomes e retorne o
#  nome com a maior quantidade de caracteres. Por exemplo, para
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
# o retorno deve ser "Fernanda".

def lista_name(list):
    name = list[0]
    for i in list:
        if len(i) > len(name):
            name = i
    return name


print(lista_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))


# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3
#  metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a
# quantidade de latas de tinta a serem compradas e o preço total a partir do
#  tamanho de uma parede (em m²).
import math


def extencoes(metros):
    litro = metros / 3
    vendidoLata = 80
    quantidadeLata = math.ceil(litro / 18)
    preco = quantidadeLata * vendidoLata
    return quantidadeLata, preco


print(extencoes(100))


# Exercício 6: Crie uma função que receba os três lado de um triângulo e
#  informe qual o tipo de triângulo formado ou "não é triangulo",
#  caso não seja possível formar um triângulo.
def type_of_triangle(side1, side2, side3):
    is_triangle = (
            side1 + side2 > side3 and
            side2 + side3 > side1 and
            side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"


print(type_of_triangle(10, 10, 20))
