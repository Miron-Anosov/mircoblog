"""Конфигурация Gunicorn."""

import os
from multiprocessing import cpu_count

# Количество рабочих процессов Gunicorn
workers = cpu_count()

# Привязка к адресу
bind = "unix:/tmp/gunicorn.sock"

# Уровень логирования
loglevel = os.getenv("LOG_LEVEL")

# Путь к приложению
wsgi_app = "src.main:create_app()"

# Класс рабочего процесса
worker_class = "uvicorn.workers.UvicornWorker"

# Дополнительные параметры (если нужно)
timeout = os.getenv("TIMEOUT")  # Таймаут для запросов
accesslog = "-"  # Логирование доступа в stdout
errorlog = "-"  # Логирование ошибок в stdout
