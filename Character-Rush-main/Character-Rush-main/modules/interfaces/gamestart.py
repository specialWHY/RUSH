import sys
import pygame
from ..sprites import Character


def GameStartInterface(screen, sounds, cfg):
    font01 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 48)
    gamestart_text01 = font01.render(" WIN?", True, (83, 83, 83))
    gamestart_text01_rect = gamestart_text01.get_rect()
    gamestart_text01_rect.centerx = cfg.SCREENSIZE[0] / 2
    gamestart_text01_rect.centery = cfg.SCREENSIZE[1] * 0.35
    font02 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 18)
    gamestart_text02 = font02.render("OR LOST!", True, (83, 83, 83))
    gamestart_text02_rect = gamestart_text02.get_rect()
    gamestart_text02_rect.centerx = cfg.SCREENSIZE[0] / 2
    gamestart_text02_rect.centery = cfg.SCREENSIZE[1] * 0.45
    ch = Character(cfg.IMAGE_PATHS['ch'])
    ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (1200, 48))
    rect = ground.get_rect()
    rect.left = 0
    rect.bottom = cfg.SCREENSIZE[1] * 0.93
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    ch.jump(sounds)
        ch.update()
        screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(ground, rect)
        screen.blit(gamestart_text01, gamestart_text01_rect)
        screen.blit(gamestart_text02, gamestart_text02_rect)
        ch.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not ch.is_jumping) and press_flag:
            return True
