import http.server
import socketserver
import os

# Укажите путь к директории, где находится ваш HTML-файл
DIRECTORY = "C:/Users/Ученик 21/Desktop/пятОК/тест сайт и сервер/сайт"  # Замените на актуальный путь

# Укажите порт, на котором будет работать сервер
PORT = 8000

# Изменяем текущую директорию
os.chdir(DIRECTORY)

# Определяем обработчик запросов
Handler = http.server.SimpleHTTPRequestHandler

# Создаем сервер
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}. Откройте http://192.168.111.160:{PORT} в браузере.")
    httpd.serve_forever()
