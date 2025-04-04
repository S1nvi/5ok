import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Киберсражение")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Вопросы викторины
questions = [
    ("Что такое фишинг?", "Атака на пользователя с целью кражи данных"),
    ("Что такое вирус?", "Программа, которая может повредить компьютер"),
    ("Для чего нужна антивирусная программа?", "Защита от вредоносных программ"),
]

# Игрок
player_pos = [WIDTH // 2, HEIGHT - 50]
player_speed = 5

# Основной игровой цикл
def game_loop():
    score = 0
    question_index = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
            player_pos[0] += player_speed

        screen.fill(WHITE)

        # Рисуем игрока
        pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], 50, 50))

        # Викторина
        if question_index < len(questions):
            question, answer = questions[question_index]
            question_text = font.render(question, True, BLACK)
            screen.blit(question_text, (50, 50))
            answer_text = font.render("Нажмите 'Y' для верного ответа", True, BLACK)
            screen.blit(answer_text, (50, 100))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                score += 1
                question_index += 1
            elif keys[pygame.K_n]:
                question_index += 1

        else:
            game_over = True

        if game_over:
            game_over_text = font.render(f"Игра окончена! Ваш счет: {score}", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        
        pygame.display.flip()
        pygame.time.delay(30)

# Запуск игры
game_loop()
