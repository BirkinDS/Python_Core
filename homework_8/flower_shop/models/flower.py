class Flower:
    def __init__(self, name, cost, lifetime):
        self.name = name
        self.cost = cost
        self.lifetime = lifetime

    def __str__(self):
        return f'{self.name} (ЦЕНА: {self.cost} руб., ВРЕМЯ ЖИЗНИ: {self.lifetime} д.)'
