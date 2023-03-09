from base_config import *

from data import (
    ingredients_models_data, 
    dishes_models_data,
    dish_ingredients
)

from create_user import create_test_users
from create_menu import create_menu


def main():

    if Ingredient.objects.count() > 0 or not settings.CREATE_TEST_DATA:
        return

    Ingredient.objects.bulk_create(ingredients_models_data) # creating ingredients data
    Dish.objects.bulk_create(dishes_models_data) # creating dishes data

    DishIngridient.objects.bulk_create(dish_ingredients) # creating dish_ingredients

    create_test_users()
    create_menu()

    print('Test data has been created!')

if __name__ == '__main__':
    main()
