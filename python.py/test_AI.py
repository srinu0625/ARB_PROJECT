import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car properties
car_img = pygame.image.load("images/car.png")
car_width, car_height = car_img.get_size()
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Obstacle properties
obstacle_img = pygame.Surface((100, 20))
obstacle_img.fill((255, 0, 0))
obstacle_speed = 5
obstacle_gap = 200
obstacle_freq = 25

clock = pygame.time.Clock()

def draw_car(x, y):
    screen.blit(car_img, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_img, (x, y))

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over!", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    score = 0
    obstacle_x = random.randint(0, WIDTH - 100)
    obstacle_y = -20

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed

        if car_x < 0:
            car_x = 0
        elif car_x > WIDTH - car_width:
            car_x = WIDTH - car_width

        obstacle_y += obstacle_speed

        if obstacle_y > HEIGHT:
            obstacle_y = -20
            obstacle_x = random.randint(0, WIDTH - 100)
            score += 1

        if car_y < obstacle_y + obstacle_img.get_height() and car_x < obstacle_x + obstacle_img.get_width() and car_x + car_width > obstacle_x:
            game_over()

        draw_car(car_x, car_y)
        draw_obstacle(obstacle_x, obstacle_y)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
