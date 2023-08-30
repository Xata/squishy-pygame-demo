import pygame
import math
from entity import Entity
from projectile import Projectile
from config import screen_height, screen_width, score

class Player(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 2  # Adjust the movement speed as needed
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.x = max(0, self.x - self.speed)
        if keys[pygame.K_d]:
            self.x = min(screen_width - self.image.get_width(), self.x + self.speed)
        if keys[pygame.K_w]:
            self.y = max(0, self.y - self.speed)
        if keys[pygame.K_s]:
            self.y = min(screen_height - self.image.get_height(), self.y + self.speed)
    
    def render(self, screen):
        self.update()  # Update player position
        
        super().render(screen)  # Render the player image

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def shoot(self, entity_manager, projectile_image, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return
        
        direction = (dx / distance, dy / distance)
        
        start_x = self.x + 64  # Start from the center of the player sprite
        start_y = self.y + 64 # Start from the center of the player sprite
        
        projectile = Projectile(start_x, start_y, projectile_image, direction)
        entity_manager.add_entity(projectile)
