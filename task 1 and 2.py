def make_list_str(recepis):
    with open(recepis) as f:
        list_string = f.readlines()
        list_string_new = [string.strip() for string in list_string]
    return list_string_new


def make_list_dish():
    dish_list_all = []
    dish_list = []
    for string in make_list_str('recipes.txt'):
        if string != '':
            dish_list += [string]
        else:
            dish_list_all.append(dish_list)
            dish_list = []
    dish_list_all.append(dish_list)
    return dish_list_all


def make_cook_book():
    cook_book = {}
    for list_ in make_list_dish():
        cook_book[list_[0]] = make_dict_ingredient(list_)
    return cook_book


def make_dict_ingredient(list_):
    dishes_list = []
    for ingredient in list_[2:]:
        dish_ingredient = ingredient.split('|')
        ingredient, quantity, measure = dish_ingredient
        dish_dict = {'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure}
        dishes_list.append(dish_dict)
    return dishes_list


def get_shop_list_by_dishes(list_dishes, person):
    cook_book = make_cook_book()
    ingredients_dict = {}
    for dish in list_dishes:
        for ingredient in cook_book[dish]:
            list_ingredient = list(ingredient.values())
            if list_ingredient[0] not in ingredients_dict.keys():
                ingredient_dict = {'measure': list_ingredient[2], 'quantity': int(list_ingredient[1]) * person}
            else:
                ingredient_dict = ingredients_dict.get(list_ingredient[0])
                ingredient_dict['quantity'] = ingredient_dict['quantity'] + int(list_ingredient[1]) * person
            ingredients_dict[list_ingredient[0]] = ingredient_dict
    return ingredients_dict


print(make_cook_book())
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
