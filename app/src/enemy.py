import pygame
from entity import Entity
from config import score

class Enemy(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.health = 5  # You can adjust the initial health as needed
        self.speed = 1

    def update(self):
        # Implement enemy-specific logic here, such as movement or behavior
        self.x += self.speed
    
    def take_damage(self, entity_manager):
        self.health -= 1
        if self.health <= 0:
            entity_manager.remove_entity(self)
            # score += 1  # Increase score when enemy is defeated

    
    def render(self, screen):
        super().render(screen)
        font = pygame.font.Font(None, 24)
        health_text = font.render(f"Health: {self.health}", True, (255, 0, 0))
        screen.blit(health_text, (self.x, self.y - 20))
