import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
import time
from process_frame import ProcessFrame
from thresholds import get_thresholds_beginner, get_thresholds_pro
import tempfile
from datetime import datetime
import json
import os
import threading
from queue import Queue

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Page config
st.set_page_config(
    page_title="🏋️ Squat Analysis System",
    page_icon="🏋️",
    layout="wide"
)

# Styles
st.markdown("""
<style>
    .main { background-color: #f9f9f9; }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .metric-label {
        font-weight: bold;
        color: #444;
    }
    .block-container {
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🏋️ Squat Analysis System")
st.markdown("""
Welcome to the AI-powered **Squat Analysis App**!  
Upload your workout video, and get automatic feedback on your squat form, rep count, and quality metrics.
""")

# Session state setup
for key in ['video_playing', 'current_frame', 'video_path', 'processed_frames',
            'processing_complete', 'analysis_results']:
    if key not in st.session_state:
        st.session_state[key] = False if key == 'video_playing' else [] if key in ['processed_frames', 'analysis_results'] else None

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    difficulty = st.radio("Select Difficulty Level:", ["Beginner", "Pro"], index=0)

if 'frame_processor' not in st.session_state:
    st.session_state.frame_processor = ProcessFrame(
        get_thresholds_beginner() if difficulty == "Beginner" else get_thresholds_pro()
    )

# Video processor function
def process_video(video_path, frame_processor, progress_queue, result_queue):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    processed_frames = []

    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, _ = frame_processor.process(frame, pose)
        processed_frames.append(processed_frame)

        progress = (i + 1) / total_frames * 100
        progress_queue.put(progress)

    stats = frame_processor.get_workout_summary()
    cap.release()
    result_queue.put((processed_frames, stats))

# Layout columns
col1, col2 = st.columns(2)

# Upload & Process Section
with col1:
    st.header("📤 Upload Your Video")
    uploaded_file = st.file_uploader("Upload a video of your squat workout", type=["mp4", "avi", "mov"])

    if uploaded_file and not st.session_state.processing_complete:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
            tmp_file.write(uploaded_file.read())
            st.session_state.video_path = tmp_file.name

        progress_queue = Queue()
        result_queue = Queue()

        video_path = st.session_state.video_path
        frame_processor = st.session_state.frame_processor

        thread = threading.Thread(
            target=process_video,
            args=(video_path, frame_processor, progress_queue, result_queue)
        )
        thread.start()

        progress_bar = st.progress(0)
        status_text = st.empty()

        while thread.is_alive():
            try:
                progress = progress_queue.get(timeout=0.1)
                progress_bar.progress(progress / 100.0)
                status_text.info(f"🔄 Processing video: {progress:.1f}%")
            except:
                pass

        thread.join()

        if not result_queue.empty():
            st.session_state.processed_frames, stats = result_queue.get()
            st.session_state.processing_complete = True

            if stats:
                st.session_state.analysis_results.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "stats": stats
                })

    if st.session_state.processed_frames:
        st.markdown("### ▶️ Playback Controls")
        col_playback = st.columns(3)
        with col_playback[0]:
            if st.button("⏮️ Rewind"):
                st.session_state.current_frame = max(0, st.session_state.current_frame - 30)
        with col_playback[1]:
            if st.button("⏯️ Play/Pause"):
                st.session_state.video_playing = not st.session_state.video_playing
        with col_playback[2]:
            if st.button("⏭️ Forward"):
                st.session_state.current_frame = min(len(st.session_state.processed_frames) - 1, st.session_state.current_frame + 30)

        frame_number = st.slider(
            "🎞️ Frame",
            0,
            len(st.session_state.processed_frames) - 1,
            st.session_state.current_frame,
            key="frame_slider"
        )
        if frame_number != st.session_state.current_frame:
            st.session_state.current_frame = frame_number

        st.image(st.session_state.processed_frames[st.session_state.current_frame], channels="BGR", use_column_width=True)

        if st.session_state.video_playing:
            st.session_state.current_frame = (st.session_state.current_frame + 1) % len(st.session_state.processed_frames)
            time.sleep(0.03)
            st.rerun()

# Analysis Summary Section
with col2:
    st.header("📊 Analysis & Summary")
    if st.session_state.analysis_results:
        latest_stats = st.session_state.analysis_results[-1]["stats"]
        st.subheader("🏁 Workout Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Total Reps", latest_stats['total_reps'])
            st.metric("❌ Improper Reps", latest_stats['improper_reps'])
        with col2:
            st.metric("📈 Avg Quality", f"{latest_stats['average_quality']:.1f}%")
            st.metric("🏅 Best Rep", f"{latest_stats['best_rep_quality']:.1f}%")
        with col3:
            st.metric("📏 Depth Consistency", f"{latest_stats['depth_consistency']:.1f}")
            st.metric("📐 Back Angle", f"{latest_stats['back_angle_consistency']:.1f}")

        if st.button("💾 Save Results"):
            os.makedirs("analysis_results", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"analysis_results/squat_analysis_{timestamp}.json"
            with open(filename, "w") as f:
                json.dump(latest_stats, f, indent=4)
            st.success(f"Results saved to `{filename}`")

            # Provide download link
            with open(filename, "r") as file:
                st.download_button(
                    label="⬇️ Download JSON",
                    data=file,
                    file_name=os.path.basename(filename),
                    mime="application/json"
                )

# Analysis History Section
if st.session_state.analysis_results:
    st.markdown("---")
    st.subheader("🕓 Previous Analyses")
    for result in reversed(st.session_state.analysis_results):
        with st.expander(f"📅 {result['timestamp']}"):
            st.json(result['stats'])

# Tips Section
st.markdown("---")
st.markdown("""
### 📝 Tips for Best Video:
- 🎥 Keep your **entire body visible** in the frame  
- 💡 Ensure **good lighting**  
- 👕 Wear **fitted clothes**  
- 🕺 Perform squats at a **moderate and consistent pace**
""")
