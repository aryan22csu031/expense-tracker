from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'expensetracker'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def index():
    return render_template('analysis_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csvFile' not in request.files:
        return redirect(request.url)

    file = request.files['csvFile']
    if file.filename == '':
        return redirect(request.url)

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Call the dashboard.py script using subprocess to generate Streamlit output
        subprocess.run(['streamlit', 'run', 'dashboard.py', '--', '--file', file_path])

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
