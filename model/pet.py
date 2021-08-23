import pygame
class Pet:
    def __init__(self, name, health, ability):
        self.name = name
        self.health = health
        self.ability = ability
        self.hunger = 0
        self.clock = pygame.time.Clock()
        self.running = False

    def tick(self):
        print("reeeeee")
        pass

    def feed(self,amount):
        self.hunger -= amount

    def start(self):
        self.running = True
        while self.running:
            self.tick()
            self.clock.tick(1/60)

    
