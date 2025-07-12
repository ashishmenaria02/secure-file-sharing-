import socket
from Crypto.Cipher import AES
import os

key = b'ThisIsASecretKey'  # 16-byte AES key

def pad(data):
    return data + b"\0" * (16 - len(data) % 16)

def encrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data))

def decrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data).rstrip(b"\0")

# SERVER
def start_server():
    s = socket.socket()
    s.bind(('0.0.0.0', 9999))
    s.listen(1)
    print("🔒 Server listening...")

    conn, addr = s.accept()
    print(f"Connected by {addr}")

    with open("received_file.enc", "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(decrypt(data))

    print("✅ File received and decrypted.")
    conn.close()

# CLIENT
def send_file(filename, ip='127.0.0.1'):
    s = socket.socket()
    s.connect((ip, 9999))

    with open(filename, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.send(encrypt(data))

    print("✅ File sent successfully.")
    s.close()
