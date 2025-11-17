from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import pathlib

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # 環境変数の読み込み（Renderでは不要だが、ローカル開発用に残す）
    load_dotenv(dotenv_path=pathlib.Path(__file__).resolve().parents[1] / ".env", override=True)
    
    app = Flask(__name__)

    # Render/Neonの DATABASE_URL を取得
    db_url = os.getenv("DATABASE_URL", "").strip()
    
    # Render環境では postgres:// で始まる場合があるため変換
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql+psycopg2://", 1)
    
    if not db_url:
        raise RuntimeError("DATABASE_URL が未設定です。.envファイルまたは環境変数を確認してください。")

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # SECRET_KEY の設定（本番環境では必ず環境変数から取得）
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

    db.init_app(app)
    migrate.init_app(app, db)
    
    # CORS設定（必要に応じてオリジンを制限）
    CORS(app, resources={
        r"/api/*": {
            "origins": os.getenv("CORS_ORIGINS", "*").split(",")
        }
    })
    
    # --- Blueprint登録 ---
    from .route import bp
    from .routes.students import students_bp
    from .routes.exams import exams_bp
    from .routes.imports import imports_bp

    app.register_blueprint(bp)
    app.register_blueprint(students_bp, url_prefix="/api")
    app.register_blueprint(exams_bp, url_prefix="/api")
    app.register_blueprint(imports_bp, url_prefix="/api")
    
    return app