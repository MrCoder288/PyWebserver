import os
import shutil
from flask import Flask, render_template, request

app = Flask(__name__)

# Set the location for uploaded files
app.config['UPLOAD_FOLDER'] = '/home/kali/Website/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if os.path.isdir(file.filename):
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        shutil.copytree(file.filename, folder_path)
    else:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
