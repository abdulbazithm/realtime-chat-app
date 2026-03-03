# 💬 Real-Time Individual Chat Application

## 🚀 Overview

A real-time one-to-one chat application built using **Django** and **Django Channels** implementing WebSocket-based communication.

The system follows strict **MVT architecture** and supports authenticated real-time messaging with presence tracking and read receipts.

## 🛠 Tech Stack

- Python 3.x
- Django
- Django Channels (ASGI + Daphne)
- SQLite
- HTML, CSS, JavaScript
- Bootstrap

## ✨ Features

### 🔐 Authentication
- User Registration
- User Login / Logout
- Auth-protected chat access

### 💬 Real-Time Messaging
- WebSocket-based one-to-one chat
- Messages stored in SQLite
- Auto-scroll to latest message
- Private individual conversations
### 👀 Read Receipts
- ✓ Single tick → Message sent
- ✓✓ Double tick → Message read

### 🟢 Online Presence
- Live online/offline indicator
- Presence broadcasting via channel layer groups

### 🔔 Unread Message Count
- Displays unread message count on user list page

### 🗑 Message Deletion
- Users can delete their own messages


## 🏗 Project Architecture (MVT)

- **Models** → Custom User & Message models  
- **Views** → HTTP request handling & message read logic  
- **Templates** → UI rendering  
- **Consumers** → WebSocket communication logic  
- **ASGI + Daphne** → Real-time server handling  

Business logic is separated properly and not placed inside templates.


# ⚙ Installation & Setup (Local Development)

# clone the Repository

git clone https://github.com/abdulbazithm/realtime-chat-app 
cd chat_app

Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Apply Database Migrations
python manage.py migrate

Create Superuser (Optional – for Admin Panel)
python manage.py createsuperuser

Run the Application (ASGI Server)
daphne chat_app.asgi:application
The application will run at:
http://127.0.0.1:8000/
Test Credentials (For Evaluation)
Example:
•	Username: abm@gmail.com
•	Password: abm@1234


🌐 Live Deployment
Deployed using Railway (ASGI + Daphne).
Live Link:
👉 https://web-production-cb5dc.up.railway.app

📌 Technical Highlights
•	Authenticated WebSocket handling using AuthMiddlewareStack
•	Real-time presence tracking
•	Database-backed read receipt logic
•	Unread message counting using efficient queries
•	Clean Bootstrap UI
•	Production-ready project structure






