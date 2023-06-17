from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("Tomate")
    ingredient_two = Ingredient("Tomate")
    assert ingredient_one.name == "Tomate"
    assert hash(ingredient_one) == hash("Tomate")
    assert str(ingredient_one) == "Ingredient('Tomate')"
    assert ingredient_one == ingredient_two
    assert ingredient_one.restrictions == set()
