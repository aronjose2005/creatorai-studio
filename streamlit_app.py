from creator_summarizer import generate_summary, get_transcript_from_youtube

# ✅ Declare the video URL FIRST
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 🎯 Get the transcript from YouTube
transcript = get_transcript_from_youtube(video_url)

# 🧠 Generate summary
summary = generate_summary(transcript)
print("\n🧠 Summary:\n", summary)

# 💾 Save to .txt
with open("summary.txt", "w") as f_txt:
    f_txt.write(summary)

# 💾 Save to .md
with open("summary.md", "w") as f_md:
    f_md.write(f"# 🎥 Summary for {video_url}\n\n{summary}")

