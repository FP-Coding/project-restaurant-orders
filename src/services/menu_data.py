from csv import DictReader
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as file:
            data = list(DictReader(file, delimiter=",", quotechar='"'))
        dishes = {}
        for item_menu in data:
            name = item_menu["dish"]
            price = float(item_menu["price"])
            amount = int(item_menu["recipe_amount"])
            ingredient = item_menu["ingredient"]
            if name not in dishes:
                dishes[name] = Dish(name, price)
                dishes[name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
            else:
                dishes[name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
        self.dishes = set(dishes.values())
