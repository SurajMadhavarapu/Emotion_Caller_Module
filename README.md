# 🎭 Emotion Caller — Real-Time Emotion Detection with Phone Link Integration

### 👨‍💻 Developed by: M. Suraj  
**3rd Year, B.Tech — Artificial Intelligence & Data Science, BVRIT**  
🧠 Built using Python, OpenCV, FER, PyTorch (GPU), and Automation

---

## 📘 Project Overview
**Emotion Caller** is an intelligent AI-based application that detects your real-time emotions using a webcam.  
If it detects **sadness** persisting for a few seconds, the system automatically opens the **Phone Link** app on Windows — allowing you to instantly connect with your best friend or support contact.

This project demonstrates how **AI-driven emotion recognition** can promote **mental well-being** through technology.

---

## ⚙️ Features
✅ Real-time emotion detection via webcam (FER + OpenCV)  
✅ Detects happiness, sadness, anger, surprise, and more  
✅ Automatic trigger for **Phone Link** app when sadness persists  
✅ GPU acceleration with PyTorch for faster performance  
✅ Safe and local — all processing happens on your computer  

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|------------------|
| Programming Language | Python 3.12 |
| Emotion Recognition | FER (Facial Emotion Recognition) |
| Video Capture | OpenCV |
| GPU Acceleration | PyTorch / CUDA |
| Automation | PyAutoGUI |
| System Integration | Windows Phone Link (`ms-phone:` command) |

---

## 🚀 How It Works

1. The webcam captures real-time frames using **OpenCV**.  
2. The **FER** model predicts the dominant emotion from each frame.  
3. If the emotion is **sad** with a confidence score above a threshold and lasts for a few seconds,  
   the system executes:
   ```python
   os.system("start ms-phone:")
# ⚙️ Installation and Setup Guide — Emotion Caller

This guide walks you through the complete setup for the **Emotion Caller** project —  
from folder creation to running the emotion detection app with GPU acceleration.

---

## 🧱 Step 1: Create the Project Folder

Open **PowerShell** or **Command Prompt** and run:

```bash
# Create the main project directory
mkdir Emotion_Caller_Module
cd Emotion_Caller_Module

# Create a subfolder for source code
mkdir Emo_caller
cd Emo_caller
# Create a Python virtual environment (using Python 3.12)
py -3.12 -m venv venv
# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
pip install opencv-python fer==22.4.0 mtcnn pyautogui torch torchvision torchaudio pillow requests tensorflow tensorflow-intel
# Create main script
New-Item auto_call_sadness.py -ItemType File

# Create a README file
New-Item README.md -ItemType File

# Create a requirements file
New-Item requirements.txt -ItemType File
python -c "import cv2, torch; print('OpenCV:', cv2.__version__, '| GPU available:', torch.cuda.is_available())"
python auto_call_sadness.py
