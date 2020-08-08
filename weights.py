import sys, pygame
from pygame.locals import *
from random import randrange

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
        