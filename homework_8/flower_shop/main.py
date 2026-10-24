from models import Bouquet, Rose, Tulip, Peony, Lily, Orchid, Accessory


def print_header(title):
    line = '=' * 50
    print(f'\n{line}')
    print(f'  {title}')
    print(f'{line}')


def print_section(title):
    print(f'\n--- {title} ---')


def main():
    print_header('СБОР БУКЕТА')

    my_bouquet = Bouquet()

    print_section('Добавление цветов')
    my_bouquet.add_flower(Rose())
    my_bouquet.add_flower(Tulip())
    my_bouquet.add_flower(Peony())
    my_bouquet.add_flower(Lily())
    my_bouquet.add_flower(Orchid())

    print_section('Добавление аксессуаров')
    my_bouquet.add_accessory(Accessory('Глянцевая упаковка', 50))
    my_bouquet.add_accessory(Accessory('Ленточка', 30))

    print_section('Состав букета')
    my_bouquet.show_bouquet()

    print_section('Стоимость')
    print(f'  Итоговая цена букета: {my_bouquet.get_total_cost()} руб.')

    print_section('Время жизни')
    print(f'  Среднее время жизни цветов в букете: {my_bouquet.get_withering_time()} дней')

    print_section('Проверка наличия цветов')
    checks = ['Роза', 'Лилия', 'Пион', 'Тюльпан', 'Орхидея']
    for name in checks:
        result = 'да' if my_bouquet.find_flower(name) else 'нет'
        print(f'  {name:<10} -> {result}')

    print_section('Сортировка по цене')
    my_bouquet.sort_flowers_by_cost()
    for flower in my_bouquet.flowers:
        print(f'  {flower.name:<10} - {flower.cost:>4} руб.')

    print(f'\n{"=" * 50}\n')


if __name__ == '__main__':
    main()
