from ..app import db  # Importar la instancia de SQLAlchemy creada en __init__.py
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    videos = db.relationship('Video', backref='usuario', lazy=True)

    @property
    def password(self):
        raise AttributeError('La contraseña no es un atributo legible.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(20), default='uploaded')  # 'uploaded', 'processed'
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
