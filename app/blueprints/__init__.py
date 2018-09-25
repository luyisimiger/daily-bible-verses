from app import app
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)
