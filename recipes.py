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
