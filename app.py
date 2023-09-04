from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download()
        original_file = video.default_filename
        new_file = original_file.replace(".mp4", ".mp3")
        os.rename(original_file, new_file)
        return send_file(new_file, as_attachment=True)
    except Exception as e:
        print(str(e))
        return "Error: Could not download or convert video."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
