from youtube_transcript_api import YouTubeTranscriptApi
import requests
import re

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    return match.group(1) if match else None

def load_cookies():
    cookies = {}
    with open("cookies.txt", "r") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                parts = line.strip().split("\t")
                if len(parts) >= 7:
                    cookies[parts[5]] = parts[6]
    return cookies

def get_transcript_from_youtube(url):
    video_id = extract_video_id(url)
    cookies = load_cookies()

    # Set cookies in YouTubeTranscriptApi session
    from youtube_transcript_api._api import TranscriptApi
    session = requests.Session()
    session.cookies.update(cookies)
    TranscriptApi._TranscriptApi__requester.session = session

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return "\n".join([x['text'] for x in transcript])

def generate_summary(transcript):
    # Dummy summary generator – replace with your model later
    return " ".join(transcript.split()[:100]) + "..."

