from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius, *args, **kwargs):
        super().__init__(x, y, radius, *args, **kwargs) # Initiate Sprite and CircleShape in MRO
        if hasattr(Player, 'containers'):
            for group in Player.containers:
                group.add(self)
        # CircleShape's positioning
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        
        # Pygame's sprite setup
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA) # Transparent surface
        pygame.draw.circle(self.image, (255, 0, 0), (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS) # Draw CircleShape's appearance
        
        self.rect = self.image.get_rect() # Use pygame.rect for positioning
        self.rect.center = self.position
        
        self.rotation = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        
    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            
        # Render the triangle to self.image for compatibility with Group.draw()
        self.image.fill((0, 0, 0, 0))  # Clear the surface (transparent)
        pygame.draw.polygon(self.image, "white", [
            (self.radius, 0),  # Adjust to fit on self.image
            (0, self.radius * 2),
            (self.radius * 2, self.radius * 2),
        ], width=2)
        
        # Clear the surface (transparent)
        self.image.fill((0, 0, 0, 0))  

        # Calculate triangle points relative to the surface
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5

        # The three points of the triangle, centered on `self.image`
        point_a = (self.radius + forward.x, self.radius - forward.y)  # Tip of triangle
        point_b = (self.radius - forward.x - right.x, self.radius + forward.y + right.y)
        point_c = (self.radius - forward.x + right.x, self.radius + forward.y - right.y)
        points = [point_a, point_b, point_c]

        # Draw the triangle onto the transparent surface
        pygame.draw.polygon(self.image, "white", points, width=2)
        self.rect.center = self.position
                
        def move(self, dt):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt
        
        # Update self.rect to match self.position
        self.rect.center = self.position