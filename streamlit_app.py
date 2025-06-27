import streamlit as st
from creator_summarizer import generate_summary, get_transcript_from_youtube

st.set_page_config(page_title="CreatorAI Studio", page_icon="🎬")
st.title("🎬 CreatorAI Studio")

video_url = st.text_input("📺 Paste YouTube Video URL")

if video_url:
    with st.spinner("🧠 Fetching transcript..."):
        transcript = get_transcript_from_youtube(video_url)

    with st.spinner("🔎 Summarizing..."):
        summary = generate_summary(transcript)

    st.subheader("📄 Summary")
    st.write(summary)

    st.download_button("⬇️ Download as .txt", summary, file_name="summary.txt")

