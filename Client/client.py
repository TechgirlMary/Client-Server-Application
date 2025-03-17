import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12346))

print("Connected to server. Type 'exit' to disconnect.")

while True:
    message = input("Client: ")
    client_socket.sendall(message.encode())
    
    if message.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

client_socket.close()
