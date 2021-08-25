import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Pet:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.ability = ""
        self.hunger = 0
        self.clock = pygame.time.Clock()
        self.running = False

    def update_hunger(self):
        self.hunger += 10

    def tick(self):
        self.update_hunger()

    def feed(self, level, amount):
        self.hunger -= (10 * level * amount)

    def start(self):
        self.running = True
        while self.running:
            self.tick()
            self.clock.tick(1/60)


    
