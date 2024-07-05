from flask import Flask, request, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_video():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided.", 400
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=".", filename="video.mp4")
        
        return send_file("video.mp4", as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)

