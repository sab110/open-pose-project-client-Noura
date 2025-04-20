# 🏋️ AI-Powered Squat Analysis System

This project is a **real-time squat form analysis tool** built with **MediaPipe**, **OpenCV**, and **Streamlit**. It allows users to upload a workout video and receive instant visual feedback and performance metrics such as rep count, form quality, and posture consistency.

## 🚀 Features

- 📤 Upload pre-recorded squat videos
- 🤖 AI-based form tracking using MediaPipe Pose
- 📈 Automatic rep counting
- ❌ Identification of improper squats
- 📊 Metrics: total reps, average quality, depth consistency, back angle consistency
- 💾 Save and download analysis results in JSON format
- 🎞️ Frame-by-frame video playback with controls

---

## 🧠 Tech Stack

- [Python](https://www.python.org/)
- [MediaPipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [Streamlit](https://streamlit.io/)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sab110/open-pose-project-client-Noura.git
cd <folder_name>
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Requirements include**:

- streamlit
- opencv-python
- numpy
- mediapipe

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501/`

---

## 📂 Project Structure

```
.
├── app.py                      # Main Streamlit interface
├── process_frame.py           # Pose processing logic
├── thresholds.py              # Angle thresholds for analysis
├── utils.py                   # Drawing & helper functions
├── analysis_results/          # Saved JSON reports
├── inputs/                   # Sample videos (optional)
└── README.md
```

---

## 📷 Tips for Best Results

- Ensure **good lighting**
- Wear **fitted clothing**
- Position the camera **side view** showing the full body
- Keep a **stable background**
- Perform squats at a **moderate, consistent pace**

---

## 📝 To-Do / Future Improvements

- [ ] Real-time webcam support
- [ ] CSV and Excel report exports
- [ ] Interactive charts (matplotlib / Plotly)
- [ ] Mobile-friendly UI
- [ ] Voice guidance for live feedback

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [MediaPipe by Google](https://github.com/google/mediapipe)
- [Streamlit](https://github.com/streamlit/streamlit)
- [OpenCV](https://opencv.org/)
