from entity import Entity, EntityManager
from enemy import Enemy

class Projectile(Entity):
    def __init__(self, x, y, image, direction):
        super().__init__(x, y, image)
        self.speed = 8  # Adjust projectile speed as needed
        self.direction = direction  # Direction of the projectile (normalized vector)
    
    def update(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def update_projectile(self, entity_manager):
        self.check_collision_with_enemies(entity_manager)
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def check_collision_with_enemies(self, entity_manager):
            for enemy in entity_manager.entities:
                if isinstance(enemy, Enemy):
                    if (
                        self.x < enemy.x + enemy.image.get_width() and
                        self.x + self.image.get_width() > enemy.x and
                        self.y < enemy.y + enemy.image.get_height() and
                        self.y + self.image.get_height() > enemy.y
                    ):
                        enemy.take_damage(entity_manager)
                        entity_manager.remove_entity(self)
