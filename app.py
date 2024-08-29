from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        # Get the highest resolution stream with progressive=True
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not stream:
            print("No downloadable stream found. The video may be restricted or private.")
            return None

        # Download the video and return the file path
        output_path = stream.download()
        return output_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    output_path = download_youtube_video(video_url)
    
    if output_path and os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    else:
        return "Failed to download video. Please check the URL and try again."

if __name__ == "__main__":
    app.run(debug=True)
