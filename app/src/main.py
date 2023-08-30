import pygame
import sys
from entity import EntityManager
from player import Player
from enemy import Enemy
from projectile import Projectile
from config import screen_height, screen_width

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Squishy Pygame Demo")

# Set up game clock
clock = pygame.time.Clock()

# Initialize entities
entity_manager = EntityManager()

player_image = pygame.image.load("app\\assets\\player_image.png")
player = Player(screen_width / 2, screen_height / 2, player_image)
entity_manager.add_entity(player)

projectile_image = pygame.image.load("app\\assets\\projectile_image.png") 

enemy_image = pygame.image.load("app\\assets\\enemy_image.png")
enemy1 = Enemy(100, 100, enemy_image)
enemy2 = Enemy(500, 300, enemy_image)
entity_manager.add_entity(enemy1)
entity_manager.add_entity(enemy2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                player.shoot(entity_manager, projectile_image, *event.pos)

    # Clear the screen
    screen.fill((0, 64, 0))
    
    # Update game logic here
    for entity in entity_manager.entities:
        if isinstance(entity, Projectile):  # Check if entity is a Projectile
            entity.update_projectile(entity_manager)
        else:
            entity.update()

    # Draw game elements here
    entity_manager.render_entities(screen)

    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
