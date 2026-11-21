import pygame, threading

def musica_menu():
    pygame.mixer.music.load("utilidades/assets/sounds/SwitchWithMeTheme.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def musica_ambiente():
    pygame.mixer.music.load("utilidades/assets/sounds/PitcherPerfectTheme.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def musica_boss():
    pass

def som_ataque():
    som = pygame.mixer.Sound("utilidades/assets/sounds/ataque.ogg")
    som.set_volume(0.2)
    
    threading.Timer(0.3, som.play).start()

def som_interacao():
    som = pygame.mixer.Sound("utilidades/assets/sounds/interagir.ogg")
    som.set_volume(0.2)
    
    threading.Timer(0.3, som.play).start()

def som_movimento():
    som = pygame.mixer.Sound("utilidades/assets/sounds/mover.ogg")
    som.set_volume(0.1)

    threading.Timer(0.3, som.play).start()

def som_aprimoramento():
    som = pygame.mixer.Sound("utilidades/assets/sounds/aprimoramento.ogg")
    som.set_volume(0.2)
        
    threading.Timer(0.2, som.play).start()

