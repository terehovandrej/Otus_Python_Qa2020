import socket
import json

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFFER_SIZE).decode("utf-8").strip()
            if data:
                http_request_headers: dict = {}
                headers = data.split(sep="\r\n")
                for i, header in enumerate(headers):
                    # Skip request type
                    if i == 0:
                        continue
                    header_name = header.split(sep=":")[0].strip()
                    header_value = header.split(sep=":")[1].strip()
                    http_request_headers[header_name] = header_value
                content = json.dumps(http_request_headers)
                conn.send(f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: application/json \n\n {content}".encode("utf-8"))
                break

