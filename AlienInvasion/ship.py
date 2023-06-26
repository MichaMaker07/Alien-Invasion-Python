import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Lädt das Bild des Schiffes und ruft dessen umgebendes Rechteck ab.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Plaziertjedes neue Schiff mittig am unteren Bildschirmrand.
        self.rect.midbottom =self.screen_rect.midbottom
        
        # Speichert einen Fließkommawert für den Schiffsmittelpunkt
        self.x = float(self.rect.x)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
        
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Aktualisert das rect-Object auf der Grundlage von self.x.
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)