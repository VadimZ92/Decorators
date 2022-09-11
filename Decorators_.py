from pprint import pprint
import os
from Decorator_ import Decorator

file_name = "recipes.txt"


@Decorator
def сooking(file_name):
    with open(file_name, encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients = []
            ingredients_dict = {'ingredient_name': 1, 'quantity': 1, 'measure': 1}
            for item in range(int(file.readline())):
                ingredient = file.readline().strip().split('|')
                ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1],
                                    'measure': ingredient[2]}
                ingredients.append(ingredients_dict)
            cook_book[dish] = ingredients
            file.readline()
        return cook_book


сooking(file_name)


@Decorator
def repetition_сount(dishes):
    repetition_dict = {}
    count = 1
    for dish in dishes:
        if dish in repetition_dict.keys():
            repetition_dict[dish] += 1
        else:
            repetition_dict.setdefault(dish, 1)

    for num_repeat in list(repetition_dict.values()):
        count *= num_repeat
    return count


@Decorator
def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict1 = {}
    ingredients_dict2 = {}

    for dish, ingredients in сooking(file_name).items():
        if dish in dishes:
            for meaning in ingredients:
                ingredients_list = []
                for view, position in meaning.items():
                    ingredients_list.append([view, position])
                ingredients_list[1], ingredients_list[2] = ingredients_list[2], ingredients_list[1]
                ingredients_dict1 = {ingredients_list[0][1]: {ingredients_list[1][0]: ingredients_list[1][1],
                                                              ingredients_list[2][0]: int(ingredients_list[2][1])
                                                                                      * person_count * repetition_сount(
                                                                  dishes)}}
                ingredients_dict2.update(ingredients_dict1)

    return (ingredients_dict2)


get_shop_list_by_dishes(['Омлет'], 1)