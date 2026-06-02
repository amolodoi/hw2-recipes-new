class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self.quantity = quantity
        self.unit = unit
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
