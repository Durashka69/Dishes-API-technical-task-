from rest_framework import serializers

from apps.dishes.models import (
    Ingredient, 
    Dish, 
    DishIngridient, 
)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "id", 
            "title"
        )


class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient_title = serializers.ReadOnlyField(source="ingredient.title")
    dish_title = serializers.ReadOnlyField(source="dish.title")

    class Meta:
        model = DishIngridient
        fields = (
            "id", 
            "dish_title", 
            "ingredient", 
            "ingredient_title", 
            "weight"
        )


class DishSerializer(serializers.ModelSerializer):
    ingridients = DishIngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = (
            "id", 
            "title", 
            "description", 
            "ingridients"
        )

    def create(self, validated_data):
        ingridients = validated_data.pop("ingridients")
        instance = Dish.objects.create(**validated_data)
        ingredients_data = [
            DishIngridient(**data, dish=instance) 
            for data in ingridients
        ]
        DishIngridient.objects.bulk_create(ingredients_data)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        ingredients_data = validated_data.get("ingridients", [])  # [] in case if we don't wanna update ingredients
        current_ingredients_ids = [ # our ingredients that are in our instance right now before updating
            ingredient.id for ingredient 
            in instance.ingridients.all()
        ]

        for ingredient_data in ingredients_data:
            ingredient_id = ingredient_data.get("id", None) 
            if ingredient_id: # if ingredient exists we change it
                current_ingredients_ids.remove(ingredient_id)
                ingredient = DishIngridient.objects.get(id=ingredient_id, dish=instance)
                ingredient.ingredient = Ingredient.objects.get(
                    id=ingredient_data.get("ingredient")
                )
                ingredient.weight = ingredient_data.get("weight")
                ingredient.save()
            else: # if ingredient does not exist then we are creating it
                DishIngridient.objects.create(dish=instance, **ingredient_data)

        DishIngridient.objects.filter(
            id__in=current_ingredients_ids, 
            dish=instance
        ).delete() # in case if we want to delete some ingredients from our dish when updating 
                   # all ingredients will be deleted if we will send an empty array if ingredients

        return instance
