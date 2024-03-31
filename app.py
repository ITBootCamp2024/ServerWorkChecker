import requests
import os
from flask import Flask, send_file, request 

app = Flask(__name__)

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
    return f'Ваш браузер: {user_agent}'

@app.route('/clean')
def clean_download_folder():
    try:
        # Get the path to the download folder
        download_folder = r'C:\Users\User\Downloads'  # Replace this with the actual path

        # Check if the download folder exists
        if os.path.exists(download_folder):
            # Iterate over the files in the download folder and delete them
            for filename in os.listdir(download_folder):
                file_path = os.path.join(download_folder, filename)
                os.remove(file_path)
            return 'Download folder cleaned successfully'
        else:
            return 'Download folder does not exist'
    except Exception as e:
        return f'Error cleaning download folder: {e}'
        
if __name__ == '__main__':
    app.run(debug=True)
