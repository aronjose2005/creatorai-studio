import streamlit as st
from creator_summarizer import get_transcript_from_youtube

st.set_page_config(page_title="CreatorAI Studio", layout="centered")
st.title("🎬 CreatorAI Studio – YouTube Video Summarizer")

video_url = st.text_input("📺 Paste YouTube Video URL")

if video_url:
    with st.spinner("📤 Fetching transcript..."):
        transcript = get_transcript_from_youtube(video_url)

    st.subheader("🧠 Transcript")
    st.write(transcript)

    st.download_button("💾 Download .txt", transcript, file_name="transcript.txt")
    st.download_button("💾 Download .md", f"# 🎥 Transcript for {video_url}\n\n{transcript}", file_name="transcript.md")

