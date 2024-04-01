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
    <title>Automatic File Download</title>
</head>
<body>
    <button id="downloadBtn">Download File</button>
    <script>
        document.getElementById('downloadBtn').addEventListener('click', function() {
            // Створення запиту на сервер для завантаження файлу
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/download', true);
            xhr.responseType = 'blob';

            xhr.onload = function() {
                if (xhr.status === 200) {
                    // Створення посилання для завантаження файлу
                    var url = window.URL.createObjectURL(xhr.response);
                    var a = document.createElement('a');
                    a.href = url;
                    a.download = 'downloaded_file.jpg';
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                }
            };

            xhr.send();
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
        
        # Надсилання файлу користувачеві з налаштуванням Content-Disposition для автоматичного завантаження
        return send_file('downloaded_file.jpg', as_attachment=True)
    else:
        return 'Помилка при завантаженні файлу з GitHub'

@app.route('/')
def index():
    return html_content
        
if __name__ == '__main__':
    app.run(debug=True)
