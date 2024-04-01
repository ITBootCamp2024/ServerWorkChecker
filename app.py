import requests
import os
from flask import Flask, send_file, request 

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
            link.download = 'downloaded_file.jpg';

            // Сховане натискання кнопки завантаження
            link.click();
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
        # Збереження файлу локально
        with open('downloaded_file.jpg', 'wb') as f:
            f.write(response.content)
        
        # Надсилання файлу користувачеві
        return send_file('downloaded_file.jpg', as_attachment=True)
    else:
        return 'Помилка при завантаженні файлу з GitHub'

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return html_content
        
if __name__ == '__main__':
    app.run(debug=True)
