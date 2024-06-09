# face_toolbox
Face detection, recognition and analysis toolbox built with Streamlit & DeepFace

# Why? 
For the sake of practicing building apps for computer vision and face detection/recognition in particular.

# What?
Python application built using DeepFace & Streamlit libraries. The application is intended to be hosted locally.
Planned functions:
## 1. Face detection.
Detec faces on an uploaded image. Results of detection will be both shown on a page with bounding boxes drawn and also will be available for export in CSV format.
## 2. Face recognition.
### 2.1 1-to-many
Face found on an uploaded image is compared with a pre-uploaded by user database of faces.
### 2.2 1-to-1
Two images are uploaded and then compared to answer if it's the same person on bot images.
## 3. Face analysis
Age, gender, race, emotions etc. Haven't tackled with that yet.

# How?
* DeepFace library is publicly available Python library that implements or interfaces multiple computer vision models for various face image processing tasks.
* Streamlit is a handy Python framework for fast developed machine learning demo applications
