import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pytest.raises(TypeError) as type_error:
        Dish("Teste", "5")
    with pytest.raises(ValueError) as value_error:
        Dish("Teste", -1)
    ingredient_one = Ingredient("farinha")
    dish_one = Dish("macarronada", 7.90)
    dish_two = Dish("macarronada", 7.90)
    dish_one.add_ingredient_dependency(ingredient_one, 1)
    assert dish_one.get_restrictions() == {Restriction.GLUTEN}
    assert dish_one.get_ingredients() == {ingredient_one}
    assert dish_one == dish_two
    assert dish_one.name == "macarronada"
    assert hash(dish_one) == hash("Dish('macarronada', R$7.90)")
    assert str(type_error.value) == "Dish price must be float."
    assert str(value_error.value) == "Dish price must be greater then zero."
