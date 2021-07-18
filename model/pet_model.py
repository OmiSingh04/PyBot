class Pet:
    def __init__(self, health, hunger, happiness, hun_rate):
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.hun_rate = hun_rate

    def damage(self, rate):
        pass
    
    def lvl_up(self):
        pass

class Cat(Pet):
    def __init__(self, health, hunger, happiness, hun_rate, breed):
        super().__init__( health, hunger, happiness, hun_rate)
        self.breed = breed
        pass

    def meow(self):
        return "Meow Meow!"

class Dog(Pet):
    def __init__(self, health, hunger, happiness, hun_rate, breed):
        super().__init__(health, hunger, happiness, hun_rate)
        self.breed = breed
        pass
    
    def woof(self):
        return "Woof Woof!!"