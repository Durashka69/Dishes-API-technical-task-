from rest_framework import serializers

from apps.menu.models import (
    Menu, 
    DishMenu
)

from apps.dishes.models import Dish

class DishMenuSerializer(serializers.ModelSerializer):
    dish_title = serializers.ReadOnlyField(source='dish.title')

    class Meta:
        model = DishMenu
        fields = (
            'id',
            'dish',
            'dish_title',
            "eating_time",
        )


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishMenuSerializer(many=True)
    user_email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Menu
        fields = (
            "id",
            "user",
            'user_email',
            "day_of_week",
            "dishes",
        )
        read_only_fields = ('user',)

    def create(self, validated_data):
        dishes = validated_data.pop("dishes")
        instance = Menu.objects.create(**validated_data)
        dishes_data = [
            DishMenu(**data, menu=instance)
            for data in dishes
        ]
        DishMenu.objects.bulk_create(dishes_data)
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.day_of_week = validated_data.get("day_of_week", instance.day_of_week)
        instance.save()

        dishes_data = validated_data.get("dishes", [])
        current_dishes_ids = [
            dish.id for dish
            in instance.dishes.all()
        ]

        for dish_data in dishes_data:
            dish_id = dish_data.get("id", None)
            if dish_id:
                current_dishes_ids.remove(dish_id)
                dish = DishMenu.objects.get(id=dish_id, menu=instance)
                dish.dish = Dish.objects.get(
                    id=dish_data.get("dish")
                )
                dish.eating_time = dish_data.get("eating_time")
                dish.save()
            else:
                DishMenu.objects.create(menu=instance, **dish_data) # I thought i could write it with 
                                                                    # bulk_update method, but I think this
                                                                    # is ok

        DishMenu.objects.filter(
            id__in=current_dishes_ids,
            menu=instance
        ).delete()

        return instance
