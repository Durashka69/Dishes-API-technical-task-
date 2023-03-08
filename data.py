from random import choice

from base_config import *


ingredients = [
    {"title": "Картофель"},
    {"title": "Морковь"},
    {"title": "Лук"},
    {"title": "Чеснок"},
    {"title": "Помидор"},
    {"title": "Огурец"},
    {"title": "Капуста"},
    {"title": "Перец"},
    {"title": "Сельдерей"},
    {"title": "Баклажан"},
    {"title": "Кукуруза"},
    {"title": "Грибы"},
    {"title": "Свекла"},
    {"title": "Фасоль"},
    {"title": "Горох"},
]

dishes = [
    {
        "title": "Борщ",
        "description": "Классический украинский суп",
    },
    {
        "title": "Оливье",
        "description": "Салат с картофелем, морковью и майонезом",
    },
    {
        "title": "Салат Цезарь",
        "description": "Салат с курицей, сыром и гренками",
    },
    {
        "title": "Пицца",
        "description": "Итальянская пицца с салями и грибами",
    },
    {
        "title": "Картофель по-деревенски",
        "description": "Традиционное блюдо русской кухни. Сочный и ароматный картофель, запеченный с луком, чесноком и специями",
    },
    {
        "title": "Салат с овощами и грибами",
        "description": "Легкий и свежий салат, приготовленный из свежих овощей и шампиньонов",
    },
    {
        "title": "Суп с фасолью и грибами",
        "description": "Плотный и насыщенный суп с фасолью и грибами",
    },
]


dish_ingredients_data = [
    [
        {"weight": 500},
        {"weight": 300},
        {"weight": 50},
        {"weight": 400},
        {"weight": 200},
        {"weight": 10},
    ],
    [
        {"weight": 300},
        {"weight": 200},
        {"weight": 100},
        {"weight": 200},
        {"weight": 20},
        {"weight": 5},
        {"weight": 50},
    ],
    [
        {"weight": 200},
        {"weight": 50},
        {"weight": 200},
        {"weight": 5},
        {"weight": 50},
        {"weight": 30},
        {"weight": 50},
    ],
    [
        {"weight": 300},
        {"weight": 100},
        {"weight": 5},
        {"weight": 50},
        {"weight": 30},
        {"weight": 100},
        {"weight": 20},
        {"weight": 50},
    ],
    [
        {"weight": 500},
        {"weight": 100},
        {"weight": 50},
        {"weight": 10},
    ],
    [
        {"weight": 200},
        {"weight": 100},
        {"weight": 100},
        {"weight": 50},
        {"weight": 50},
    ],
    [
        {"weight": 300},
        {"weight": 150},
        {"weight": 100},
        {"weight": 50},
    ],
]


ingredients_models_data = [Ingredient(**ingredient) for ingredient in ingredients]
dishes_models_data = [Dish(**dish) for dish in dishes]

dish_ingrs = []


for ingredient_arr in dish_ingredients_data:
    for dish_ingr in ingredient_arr:
        dish_ingr.update({'ingredient': choice(ingredients_models_data)})
        dish_ingrs.append(dish_ingr)


for dish in dish_ingrs:
    dish.update({"dish": choice(dishes_models_data)})


dish_ingredients = [DishIngridient(**data) for data in dish_ingrs]


if __name__ == "__main__":
    print(dish_ingredients)
