from random import choice

from base_config import *

from apps.menu.models import Menu, DishMenu

from apps.users.models import User

from apps.dishes.models import Dish


def create_menu():
    users = User.objects.filter(id__gt=1)
    dishes = Dish.objects.all()

    menu_data = []
    menu_dishes = []

    days = (
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    )
    eating_times = (
        'Завтрак',
        'Обед',
        'Ужин'
    )


    for user in users:
        data = {
            "user": user,
            "day_of_week": choice(days),
        }
        menu_data.append(data)

    menu = [Menu(**data) for data in menu_data]

    menus = Menu.objects.bulk_create(menu)


    for menu in menus:
        for eating_time in eating_times:
            data =  {
                'menu': menu,
                'dish': choice(dishes),
                'eating_time': eating_time
            }
            menu_dishes.append(data)

    menu_dishes_data = [DishMenu(**data) for data in menu_dishes]

    DishMenu.objects.bulk_create(menu_dishes_data)


if __name__ == '__main__':
    create_menu()
