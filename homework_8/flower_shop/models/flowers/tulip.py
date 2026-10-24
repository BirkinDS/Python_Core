from models.flower import Flower


class Tulip(Flower):
    def __init__(self, cost=100, lifetime=5):
        super().__init__(name='Тюльпан', cost=cost, lifetime=lifetime)
