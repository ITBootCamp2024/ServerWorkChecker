import requests
from flask import Flask, send_file

app = Flask(__name__)

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
            // Отримання файлу з GitHub
            var githubFileUrl = 'https://raw.githubusercontent.com/ITBootCamp2024/ServerWorkChecker/main/1618010991_9-p-bushuyushchee-more-fentezi-9.jpg';
            
            // Створення тегу <a> для завантаження файлу
            var link = document.createElement('a');
            link.href = githubFileUrl;
            link.download = 'downloaded_file.jpg';
            link.target = '_blank'; // Встановлення атрибуту target для уникнення вспливаючого повідомлення

            // Додавання тегу <a> до DOM, але не додавання його до відображення
            document.body.appendChild(link);

            // Натискання на тег <a> для початку завантаження
            link.click();

            // Видалення тегу <a>, оскільки він більше не потрібен
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
