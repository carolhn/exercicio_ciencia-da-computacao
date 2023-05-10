from abc import ABC, abstractmethod


class Navigator:
    def __init__(self, navegator_strategy):
        self._navegator_strategy = navegator_strategy

    def build_route(self, departure, arrival):
        return self._navegator_strategy.build_route(departure, arrival)


class NavigatorStrategy(ABC):
    @classmethod
    @abstractmethod
    def build_route(self):
        raise NotImplementedError


class WalkStrategy(NavigatorStrategy):
    @classmethod
    def build_route(self, departure, arrival):
        return f"Rota a pé de {departure} até {arrival}"


class BikeStrategy(NavigatorStrategy):
    @classmethod
    def build_route(self, departure, arrival):
        return f"Rota de bicileta de {departure} até {arrival}"


class BussStrategy(NavigatorStrategy):
    @classmethod
    def build_route(self, departure, arrival):
        return f"Rota de buss de {departure} até {arrival}"


class CarStrategy(NavigatorStrategy):
    @classmethod
    def build_route(self, departure, arrival):
        return f"Rota de carro de {departure} até {arrival}"


Navigator(WalkStrategy).build_route("Casa", "Trabalho")
Navigator(BikeStrategy).build_route("Casa", "Trabalho")
Navigator(BussStrategy).build_route("Casa", "Trabalho")
Navigator(CarStrategy).build_route("Casa", "Trabalho")
