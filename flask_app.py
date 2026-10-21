import os
from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Создаём папку для загрузок, если её нет
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# HTML-шаблон для заданий 2 и 4
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Flask App</title></head>
<body>
    <h2>Задание 2: Форма приветствия</h2>
    <form method="POST" action="/greet">
        <input type="text" name="username" placeholder="Введите имя" required>
        <button type="submit">Поздороваться</button>
    </form>
    {% if greeting %}
        <h3 style="color: green;">{{ greeting }}</h3>
    {% endif %}

    <hr>

    <h2>Задание 4: Загрузка файла</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Загрузить</button>
    </form>
    {% if upload_msg %}
        <h3 style="color: blue;">{{ upload_msg }}</h3>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_PAGE)


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username')
    return render_template_string(HTML_PAGE, greeting=f"Привет, {name}!")


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template_string(HTML_PAGE, upload_msg="Файл не выбран")

    file = request.files['file']
    if file.filename == '':
        return render_template_string(HTML_PAGE, upload_msg="Имя файла пустое")

    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return render_template_string(HTML_PAGE, upload_msg=f"Файл '{filename}' успешно загружен!")

    return render_template_string(HTML_PAGE)


if __name__ == '__main__':
    app.run(debug=True, port=5000)