class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        
    
    def update(self):
        pass  # Implement entity-specific logic here
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class EntityManager:
    def __init__(self):
        self.entities = []
    
    def add_entity(self, entity):
        self.entities.append(entity)
    
    def update_entities(self):
        for entity in self.entities:
            entity.update()
    
    def render_entities(self, screen):
        for entity in self.entities:
            entity.render(screen)

    def remove_entity(self, entity):
        self.entities.remove(entity)
