from flask import Flask, render_template
import os

app = Flask(__name__)
BASE_DIR = 'static/uploads'

@app.route('/')
def index():
    categories = os.listdir(BASE_DIR)
    return render_template('gallery.html', categories=categories)

@app.route('/gallery/<category>')
def gallery(category):
    path = os.path.join(BASE_DIR, category)
    if not os.path.exists(path):
        return f"{category} 카테고리가 없습니다."
    files = os.listdir(path)
    image_paths = [f"/{path}/{file}" for file in files]
    return render_template('category_gallery.html', category=category, images=image_paths)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)

