from models.flower import Flower


class Rose(Flower):
    def __init__(self, cost=150, lifetime=7):
        super().__init__(name='Роза', cost=cost, lifetime=lifetime)
