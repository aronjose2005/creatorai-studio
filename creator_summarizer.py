import requests
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._request import TranscriptRequester

# Load cookies from cookies.txt (Netscape format)
def load_cookies_from_txt():
    cookies = {}
    with open("cookies.txt", "r") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                parts = line.strip().split("\t")
                if len(parts) >= 7:
                    cookies[parts[5]] = parts[6]
    return cookies

# Inject cookies into custom HTTP requester
class PatchedTranscriptRequester(TranscriptRequester):
    def __init__(self, cookies):
        super().__init__()
        self.session.cookies.update(cookies)

# Extract video ID from YouTube URL
def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    return match.group(1) if match else None

# Use custom requester to fetch transcript
def get_transcript_from_youtube(url):
    video_id = extract_video_id(url)
    cookies = load_cookies_from_txt()
    requester = PatchedTranscriptRequester(cookies)
    transcript_api = YouTubeTranscriptApi(requester)
    transcript = transcript_api.get_transcript(video_id)
    return "\n".join([x['text'] for x in transcript])

# Dummy summary for now (replace with your model logic if needed)
def generate_summary(text):
    return "📄 Summary:\n\n" + text[:1000]  # Trimmed for display

