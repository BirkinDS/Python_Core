from models.flower import Flower


class Peony(Flower):
    def __init__(self, cost=350, lifetime=5):
        super().__init__(name='Пион', cost=cost, lifetime=lifetime)
