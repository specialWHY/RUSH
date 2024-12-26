import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, imagepaths, position=(1200, 545), sizes=[(120, 204), (80, 114)], **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for imagepath, size in zip(imagepaths, sizes):
            image = pygame.image.load(imagepath)
            self.images.append(pygame.transform.scale(image, size))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


class Ptera(pygame.sprite.Sprite):
    def __init__(self, imagepath, position, size=(138, 90), **kwargs):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
