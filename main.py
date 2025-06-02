import pygame
import random

# Initialize pygame.
pygame.init()

# Screen dimensions.
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game with Keyboard Controlled Paddles")

# Colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

# Fonts.
score_font = pygame.font.SysFont("Comic Sans", 24)
instruction_font = pygame.font.SysFont("Comic Sans", 18)

'''
main.py
-------
This is a simple Pong game using Pygame. It demonstrates basic Object-Oriented Programming (OOP) concepts and how to use Pygame's Sprite system.

- Each game object (paddle, ball) is a class that inherits from pygame.sprite.Sprite.
- Sprite groups are used to manage and draw all game objects easily.
- The game loop handles input, updates game state, and draws everything to the screen.
'''

# Paddle class inheriting from pygame.sprite.Sprite
class Paddle(pygame.sprite.Sprite):
    '''
    Paddle represents a player's paddle. It can move up and down, and is kept within the screen bounds.
    Inherits from pygame.sprite.Sprite so it can be used in sprite groups.
    '''
    def __init__(self, x, y, width, height, speed):
        super().__init__()  # Initialize the Sprite parent class
        
        # Create the paddle's image (a simple rectangle)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)  # Fill the paddle with white color
        
        # Get the rectangle (position and size) for the paddle
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.speed = speed  # How fast the paddle moves

    def move(self, dy):
        '''Move the paddle by dy pixels (up or down).'''
        self.rect.y += dy
        
        # Keep the paddle within the screen bounds.
        if self.rect.top < 0:
            self.rect.top = 0  # Don't let the paddle go above the screen
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height  # Don't let the paddle go below the screen

# Ball class inheriting from pygame.sprite.Sprite
class Ball(pygame.sprite.Sprite):
    '''
    Ball represents the moving ball in the game.
    Inherits from pygame.sprite.Sprite for easy collision and drawing.
    '''
    def __init__(self, x, y, size, speed_x, speed_y):
        super().__init__()  # Initialize the Sprite parent class
        
        # Create the ball's image (a red circle)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, [0, 0, size, size])
        
        # Get the rectangle for the ball and set its center
        self.rect = self.image.get_rect(center=(x, y))
        
        self.vx = speed_x  # Horizontal speed
        self.vy = speed_y  # Vertical speed

    def update(self):
        '''Move the ball and bounce off the top/bottom edges.'''
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Bounce off the top and bottom edges.
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.vy *= -1  # Reverse vertical direction

    def reset(self):
        '''Reset the ball to the center and give it a new random direction.'''
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.vx = random.choice([-4, 4])
        self.vy = random.choice([-4, 4])

# Initialize paddles and ball.
# These are the main objects in the game.
left_paddle = Paddle(10, (screen_height - 100) // 2, 10, 100, 5)  # Left player's paddle
right_paddle = Paddle(screen_width - 20, (screen_height - 100) // 2, 10, 100, 5)  # Right player's paddle
ball = Ball(screen_width // 2, screen_height // 2, 10, 4, 4)  # The ball

# Create a sprite group to manage all sprites together.
# This lets us update and draw everything with just one line.
all_sprites = pygame.sprite.Group()
all_sprites.add(left_paddle, right_paddle, ball)

# Initialize scores for both players.
left_score = 0
right_score = 0

# Instruction text to show controls to the players.
instructions = "Left: Q (up), Z (down)   Right: P (up), . (down)"

clock = pygame.time.Clock()

running = True
while running:  # One iteration represents one frame.
    clock.tick(60)  # 60 frames per second.
    
    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input.
    keys = pygame.key.get_pressed()
    
    # Left paddle: Q for up, Z for down.
    if keys[pygame.K_q]:
        left_paddle.move(-left_paddle.speed)
    if keys[pygame.K_z]:
        left_paddle.move(left_paddle.speed)
    
    # Right paddle: P for up, . (period) for down.
    if keys[pygame.K_p]:
        right_paddle.move(-right_paddle.speed)
    if keys[pygame.K_PERIOD]:
        right_paddle.move(right_paddle.speed)

    # Update ball movement.
    ball.update()

    # Check for collision with paddles.
    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
        ball.vx *= -1

    # Check for scoring.
    if ball.rect.left <= 0:
        right_score += 1
        ball.reset()
    if ball.rect.right >= screen_width:
        left_score += 1
        ball.reset()

    # Drawing section.
    screen.fill(BLACK)
    
    # Draw all sprites.
    all_sprites.draw(screen)
    
    # Display scores.
    score_text = score_font.render(f"Left: {left_score}    Right: {right_score}", True, WHITE)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))
    
    # Display instructions in grey.
    instruction_text = instruction_font.render(instructions, True, GREY)
    screen.blit(instruction_text, (screen_width // 2 - instruction_text.get_width() // 2, screen_height - 40))
    
    pygame.display.flip()

pygame.quit()