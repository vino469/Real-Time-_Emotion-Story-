# Real-Time Emotion Story Generator

## Overview

Real-Time Emotion Story Generator is a Computer Vision and Artificial Intelligence application that detects a user's facial emotion through a live webcam feed and generates motivational stories based on the detected emotional state.

The project combines facial emotion recognition using DeepFace with real-time video processing using OpenCV to create an interactive and engaging user experience. The system continuously analyzes facial expressions, identifies the dominant emotion, and displays an emotion-specific motivational story on the screen.

---

## Features

* Real-time webcam video capture and processing
* Facial emotion detection using DeepFace
* Detection of dominant emotional states
* Emotion confidence score visualization
* Emotion-based motivational story generation
* Real-time display using OpenCV
* Automatic emotion monitoring
* Interactive user controls
* Lightweight and efficient implementation

---

## Supported Emotions

* Happy
* Sad
* Angry
* Fear
* Surprise
* Neutral
* Disgust

---

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* OpenCV
* DeepFace
* TensorFlow
* NumPy
* Anthropic API (Optional)
* Threading
* TextWrap

### Concepts

* Computer Vision
* Facial Emotion Recognition
* Deep Learning
* Real-Time Video Processing
* Human-Computer Interaction
* Artificial Intelligence

---

## System Workflow

1. Capture live video from the webcam.
2. Process video frames using DeepFace.
3. Detect facial emotions and identify the dominant emotion.
4. Calculate confidence scores for detected emotions.
5. Generate a motivational story based on the detected emotion.
6. Display the emotion and story on the video feed.
7. Continuously update results in real time.

---

## Project Structure

```text
Emotion-Story-Generator/
│
├── emotion_story.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/emotion-story-generator.git
cd emotion-story-generator
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```txt
opencv-python
deepface
numpy
tensorflow==2.15.0
tf-keras
anthropic
```

---

## Running the Application

```bash
python emotion_story.py
```

---

## Controls

| Key | Function             |
| --- | -------------------- |
| S   | Generate a new story |
| Q   | Exit the application |

---

## Applications

* Emotion-aware intelligent systems
* Interactive AI applications
* Computer Vision projects
* Human-Computer Interaction research
* Educational AI demonstrations
* Emotion-based storytelling systems

---

## Future Enhancements

* Voice-based story narration
* Multi-face emotion detection
* Emotion analytics dashboard
* Story history management
* Web deployment using Streamlit
* Advanced AI-generated storytelling
* Emotion trend visualization

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Computer Vision
* Facial Emotion Recognition
* Deep Learning Integration
* OpenCV Application Development
* Real-Time Video Processing
* Interactive AI Systems
* Python Programming
