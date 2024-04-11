from datetime import datetime
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
from application.models.models import db, Task
import os

video_blueprint = Blueprint('video', __name__)

@video_blueprint.route('/tasks', methods=['POST'])
def upload_video():

    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    
    file.save(filepath)

    new_task = Task(status='uploaded')
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': f'Video {filename} uploaded successfully', 'task_id': new_task.id}), 201
