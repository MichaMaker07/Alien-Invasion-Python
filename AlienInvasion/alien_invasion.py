import sys

import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
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
            self._update_aliens()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Erstellt ein Invasionsschiff und ermittelt die Anzahl der
        # Invasionsschiffe pro Zeile.
        # Der Abstand beträgt jweils eine Schiffsbreite
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Bestimmt die Anzahl der Reihen von Invasionsschiffen, die auf den Bildschirm passen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Erstellt die Invasionsschiffen.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        
        
            
            

    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Entfernt die verschwundenen Geschosse.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
            
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(sefl):
        """Respond to bullet-alien collisions."""
        # Entfernt alle kollidierten Geschosse und Invasionsschiffe.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Zerstört vorhandene Geschosse und erstellt eine neue Flott.
            self.bullets.empty()
            self._create_fleet()
        
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

                
    def _update_aliens(self):
        """Update the positions fo all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
    
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
            
        self.aliens.draw(self.screen)    
        # Macht den als Letztes gezeichneten Bildschirm sichtbar        
        pygame.display.flip()
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
if __name__ == '__main__':
    # Erstellt eine Spielinstanz und fuerht das Spiel aus
    ai = AlienInvasion()
    ai.run_game()