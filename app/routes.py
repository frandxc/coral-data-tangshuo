from flask import request, render_template, redirect, url_for, send_from_directory
from app import app
import pandas as pd
import os

UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('visualize', filename=file.filename))
    return render_template('index.html')

@app.route('/visualize/<filename>')
def visualize(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)
    stats = df.describe().to_html()  # Example: Show data statistics
    return render_template('visualize.html', stats=stats)
