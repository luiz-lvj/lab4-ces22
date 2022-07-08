class FoodComponent:
    def getDescription(self):
        return self.__class__.__name__
    
    def getTotalCost(self):
        return self.__class__.cost

class Plate(FoodComponent):
    cost = 0.0

class Decorator(FoodComponent):
    def __init__(self, foodComponent):
        self.component = foodComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + FoodComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + " " + FoodComponent.getDescription(self)


class Oregano(Decorator):
    cost = 1.20
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Muzzarela(Decorator):
    cost = 1.00
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Lombo(Decorator):
    cost = 2.00
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Queijo(Decorator):
    cost = 0.75
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class MolhoTomate(Decorator):
    cost = 0.50
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Calabresa(Decorator):
    cost = 1.15
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

# -------- TESTES ---------

pizza1 = Calabresa(Queijo(Muzzarela(Plate())))
pizza2 = Oregano(Lombo(MolhoTomate(Plate())))

print(pizza1.getDescription() + ": $" + str(pizza1.getTotalCost()))
print(pizza2.getDescription() + ": $" + str(pizza2.getTotalCost()))


