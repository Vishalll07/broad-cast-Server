import sys
from server import start_server
from client import connect_client

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [start|connect]")
        sys.exit(1)

    command = sys.argv[1]

    host = "localhost"
    port = 8765

    if command == "start":
        start_server(host, port)
    elif command == "connect":
        connect_client(host, port)
    else:
        print("Invalid command. Use 'start' or 'connect'.")
