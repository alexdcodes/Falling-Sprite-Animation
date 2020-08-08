import sys, pygame
from pygame.locals import *
from random import randrange

screen_size = 800, 600
weight_image = pygame.image.load('weight.png')

class Weight(pygame.sprite.Sprite)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """

        :return:
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        self.rect.top +=1

        if self.rect.top > screen_size[1]:
            self.reset()

    pygame.init()
    pygame.display.set_mode(screen_size, FULLSCREEN)
    pygame.mouse.set_mode(screen_size, FULLSCREEN)
    pygame.mouse_set_visable(0)
#    weight_image = pygame.image.load('weight.png')
    weight_image = weight_image.convert()

    sprite = pygame.sprite.RenderUpdates()

