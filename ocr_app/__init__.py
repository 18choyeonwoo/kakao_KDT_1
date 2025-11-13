from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'static')
    )

    app.config['SECRET_KEY'] = 'mykey123'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ocr_results.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    db.init_app(app)

    # 업로드 폴더 생성
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Blueprint 등록
    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    from .sam_routes import sam_bp
    app.register_blueprint(sam_bp)


    with app.app_context():
        db.create_all()

    return app
