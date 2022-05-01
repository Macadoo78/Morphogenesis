import pygame
import ctypes
from game import Game

pygame.init()
usr32 = ctypes.windll.user32
longueur = usr32.GetSystemMetrics(0)
largeur = usr32.GetSystemMetrics(1)
screen = pygame.display.set_mode((longueur, largeur-50))
pygame.display.set_caption('Morphogenesis - aventure')
icon = pygame.image.load('jeux_de_marlou\lejeu\grass.png')
pygame.display.set_icon(icon)

game = Game(screen, longueur, largeur)
game.run()
pygame.quit()