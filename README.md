# Real-Time Individual Chat Application

## 🚀 Overview

This is a real-time one-to-one chat application built using:

- Python
- Django (MVT Architecture)
- Django Channels (WebSocket)
- SQLite
- HTML, CSS, JavaScript
- Bootstrap

The application allows authenticated users to chat in real-time with online presence tracking, read receipts, and unread message counts.

---

## ✅ Features

### 🔐 Authentication
- User Registration
- User Login
- Logout
- Auth-protected chat access

### 💬 Real-Time Chat
- WebSocket-based communication using Django Channels
- Messages stored in database
- Auto-scroll to latest message
- Private individual chat

### 👀 Read Receipts
- ✓ Single tick for sent messages
- ✓✓ Double tick for read messages

### 🟢 Online Status
- Live online/offline indicator
- Presence handled via WebSocket groups

### 🔔 Unread Message Count
- Shows unread message count in user list

### 🗑 Delete Message
- Users can delete their own messages

---

## 🏗 Project Architecture (MVT)

- **Models** → Custom User model and Message model
- **Views** → Handle HTTP requests and read logic
- **Templates** → Render UI
- **Consumers** → Handle WebSocket communication
- **ASGI + Daphne** → Real-time server

## 📌 Technical Highlights

- Authenticated WebSocket handling
- Real-time presence tracking
- Database-backed read receipts
- Clean UI using Bootstrap
- Production-ready project structure


## 🌐 Live Demo

Deployed using Railway with Daphne ASGI server.
Live Link: 
