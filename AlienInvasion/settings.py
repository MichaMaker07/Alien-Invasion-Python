class Settings():
    """ A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Schiffseinstellungen
        self.ship_speed = 1.5
        
        # Invasionsschiffseinstellung
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Der Wert 1 für fleet_direction bedeutet "nach rechts", -1 "nach links".
        self.fleet_direction = 1
        
        # Geschosseinstellungen
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        