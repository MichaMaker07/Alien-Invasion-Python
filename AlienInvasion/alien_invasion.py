import sys

import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall aclass to manage game assets and behavior."""
    def __init__(self):
        # Initialisiert das Spiel und erstellt ein screen-Objekt.
        pygame.init()
        self.settings = Settings()


        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """ Start the main loop for the game."""
        # Legt die Hintergrundfarbe fest.
        # bg_color = (230,230,230)
        # Startet die Hauptschleife des Spiels.
        while True:
            #Lauscht auf Tastatur- und Mausereignisse.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Entfernt die verschwundenen Geschosse.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
                
    def _fire_bullet(self):
        """Create a new bullet adn add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

                
    
    
    def _check_keydown_events(self,event):
        """Respont to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            print("RIGHT")
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            print("LEFT")

        elif event.key == pygame.K_q:
            print("q")
            sys.exit()
        elif event.key == pygame.K_SPACE:
            print("Space")
            self._fire_bullet()
            
    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Macht den als Letztes gezeichneten Bildschirm sichtbar        
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Erstellt eine Spielinstanz und fuerht das Spiel aus
    ai = AlienInvasion()
    ai.run_game()