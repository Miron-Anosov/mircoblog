"""Конфигурация Gunicorn."""

from src.core.settings.settings import settings

# Количество рабочих процессов Gunicorn
workers = settings.gunicorn.WORKERS

# Привязка к адресу
bind = settings.gunicorn.BUILD

# Уровень логирования
loglevel = settings.gunicorn.LOG_LEVEL

# Путь к приложению
wsgi_app = settings.gunicorn.WSGI_APP

# Класс рабочего процесса
worker_class = settings.gunicorn.WORKER_CLASS

# Дополнительные параметры (если нужно)
timeout = settings.gunicorn.TIMEOUT  # Таймаут для запросов
accesslog = settings.gunicorn.ACCESSLOG  # Логирование доступа в stdout
errorlog = settings.gunicorn.ERRORLOG  # Логирование ошибок в stdout
