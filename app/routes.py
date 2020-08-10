from flask import render_template, request
from app import app
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route('/main')
def main():
    # return "Hello, World!"
    return render_template('main.html')

@app.route('/sendfile', methods=["POST"])
def send_file():
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('main.html')
