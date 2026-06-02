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
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        result = f"Рецепт: {self.title}"
        for ing in self.ingredients:
            result += f"\n  - {ing}"
        return result
