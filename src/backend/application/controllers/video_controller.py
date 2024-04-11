from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
from application.models.models import db, Task
import os

video_blueprint = Blueprint('video', __name__)

@video_blueprint.route('/tasks', methods=['POST'])
def upload_video():
    # print('Request files:', request.files)
    # return jsonify({'message': 'Hello from the video controller!'}), 200
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    
    # Guardar el archivo en el sistema de archivos
    file.save(filepath)

    # Asumiendo que el user_id se obtiene de algún mecanismo de autenticación
    user_id = 1  # Debes reemplazar esto con el id del usuario actual

    # Crear y guardar una nueva tarea en la base de datos
    new_task = Task(user_id=user_id, file_path=filepath, status='uploaded')
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': f'Video {filename} uploaded successfully', 'task_id': new_task.id}), 201
