import streamlit as st
from creator_summarizer import generate_summary, get_transcript_from_youtube

st.set_page_config(page_title="CreatorAI Studio", layout="centered")
st.title("🎬 CreatorAI Studio – YouTube Video Summarizer")

video_url = st.text_input("📺 Paste YouTube Video URL")

if video_url:
    with st.spinner("📤 Fetching transcript..."):
        transcript = get_transcript_from_youtube(video_url)

    with st.spinner("🧠 Generating summary..."):
        summary = generate_summary(transcript)

    st.subheader("🧠 Summary")
    st.write(summary)

    st.download_button("💾 Download .txt", summary, file_name="summary.txt")
    st.download_button("💾 Download .md", f"# 🎥 Summary for {video_url}\n\n{summary}", file_name="summary.md")

