import sys

import pygame

from settings import Settings

def run_game():
    # Initialisiert das Spiel und erstellt ein screen-Objekt.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    # Legt die Hintergrundfarbe fest.
    # bg_color = (230,230,230)
    #sStartet die Hauptschleife des Spiels.
    while True:
        
        #Lauscht auf Tastatur- und Mausereignisse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        # Macht den als Letztes gezeichneten Bildschirm sichtbar        
        pygame.display.flip()
        

run_game()
