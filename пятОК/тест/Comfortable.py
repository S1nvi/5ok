import pygame
import sys
import math
import threading

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вращающаяся Сфера")

# Параметры сферы
angle_x, angle_y = 0, 0  # Углы вращения
rotation_speed = 1  # Начальная скорость вращения
size = 150  # Радиус сферы
num_points = 1000  # Количество точек на сфере

# Параметры камеры
camera_x, camera_y, camera_z = 0, 0, 0  # Положение камеры

# Генерация точек на сфере
def generate_sphere_points(radius, num_points):
    points = []
    for i in range(num_points):
        theta = math.acos(1 - 2 * (i + 0.5) / num_points)  # Угол по вертикали
        phi = math.pi * (1 + 5**0.5) * i  # Угол по горизонтали
        x = radius * math.sin(theta) * math.cos(phi)
        y = radius * math.sin(theta) * math.sin(phi)
        z = radius * math.cos(theta)
        points.append((x, y, z))
    return points

# Получаем точки для сферы
sphere_points = generate_sphere_points(size, num_points)

# Функция для управления через командную строку
def command_listener():
    global rotation_speed
    while True:
        command = input("Введите команду: ")
        if command == "run +":
            rotation_speed += 1
            print(f"Скорость вращения увеличена: {rotation_speed}")
        elif command == "run -":
            rotation_speed = max(1, rotation_speed - 1)  # Минимальная скорость 1
            print(f"Скорость вращения уменьшена: {rotation_speed}")

# Запуск потока для управления командной строкой
threading.Thread(target=command_listener, daemon=True).start()

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_z += 5  # Движение вперед
    if keys[pygame.K_s]:
        camera_z -= 5  # Движение назад
    if keys[pygame.K_a]:
        camera_x -= 5  # Движение влево
    if keys[pygame.K_d]:
        camera_x += 5  # Движение вправо
    if keys[pygame.K_q]:
        camera_y -= 5  # Движение вверх
    if keys[pygame.K_e]:
        camera_y += 5  # Движение вниз

    # Очистка экрана
    screen.fill((0, 0, 0))  # Черный фон

    # Обновление углов вращения
    angle_x += rotation_speed * 0.01
    angle_y += rotation_speed * 0.01

    # Рисуем сферу
    for x, y, z in sphere_points:
        # Поворот точек
        x_rotated = x * math.cos(angle_y) - z * math.sin(angle_y)
        z_rotated = x * math.sin(angle_y) + z * math.cos(angle_y)
        y_rotated = y * math.cos(angle_x) - z_rotated * math.sin(angle_x)
        z_rotated = y * math.sin(angle_x) + z_rotated * math.cos(angle_x)

        # Проекция 3D-координат на 2D-экран
        perspective = 400 / (400 + z_rotated + camera_z)  # Простая перспектива
        x_screen = int(WIDTH / 2 + (x_rotated + camera_x) * perspective)
        y_screen = int(HEIGHT / 2 - (y_rotated + camera_y) * perspective)

        # Проверка, что точка находится в пределах экрана
        if 0 <= x_screen < WIDTH and 0 <= y_screen < HEIGHT:
            # Рисуем точку на экране
            pygame.draw.circle(screen, (255))
