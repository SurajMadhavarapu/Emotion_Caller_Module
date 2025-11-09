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
