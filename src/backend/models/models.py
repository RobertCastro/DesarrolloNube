from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicialización del objeto SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Asumo que quisiste referirte a 'password' en lugar de 'password1'
    email = db.Column(db.String(50), nullable=False, unique=True)

    # Relación uno a muchos: Un usuario puede tener muchas tareas
    tasks = db.relationship('Task', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    
    # Clave foránea para asociar una tarea con un usuario
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}, Status: {self.status}>'
