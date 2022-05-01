import pygame

class Bloc() : 
    def __init__(self, x, y, typdebloc) : 
        self.texte = 'jeux_de_marlou\lejeu'
        self.texte += typdebloc
        self.texte += '.png'
        self.image = pygame.image.load(self.texte)
        self.rect = self.image.get_rect(x=x,y=y)
        self.hauteur = 11

    def move(self,x,y) :
        self.rect.move_ip(x,y)

    def jump(self) :
        self.hauteur -= 1

    def draw(self,screen) :
        screen.blit(self.image,self.rect)