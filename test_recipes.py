import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe


class TestIngredient:
    def test_creation(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert ing.name == "Мука"
        assert ing.quantity == 500.0
        assert ing.unit == "г"
    
    def test_quantity_positive(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", -100, "г")
    
    def test_str(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert str(ing) == "Мука: 500.0 г"
    
    def test_eq(self):
        ing1 = Ingredient("Мука", 500.0, "г")
        ing2 = Ingredient("Мука", 300.0, "г")
        ing3 = Ingredient("Сахар", 100.0, "г")
        assert ing1 == ing2
        assert ing1 != ing3
