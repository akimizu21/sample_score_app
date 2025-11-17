# Gunicorn configuration file
import multiprocessing

# Server socket
bind = "0.0.0.0:10000"  # Renderのデフォルトポート
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000

# タイムアウトを延長（30秒 → 180秒）
# 大量データのインポート処理に対応
timeout = 180

keepalive = 2

# グレースフルタイムアウトも設定
graceful_timeout = 120

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'