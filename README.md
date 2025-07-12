# 🔐 Secure File Sharing System

A socket-based encrypted file transfer system built in Python using AES encryption for secure peer-to-peer communication.

---

## 💡 Features

- AES Encryption (128-bit)
- Peer-to-peer file transfer via sockets
- Encrypts data before sending
- Decrypts and reconstructs file on receiver’s end
- Cross-platform (runs on Python 3)

---

## 📁 How It Works

- **Client** selects a file and sends it in chunks
- Each chunk is encrypted using AES and sent over a socket
- **Server** receives the chunks, decrypts, and saves the original file

---

## 🛠️ Tech Stack

- Python 3
- Socket Programming
- PyCryptodome for AES

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
