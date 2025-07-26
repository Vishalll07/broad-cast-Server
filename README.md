# WebSocket Broadcast Server

A simple WebSocket-based broadcast chat server and client using Python’s `websockets` library. Multiple users can chat in real-time through the terminal.

## 📌 Features

- Real-time communication via WebSockets  
- Broadcasts messages from one client to all others  
- Each user is automatically assigned a name like `User 1`, `User 2`, etc.  
- Command-line interface  
- Colored message output for readability

## 🧰 Requirements

- Python 3.7+
- `websockets` library

Install with:

```bash
pip install websockets
```

## 🚀 Usage

### 1. Clone the repository

```bash
git clone https://github.com/Vishalll07/broad-cast-Server.git
cd broad-cast-Server
```

### 2. Start the Server

```bash
python main.py start
```

The server starts at `ws://localhost:8765` by default.

### 3. Start a Client

In a separate terminal window, run:

```bash
python main.py connect
```

You can start multiple clients to test broadcasting.

## 🎨 Output with Colors

- Messages received from others are shown in **cyan**
- Your messages remain in **white**
- Server join/leave messages may be added in **green** (if extended)

## 📁 Project Structure

```
broad-cast-Server/
├── client.py        # Client-side logic
├── server.py        # Server-side broadcasting logic
├── main.py          # Entry point to run server or client
└── README.md
```

## 🛣️ Roadmap

- [ ] Allow clients to set custom usernames
- [ ] Dockerize the project
- [ ] Add chat logging
- [ ] Handle client disconnections gracefully

## 🔗 Repository Link

GitHub: [https://github.com/Vishalll07/broad-cast-Server](https://github.com/Vishalll07/broad-cast-Server)
roadmap: (https://roadmap.sh/projects/broadcast-server)
