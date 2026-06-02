import pytest
from recipes import Ingredient, Recipe, ShoppingList


class TestIngredient:
    def test_creation(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert ing.name == "Мука"
        assert ing.quantity == 500.0
    
    def test_quantity_positive(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", -100, "г")
    
    def test_eq(self):
        ing1 = Ingredient("Мука", 500.0, "г")
        ing2 = Ingredient("Мука", 300.0, "г")
        assert ing1 == ing2


class TestRecipe:
    def test_add_ingredient(self):
        recipe = Recipe("Блины")
        flour = Ingredient("Мука", 500.0, "г")
        recipe.add_ingredient(flour)
        assert len(recipe) == 1
    
    def test_scale(self):
        recipe = Recipe("Блины", [Ingredient("Мука", 500.0, "г")])
        scaled = recipe.scale(2)
        assert scaled.ingredients[0].quantity == 1000.0


class TestShoppingList:
    def test_add_recipe(self):
        sl = ShoppingList()
        recipe = Recipe("Блины", [Ingredient("Мука", 500.0, "г")])
        sl.add_recipe(recipe, 2)
        assert len(sl.items) == 1
    
    def test_get_list(self):
        sl = ShoppingList()
        recipe = Recipe("Блины", [Ingredient("Мука", 500.0, "г")])
        sl.add_recipe(recipe, 2)
        result = sl.get_list()
        assert len(result) == 1
