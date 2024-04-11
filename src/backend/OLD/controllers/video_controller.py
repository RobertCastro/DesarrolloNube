from flask import request, jsonify
from werkzeug.utils import secure_filename
from ..models.models import db, Task
import os


# Directorio donde se guardarán los videos subidos
UPLOAD_FOLDER = '/path/to/upload/directory'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_video():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'message': 'No selected file or invalid file type'}), 400
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Asumiendo que ya se ha manejado la autenticación y tenemos el user_id
    user_id = 1  # Este es solo un ejemplo, necesitarás obtener el user_id del usuario autenticado

    new_task = Task(user_id=user_id, file_path=file_path, status='uploaded')
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully', 'task_id': new_task.id}), 201
