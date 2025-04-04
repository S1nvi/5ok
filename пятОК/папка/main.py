import pygame
import sys
from screen import Screen  # Импортируем класс Screen из screen.py

# Цвета для квадратов
colors = [
    (255, 0, 0),    # Красный
    (0, 255, 0),    # Зеленый
    (0, 0, 255),    # Синий
    (255, 255, 0),  # Желтый
    (255, 165, 0)   # Оранжевый
]

def main():
    screen = Screen()
    square_size = 50  # Размер квадратов
    spacing = 10      # Расстояние между квадратами

    # Позиции для квадратов
    square_positions = [
        (screen.WIDTH // 2 - 2 * (square_size + spacing), screen.HEIGHT // 2),  # Левый квадрат
        (screen.WIDTH // 2 - (square_size + spacing), screen.HEIGHT // 2),        # Второй квадрат
        (screen.WIDTH // 2, screen.HEIGHT // 2),                                   # Центральный квадрат
        (screen.WIDTH // 2 + (square_size + spacing), screen.HEIGHT // 2),        # Четвертый квадрат
        (screen.WIDTH // 2 + 2 * (square_size + spacing), screen.HEIGHT // 2)     # Правый квадрат
    ]

    options = [
        ("Начать играть", (screen.WIDTH // 2, screen.HEIGHT // 3)),
        ("Уровни", (screen.WIDTH // 2, screen.HEIGHT // 2)),
        ("Разработчики", (screen.WIDTH // 2, screen.HEIGHT * 2 // 3)),
        ("Выход", (screen.WIDTH // 2, screen.HEIGHT * 5 // 6)),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill_color((0, 0, 0))  # Черный фон

        # Рисуем разноцветные квадраты
        for i in range(len(colors)):
            screen.draw_square(square_positions[i], square_size, colors[i])

        # Рисуем текстовые заметки
        for text, position in options:
            screen.draw_text(text, position, (255, 255, 255))  # Белый цвет текста

        screen.update()

if __name__ == "__main__":
    main()
