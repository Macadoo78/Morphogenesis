import pygame

class Player() : 
    def __init__(self,x,y) : 
        self.image = pygame.image.load('jeux_de_marlou\lejeu\monsieur.png')
        self.rect = self.image.get_rect(x=x,y=y)

    def move(self,x,y) :
        self.rect.move_ip(x,y)

    def draw(self,screen) :
        screen.blit(self.image,self.rect)