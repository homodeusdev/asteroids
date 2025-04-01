import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rorate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
        if self.rotation >= 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rorate(-dt)
        if keys[pygame.K_d]:
            self.rorate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        self.rotation %= 360

    def shoot(self):
        # Placeholder for shooting functionality
        print("Pew! Pew!")

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
