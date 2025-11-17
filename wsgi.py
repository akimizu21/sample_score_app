import sys
import os

# プロジェクトルートをPythonパスに追加
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.flaskr import create_app

app = create_app()

if __name__ == "__main__":
    app.run()