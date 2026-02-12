📢 Smart Edu Alerts
AI-Based Voice and Messaging System for Automated Fee and Attendance Notifications
👥 Team No: 2

Sk. Jaberulla – Dept. of Computer Science & Engineering,
Kara Sai Krishna Chandana,
Shaik Salma,
Chintala Kalpana Reddy,
Katikala Kiranmai – Dept. of Allied Computer Science & Engineering
Institution:
Vignan’s Lara Institute of Technology & Science, Vadlamudi

📌 Project Overview
Smart Edu Alerts is an AI-powered notification system designed to automate student fee and attendance communication between educational institutions and parents.
Traditional methods like phone calls, notice boards, and manual messaging are time-consuming, error-prone, and inefficient. This system leverages Artificial Intelligence, OCR, Machine Learning, Text-to-Speech (TTS), and Telegram integration to deliver instant voice and message alerts.
The system ensures:
->Timely communication
->Reduced manual workload
->Improved transparency
->Real-time alert delivery

🚀 Key Features
📂 Upload student data (CSV, Excel, PDF)
🔍 OCR-based data extraction
🤖 ML-based fee prediction/analysis
🔊 AI-based Voice Alerts using gTTS
💬 Telegram Bot Messaging Integration
🌐 Web Dashboard Interface
🗃️ MySQL/PostgreSQL compatible backend
📊 CSV-based student data processing

🛠️ Technologies Used
Python
Flask
OpenCV
OCR
gTTS (Google Text-to-Speech)
Telegram Bot API
Machine Learning (Scikit-learn)
Pickle (.pkl model files)
HTML (Frontend Templates)

📂 Project Folder Structure
SmartEduAlerts/
│
├── __pycache__/
├── database/
│
├── modules/
│   ├── __pycache__/
│   ├── analyzer.py
│   ├── ml_predictor.py
│   ├── ocr.py
│   ├── parser.py
│   ├── telegram_bot.py
│   ├── translator.py
│   ├── tts.py
│
├── static/
│   └── audio/
│       ├── en.mp3
│       ├── hi.mp3
│       ├── te.mp3
│       └── ur.mp3
│
├── templates/
│   ├── dashboard.html
│   ├── upload.html
│
├── app.py
├── config.py
├── data_full.csv
├── fee_encoder.pkl
├── ml_model.pkl
├── students.csv
├── train_model.py
├── training_data_full.csv
├── training_data.csv


⚙️ Module Description
🔹 app.py
Main Flask application file that runs the web server and connects all modules.

🔹 config.py
Contains configuration details like Telegram Bot Token and other credentials.

🔹 modules/
analyzer.py – Analyzes student attendance and fee records
ml_predictor.py – Uses trained ML model to predict fee-related outputs
ocr.py – Extracts text from uploaded PDF/Images
parser.py – Parses and processes CSV/Excel data
telegram_bot.py – Sends automated alerts via Telegram
translator.py – Multi-language message support
tts.py – Generates voice alerts using Text-to-Speech

🔹 static/audio/
Stores generated voice alert audio files in multiple languages:
English (en.mp3)
Hindi (hi.mp3)
Telugu (te.mp3)
Urdu (ur.mp3)

🔹 templates/
dashboard.html – Displays system dashboard
upload.html – Upload student data interface

🔹 ML Model Files
ml_model.pkl – Trained Machine Learning model
fee_encoder.pkl – Label encoder for fee data

🧠 Methodology
->Upload Student Records (CSV/PDF/Excel)
->OCR & Data Parsing
->ML-based Fee & Attendance Analysis
->Generate Alert Message
->Convert Message to Voice (TTS)
->Send Telegram Message + Voice Alert
-Dashboard Monitoring

🎯 Objectives
Automate attendance & fee notification system
Reduce administrative manual workload
Deliver real-time personalized alerts
Improve parent-institution communication

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Configure Telegram Bot
Edit config.py and add your Telegram Bot Token.
3️⃣ Train ML Model (Optional)
python train_model.py
4️⃣ Run Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000/

🔐 Future Enhancements
WhatsApp API Integration
SMS Gateway Support
Cloud Deployment
Admin Role Management
Real-time Attendance Tracking


