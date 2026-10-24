from models.flower import Flower


class Orchid(Flower):
    def __init__(self, cost=250, lifetime=14):
        super().__init__(name='Орхидея', cost=cost, lifetime=lifetime)
