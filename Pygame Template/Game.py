import pygame as pg
from settings import *

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((W, H))
        self.screen.fill(BLACK)
        pg.display.set_caption(TITLE)
        
        self.running = True
      
    def new_game(self):
        self.playing = True
        self.sprites = pg.sprite.Group()
        
        self.run()

    def events(self):
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def draw(self):
        self.sprites.draw(self.screen)
        
        pg.display.flip()
    
    def update(self):
        self.sprites.update()
    
    def run(self):
        while self.playing:
            pg.time.Clock().tick(FPS)  
            
            self.events()
            self.update()
            self.draw()