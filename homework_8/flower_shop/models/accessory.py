class Accessory:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f'Аксессуар: {self.name} ({self.cost} руб.)'

    def __repr__(self):
        return self.__str__()
