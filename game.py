import pygame
from player import Player
from bloc import Bloc

class Game():
    def __init__(self, screen, longueur, largeur):    
        # on initie toutes les variables   
        self.screen = screen
        self.running = True
        self.move = [0,0]
        self.player = Player(longueur/2, largeur/2)
        self.bloc = Bloc(longueur/2, (largeur/2)+30, '\grass')
        self.clock = pygame.time.Clock()
        self.saut = False
        
    def handling_events(self):    
        # on regarde si ca quitte
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        self.keys = pygame.key.get_pressed()

        # deplacement horrizontal
        if self.keys[pygame.K_RIGHT] :
            self.move[0] = 5
        elif self.keys[pygame.K_LEFT] :
            self.move[0] = -5
        else :
            self.move[0] = 0

        # déplacement vertical également appelé "saut" par les professionnels 
        if self.keys[pygame.K_UP] :
            self.saut = True
        
        if self.saut:
                self.bloc.jump()
                self.move[1] = self.bloc.hauteur
                if self.bloc.hauteur == -11 :
                    self.saut = False
                    self.bloc.hauteur = 11
                    self.move[1] = 0



    def update(self):
        self.bloc.move(-self.move[0],self.move[1])

    def display(self):
        # on update l'ecran a chaque frame
        self.screen.fill('black')
        self.player.draw(self.screen)
        self.bloc.draw(self.screen)
        pygame.display.flip()


    def run(self):
        while self.running : 
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

            
