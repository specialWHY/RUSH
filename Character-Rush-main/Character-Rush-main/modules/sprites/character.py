import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, imagepaths, position=(40, 535), size=[(100, 141), (177, 80)], **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        # 加载第一张图片
        image = pygame.image.load(imagepaths[0])
        self.images.append(pygame.transform.scale(image, size[0]))
        # 加载第二张图片
        image = pygame.image.load(imagepaths[1])
        self.images.append(pygame.transform.scale(image, size[1]))
        self.image_idx = 0
        self.jump_image_idx = 0  # 跳跃状态图片索引
        self.duck_image_idx = 1  # 俯身状态图片索引
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)

        self.init_position = position
        self.refresh_rate = 5
        self.refresh_counter = 0
        self.speed = 20
        self.gravity = 0.7
        self.is_jumping = False
        self.is_ducking = False
        self.is_dead = False
        self.movement = [0, 0]

    def jump(self, sounds):
        if self.is_dead or self.is_jumping:
            return
        sounds['jump'].play()
        self.is_jumping = True
        self.movement[1] = -1 * self.speed

    def duck(self):
        if self.is_jumping or self.is_dead:
            return
        self.is_ducking = True
        self.rect.bottom += 60  # 俯身时将图片起点往下移60

    def unduck(self):
        self.is_ducking = False
        self.rect.bottom -= 60  # 取消俯身时将图片起点恢复

    def die(self, sounds):
        if self.is_dead:
            return
        sounds['die'].play()
        self.is_dead = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.is_dead:
            self.image_idx = 1  # 死亡状态展示第二张图片
            self.loadImage()
            return
        if self.is_jumping:
            self.movement[1] += self.gravity
            self.image_idx = self.jump_image_idx  # 跳跃状态展示跳跃图片
            self.loadImage()
            self.rect = self.rect.move(self.movement)
            if self.rect.bottom >= self.init_position[1]:
                self.rect.bottom = self.init_position[1]
                self.is_jumping = False
        elif self.is_ducking:
            self.image_idx = self.duck_image_idx  # 俯身状态展示俯身图片
            self.loadImage()
        else:
            self.image_idx = 0  # 其他状态展示第一张图片
            self.loadImage()
        self.refresh_counter += 1
