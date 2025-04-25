# Pose Recognition with Deep Learning in Sports Applications

## Introduction

This project introduces an AI-powered **Squat Analysis System** that leverages pose estimation and deep learning techniques to evaluate squat form in real-time using video input. Built using **MediaPipe**, **OpenCV**, and **Streamlit**, it accurately tracks key body landmarks and angles to classify posture, count repetitions, and provide actionable feedback. Designed for both beginners and professionals, this system offers a seamless and intuitive interface to help athletes and fitness enthusiasts enhance their workout performance while avoiding incorrect form that may lead to injury.

## Project Metadata

### Authors

- **Team:** [add name], [add others]
- **Supervisor Name:** [Supervisor Name]
- **Affiliations:**  University, Department of Business Analytics

### Project Documents

- **Presentation:** [Project Presentation](/[add link])
- **Report:** [Project Report](/[add link])

### Reference Paper

- [BlazePose: On-device Real-time Body Pose Tracking](https://arxiv.org/abs/2006.10204)

### Reference Dataset

- [CMU Panoptic Dataset](http://domedb.perception.cs.cmu.edu/)

## Project Technicalities

### Terminologies

- **Pose Estimation:** Technique to locate key human joints in images or video.
- **MediaPipe:** A framework by Google for building pipelines to process video, audio, and other multimedia.
- **Hip-Knee-Ankle Angle:** Used to assess depth and form during squats.
- **Offset Angle:** Measures camera alignment based on the nose-shoulder angle.
- **Inactivity Detection:** Mechanism to reset counters if no movement is detected for a defined time.
- **Squat States:** s1 (standing), s2 (transition), s3 (deep squat).
- **Real-Time Feedback:** Visual cues rendered on the video feed based on form.
- **Beginner vs. Pro Thresholds:** Different angle limits based on user expertise.

### Problem Statements

- **Problem 1:** Users often perform squats with incorrect posture, risking injuries.
- **Problem 2:** Manual form correction is not scalable in home workouts or online fitness training.
- **Problem 3:** Lack of real-time systems that give corrective feedback for body posture during workouts.

### Loopholes or Research Areas

- **Generalization:** Adapting the model to different lighting, clothing, and body types.
- **Camera Dependency:** Performance can degrade with poor camera placement or quality.
- **Lack of Depth Data:** 2D pose estimation might misinterpret depth or overlap issues.

### Problem vs. Ideation: Proposed 3 Ideas to Solve the Problems

1. **Pose Classification-Based Tracking:** Use joint angles and temporal movement to classify squat states.
2. **Camera Alignment Detection:** Ensure video quality by flagging poor camera placement.
3. **Feedback Overlay:** Visually overlay messages to correct form in real time.

### Proposed Solution: Code-Based Implementation

The repository implements a Streamlit-based video processing app with real-time squat detection and feedback. Key features include:

- **Beginner and Pro Modes:** Custom thresholds for joint angles.
- **Visual Feedback System:** Overlays for cues like "Lower your hips" or "Knee over toe."
- **Statistical Summary:** Total reps, improper reps, and quality metrics.

### Key Components

- **`app.py`**: Streamlit front-end for video upload, processing, and displaying metrics.
- **`process_frame.py`**: Core processing logic for pose estimation and feedback.
- **`thresholds.py`**: Defines angle thresholds for beginner and pro modes.
- **`utils.py`**: Drawing functions, angle calculations, and MediaPipe helpers.

## Model Workflow

1. **Input:**

   - **Video Upload:** User uploads a video through the web interface.
   - **MediaPipe Pose Detection:** Extracts joint landmarks from each frame.

2. **Squat Analysis:**

   - **Angle Calculation:** Calculates vertical angles for hip, knee, and ankle joints.
   - **Posture Classification:** Determines the squat state (`s1`, `s2`, `s3`) using thresholds.
   - **Feedback Logic:** Evaluates joint angles and provides visual warnings or positive feedback.

3. **Output:**

   - **Annotated Video Frames:** Each frame is rendered with joint overlays and messages.
   - **Statistical Metrics:** Reps count, incorrect form count, average quality, and more.

## How to Run the Code

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sab110/open-pose-project-client-Noura.git
   cd open-pose-project-client-Noura
   ```

2. **Set Up the Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch the App:**

   ```bash
   streamlit run app.py
   ```

4. **Upload a Video and Get Feedback:**

   - Choose **Beginner** or **Pro** mode.
   - Upload a workout video.
   - Watch real-time analysis and review workout metrics.

## Acknowledgments

- **Open-Source Contributors:** MediaPipe, OpenCV, and Streamlit teams.
- **Mentors & Reviewers:** Thank you to our mentors and supervisors for guiding this project.
- **Institutes:** Gratitude to [University Placeholders] for supporting this research and development.

---

