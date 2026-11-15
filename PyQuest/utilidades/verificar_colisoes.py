import pygame

def verificar_colisao(window, ator1, ator2=False):
    # colisão da porta
    if (ator1.colliderect(pygame.Rect(0, 0, 200, 10)) or ator1.colliderect(pygame.Rect(window.get_width() - 200, 0, 200, 10))):
        ator1.move_ip(0, 50)
