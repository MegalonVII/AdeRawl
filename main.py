# type: ignore
import re
import yt_dlp
from flask import Flask, render_template, request, redirect
from pytz import timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_link():
    youtube_url = request.form.get('youtube_url')
    if is_valid_url(youtube_url):
        direct_link = get_direct_link(youtube_url)
        if direct_link:
            return redirect(direct_link)
        else:
            return render_template('index.html', error_message='Raw video unavailable. Try again later.')
    else:
        return render_template('index.html', error_message='Invalid YouTube URL')

def is_valid_url(url):
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})"
    match = re.match(regex, url)
    return match is not None

def get_direct_link(youtube_url):
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'noplaylist': True,
            'username': 'oauth',
            'password': ''
        }
        try:
            ydl_opts['cookiefile'] = '/etc/secrets/cookies.txt'
        except:
            ydl_opts['cookiefile'] = 'cookies.txt'
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            direct_link = info_dict.get('url')
            return direct_link
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_login_time(tz: str) -> str:
    return f"\nLogged in at {datetime.now(timezone(tz)).strftime('%m/%d/%Y, %I:%M:%S %p')}\nTimezone: {tz}\n"

print(get_login_time('US/Eastern'))
app.run(host='0.0.0.0', port=80)
