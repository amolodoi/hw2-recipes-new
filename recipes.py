class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self.quantity = quantity
        self.unit = unit
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients.copy()
    
    def add_ingredient(self, ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return ratio > 0
    
    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")
        new_ingredients = []
        for ing in self.ingredients:
            new_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            new_ingredients.append(new_ing)
        return Recipe(self.title, new_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        result = f"Рецепт: {self.title}"
        for ing in self.ingredients:
            result += f"\n  - {ing}"
        return result


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def __str__(self):
        return f"[{self.diet_type}] {self.title}"


class ShoppingList:
    def __init__(self):
        self.items = []
    
    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ing in scaled.ingredients:
            self.items.append((ing, recipe.title))
    
    def get_list(self):
        result = []
        for ing, title in self.items:
            result.append(ing)
        return result
