import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ball Game')

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Параметры шара
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Параметры объекта (что нужно собирать)
object_radius = 15
object_x = random.randint(50, width - 50)
object_y = random.randint(50, height - 50)

# Игровые параметры
score = 0
font = pygame.font.SysFont('Arial', 30)

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление шариком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed_x
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed_x
    if keys[pygame.K_UP]:
        ball_y -= ball_speed_y
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed_y

    # Отскок от стен
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Проверка столкновения с объектом
    distance = ((ball_x - object_x) ** 2 + (ball_y - object_y) ** 2) ** 0.5
    if distance < ball_radius + object_radius:
        score += 1
        object_x = random.randint(50, width - 50)
        object_y = random.randint(50, height - 50)

    # Отображение шарика и объекта
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    pygame.draw.circle(screen, GREEN, (object_x, object_y), object_radius)

    # Отображение счета
    score_text = font.render(f'Score: {score}', True, RED)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Завершение игры
pygame.quit()
