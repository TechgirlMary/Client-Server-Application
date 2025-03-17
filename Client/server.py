import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12346))
server_socket.listen(1)

print("Server is listening on port 12345...")
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    client_message = conn.recv(1024).decode()
    if client_message.lower() == "exit":
        print("Client disconnected.")
        break
    print(f"Client: {client_message}")

    server_message = input("Server: ")
    conn.sendall(server_message.encode())

conn.close()
server_socket.close()
