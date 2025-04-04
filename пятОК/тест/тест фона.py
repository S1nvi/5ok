import pygame

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Загрузка изображений
background1 = pygame.image.load("computer.jpg").convert()
background2 = pygame.image.load("computer2.png").convert()
current_background = background1

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Смена фона при клике мышью
            if current_background == background1:
                current_background = background2
            else:
                current_background = background1

    # Отображение текущего фона
    screen.blit(current_background, (0, 0))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
