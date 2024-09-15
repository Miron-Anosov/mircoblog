"""Конфигурация Gunicorn."""

from multiprocessing import cpu_count

# Количество рабочих процессов Gunicorn
workers = cpu_count() * 2 + 1

# Привязка к адресу
bind = "unix:/tmp/gunicorn.sock"

# Уровень логирования
loglevel = "info"

# Путь к приложению
wsgi_app = "src.main:create_app()"

# Класс рабочего процесса
worker_class = "uvicorn.workers.UvicornWorker"

# Дополнительные параметры (если нужно)
timeout = 30  # Таймаут для запросов
accesslog = "-"  # Логирование доступа в stdout
errorlog = "-"  # Логирование ошибок в stdout
