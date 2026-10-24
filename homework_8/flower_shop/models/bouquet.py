from models.flower import Flower
from models.accessory import Accessory


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)
        print(f'Добавлен цветок {flower.name}.')

    def add_accessory(self, accessory: Accessory):
        self.accessories.append(accessory)
        print(f'Добавлен аксессуар {accessory.name}.')

    def get_total_cost(self):
        total_cost = sum(flower.cost for flower in self.flowers)
        total_cost += sum(acc.cost for acc in self.accessories)
        return total_cost

    def get_withering_time(self):
        if not self.flowers:
            return 0
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        average = total_lifetime / len(self.flowers)
        return round(average, 1)

    def sort_flowers_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.cost)
        print('Сортировка цветов по стоимости выполнена.')

    def find_flower(self, name):
        for flower in self.flowers:
            if flower.name.lower() == name.lower():
                return True
        return False

    def show_bouquet(self):
        print('Букет:')
        if not self.flowers and not self.accessories:
            print('Отсутствуют данные для сбора букета')
            return
        for flower in self.flowers:
            print(f'  {flower}')
        for acc in self.accessories:
            print(f'  {acc}')
