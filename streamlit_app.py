import streamlit as st
from creator_summarizer import generate_summary, get_transcript_from_youtube

st.set_page_config(page_title="🎬 CreatorAI Studio", layout="centered")
st.title("🎬 CreatorAI Studio – YouTube & Text Summarizer")
st.markdown("👨‍💻 Built with ❤️ by **aronjose2005**")

option = st.radio("📥 Choose input method:", ["Paste YouTube URL", "Upload Transcript (.txt)"])

text_data = ""

if option == "Paste YouTube URL":
    video_url = st.text_input("📺 Enter YouTube Video URL")

    if video_url:
        with st.spinner("📤 Fetching transcript..."):
            try:
                text_data = get_transcript_from_youtube(video_url)
            except Exception as e:
                st.error(f"❌ Failed to fetch transcript:\n\n{e}")
elif option == "Upload Transcript (.txt)":
    uploaded_file = st.file_uploader("📤 Upload transcript .txt file", type="txt")
    if uploaded_file is not None:
        text_data = uploaded_file.read().decode("utf-8")

if text_data:
    with st.spinner("🧠 Generating summary..."):
        summary = generate_summary(text_data)

    st.subheader("🧠 Summary")
    st.write(summary)

    st.download_button("💾 Download .txt", summary, file_name="summary.txt")
    st.download_button("💾 Download .md", f"# 🎥 Summary\n\n{summary}", file_name="summary.md")

