from abc import ABC, abstractmethod
from math import pi as PI
from collections import Counter


#  Exercício 1: Implemente a classe com base no diagrama
class Tv:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def __aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def __diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if canal <= 1 or canal >= 99:
            raise ValueError('Canal indisponível')

        self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada

# exercicio 2 -  Implemente uma classe Estatistica


class Estatistica:
    def __init__(self, numbers):
        self.numbers = numbers

    def media(self):
        return sum(self.numbers) / len(self.numbers)

    def mediana(self):
        numbers = sorted(self.numbers)
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index]) / 2

        return numbers[index]

    def moda(self):
        number, _ = Counter(self.numbers).most_common()[0]
        return number


# Exercício 3: Implemente as classes das figuras geométricas


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimetro(self):
        raise NotImplementedError


class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado


class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return PI * self.raio * self.raio

    def perimetro(self):
        return 2 * PI * self.raio
