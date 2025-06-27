from transformers import pipeline

# Load Hugging Face summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript_from_youtube(video_url):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([d["text"] for d in transcript])
    except Exception as e:
        return f"[Error extracting transcript] {e}"

