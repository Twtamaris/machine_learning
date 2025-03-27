# Interactive Vision-Based Games

This repository contains two innovative interactive projects developed using Pygame, OpenCV, and deep learning techniques. Both projects leverage computer vision and custom-trained models to create engaging user experiences that blend real-time input with dynamic game mechanics.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Descriptions](#project-descriptions)
  - [Finger-Tracking Game](#finger-tracking-game)
  - [Eye-Tracker Game](#eye-tracker-game)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Custom Dataset and Training](#custom-dataset-and-training)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project explores interactive gaming using two distinct approaches:
1. **Finger-Tracking Game:** The game utilizes a camera to detect your finger and generate a random rectangle. The objective is to align your finger with the corresponding rectangle displayed in the Pygame window.
2. **Eye-Tracker Game:** This game displays multiple rectangles at random positions on the desktop. Using a deep learning model integrated with OpenCV, the system detects your eye gaze. When you look at a rectangle, it is deleted from the screen. The model also calculates your distance from the laptop and the angle of your eye, ensuring accurate detection. The eye tracker is trained on a custom dataset for improved performance.

---

## Features

- **Real-Time Finger Tracking:** Use your finger to interact with game elements as the camera detects and generates random rectangle boxes.
- **Gaze-Based Interaction:** Remove rectangles by simply looking at them, thanks to the deep learning-powered eye tracking.
- **Custom Deep Learning Model:** Trained on a personally curated dataset to enhance eye detection accuracy and user interaction.
- **Dynamic Game Mechanics:** Both games feature randomly generated rectangles to provide a unique challenge every time.

---

## Project Descriptions

### Finger-Tracking Game

- **Mechanism:** The camera detects your finger and generates a random rectangle. The challenge is to align or "select" the rectangle displayed in the Pygame window.
- **Objective:** Improve hand-eye coordination and reaction time through interactive visual feedback.
- **Technologies:** Pygame for game interface, OpenCV for camera capture and finger detection.

### Eye-Tracker Game

- **Mechanism:** Multiple rectangles appear randomly on your desktop. As the user’s gaze is detected using the custom deep learning model and OpenCV, the rectangle being looked at is removed from the screen.
- **Objective:** Engage the user in a unique interaction where eye movements control game progression.
- **Technologies:** Pygame for rendering game elements, OpenCV for video capture, and deep learning (e.g., TensorFlow/PyTorch) for eye tracking.
- **Additional Features:** 
  - **Distance Calculation:** The system calculates the user’s distance from the laptop.
  - **Angle Estimation:** The angle of the eye is computed to improve the precision of gaze detection.

---

## Setup and Installation

### Prerequisites

- **Python 3.x**
- **Pygame**
- **OpenCV**
- **Deep Learning Framework:** (TensorFlow or PyTorch, depending on your implementation)
- **Other Python Packages:** Numpy, etc.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/interactive-vision-games.git
   cd interactive-vision-games
