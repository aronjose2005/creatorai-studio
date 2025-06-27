import streamlit as st
from creator_summarizer import generate_summary, get_transcript_from_youtube

st.title("🎬 CreatorAI Studio - YouTube Summarizer")

video_url = st.text_input("🔗 Paste YouTube Video URL")

if video_url:
    with st.spinner("⏳ Fetching transcript..."):
        transcript = get_transcript_from_youtube(video_url)
    
    with st.spinner("🧠 Summarizing..."):
        summary = generate_summary(transcript)
    
    st.subheader("📄 Summary")
    st.write(summary)
    
    st.download_button("📥 Download Summary (.txt)", summary, file_name="summary.txt")

