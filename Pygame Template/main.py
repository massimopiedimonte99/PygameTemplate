import pygame as pg
from Game import Game
from settings import *

pg.init()

g = Game()

while g.running:
    g.new_game()
