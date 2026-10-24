from models.flower import Flower


class Lily(Flower):
    def __init__(self, cost=300, lifetime=10):
        super().__init__(name='Лилия', cost=cost, lifetime=lifetime)
