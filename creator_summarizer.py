import requests
import re

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

# Extract the YouTube video ID from URL
def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    return match.group(1) if match else None

# Get transcript using YouTube internal API
def get_transcript_from_youtube(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "❌ Invalid YouTube URL"

    cookies = load_cookies_from_txt()

    session = requests.Session()
    session.cookies.update(cookies)

    # Internal YouTube API endpoint (requires cookies)
    endpoint = "https://www.youtube.com/youtubei/v1/get_transcript?key=AIzaSyA-9dDU6o4dZoYAw4-tOERDys_5GUgHHiY"

    payload = {
        "context": {
            "client": {
                "hl": "en",
                "clientName": "WEB",
                "clientVersion": "2.20210721.00.00"
            }
        },
        "videoId": video_id
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = session.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "actions" not in data:
            return "❌ No transcript found"

        events = data["actions"][0]["updateEngagementPanelAction"]["content"]["transcriptRenderer"]["body"]["transcriptBodyRenderer"]["cueGroups"]
        lines = [cue["transcriptCueGroupRenderer"]["cues"][0]["transcriptCueRenderer"]["cue"]["simpleText"] for cue in events]
        return "\n".join(lines)

    except requests.exceptions.RequestException as e:
        return f"❌ YouTube API error: {e}"
    except Exception as e:
        return f"❌ Unexpected error: {e}"

