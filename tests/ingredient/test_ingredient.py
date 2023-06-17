from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("farinha")
    ingredient_two = Ingredient("farinha")
    assert ingredient_one.name == "farinha"
    assert hash(ingredient_one) == hash("farinha")
    assert str(ingredient_one) == "Ingredient('farinha')"
    assert ingredient_one == ingredient_two
    assert ingredient_one.restrictions == {Restriction.GLUTEN}
