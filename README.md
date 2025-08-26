# Gesture-Controlled-Lamp
Control a 220V lamp using hand gestures with Arduino/ESP8266, OpenCV, and cvzone



---

# 🤖 Gesture-Controlled Smart Lamp

This project demonstrates how **Computer Vision**, **Embedded Systems**, and **Power Electronics** can work together to create a **gesture-controlled smart lamp**.
By using **OpenCV + cvzone** for real-time hand tracking and an **Arduino/ESP8266** with a relay for hardware control, the system allows a **220V AC lamp** to be switched ON/OFF using simple hand gestures.

---

## 🔹 Project Overview

* **Goal:** Control a 220V lamp using only hand gestures, without touching switches.
* **Technologies Used:**

  * **Python (OpenCV + cvzone):** Hand detection & gesture recognition
  * **Arduino/ESP8266:** Receives commands via Serial and controls relay
  * **Relay Module + Flywheel Diode:** Safe interfacing with 220V lamp
  * **Proteus Simulation:** Circuit testing before real implementation

This project reflects how combining **Power Electronics**, **Embedded Systems**, and **IoT concepts** can open doors to **smarter, safer, and more interactive solutions** in both home automation and industrial applications.

---

## 🔹 Features

* Real-time **hand tracking** with OpenCV + cvzone
* Detects which **fingers are raised** to decide actions
* Serial communication between Python and Arduino/ESP8266
* **Relay driver with flywheel diode** for safe control of 220V lamp
* Works in both **simulation (Proteus)** and **real hardware testing**

---

## 🔹 Hardware Requirements

* Arduino Uno / ESP8266 (NodeMCU)
* Relay Module (5V)
* Flywheel Diode (1N4007 recommended)
* NPN Transistor (e.g., 2N2222 or BC547) for relay driving
* 220V AC Lamp
* Jumper wires, Breadboard, Power supply

⚠️ **Safety Note:** When working with 220V AC, always ensure proper isolation and precautions. The relay must be opto-isolated or safely rated for AC loads.

---

## 🔹 Software Requirements

* Python 3.x
* OpenCV (`cv2`)
* cvzone (`pip install cvzone`)
* pySerial (`pip install pyserial`)
* Arduino IDE (for uploading `.ino` code)
* Proteus (for simulation, optional)
* com0com (Virtual Serial Port) → Required to link Proteus simulation with Python script

---

## 🔹 System Workflow

1. Camera captures video stream
2. Python + cvzone detect hand gestures
3. Recognized gesture → Python sends command (USB or virtual COM port) to Arduino/ESP8266
4. Arduino drives relay → Controls 220V lamp
5. Flywheel diode protects transistor from relay back EMF

---

## 🔹 Project Structure

```
Gesture-Controlled-Lamp/
│── Python_Code/
│   ├── main.py          # OpenCV + hand gesture detection
│   ├── controller.py    # Serial communication with Arduino/ESP8266
│
│── Arduino_Code/
│   ├── lamp_control.ino # Microcontroller code for relay control
│
│── Proteus_Simulation/
│   ├── lamp_circuit.pdsprj  # Simulation project file
│
│── README.md            # Project explanation (this file)
│── LICENSE              
```

---

## 🔹 How to Run


1. Install dependencies:

   ```bash
   pip install opencv-python cvzone pyserial
   ```
2. Connect Arduino/ESP8266 to PC and note the COM port
3. Upload `lamp_control.ino` to Arduino/ESP8266 using Arduino IDE
4. Run Python script:

   ```bash
   python main.py
   ```
5. Move your hand in front of the camera → Control the lamp!

---

## 🔹 Demo Video

🎥 Check out the demo showing both **Proteus simulation** and **real hardware test**.
👉

---

## 🔹 Applications

* Smart Home Automation (touchless light/fan control)
* IoT Systems (gesture-based commands)
* Industrial Automation (hands-free control for safety)
* Assistive Technology (for elderly or disabled users)

---

## 🔹 License

This project is licensed under the **MIT License** – feel free to use and modify with attribution.

---

## 🔹 Author

👤 **Ahmed Emad**
*Power Electrical Engineer | Embedded Systems & IoT Enthusiast*

