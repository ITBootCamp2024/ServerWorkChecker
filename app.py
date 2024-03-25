from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    file_path = 'images/1618010991_9-p-bushuyushchee-more-fentezi-9.jpg'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
