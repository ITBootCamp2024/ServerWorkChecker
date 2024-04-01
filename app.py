import requests
import os
from flask import Flask, send_file, request, make_response

app = Flask(__name__)

# HTML-код сторінки
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download File</title>
</head>
<body>
    <button id="downloadBtn">Download File</button>
    <script>
        document.getElementById('downloadBtn').addEventListener('click', function() {
            // Отримання файлу з GitHub
            var githubFileUrl = 'https://raw.githubusercontent.com/ITBootCamp2024/ServerWorkChecker/main/1618010991_9-p-bushuyushchee-more-fentezi-9.jpg';
            
            // Створення тегу <a> для завантаження файлу
            var link = document.createElement('a');
            link.href = githubFileUrl;
            link.setAttribute('download', 'downloaded_file.jpg');

            // Сховане натискання кнопки завантаження
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    </script>
</body>
</html>
"""

@app.route('/download')
def download_file():
    # Отримання файлу з GitHub
    github_file_url = 'https://raw.githubusercontent.com/ITBootCamp2024/ServerWorkChecker/main/1618010991_9-p-bushuyushchee-more-fentezi-9.jpg'
    response = requests.get(github_file_url)

    # Перевірка статусу відповіді
    if response.status_code == 200:
        # Налаштування заголовків для завантаження файлу
        response = make_response(response.content)
        response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.jpg"
        return response
    else:
        return 'Помилка при завантаженні файлу з GitHub'

@app.route('/')
def index():
    return html_content
        
if __name__ == '__main__':
    app.run(debug=True)
