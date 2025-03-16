

import socket  

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Define host and port  
HOST = '127.0.0.1'  # Localhost  
PORT = 12345  # Choose any available port  

# Bind the socket to the address  
server_socket.bind((HOST, PORT))  

# Listen for incoming connections (1 client at a time)  
server_socket.listen(1)  
print(f"Server is listening on {HOST}:{PORT}...")  

# Accept client connection  
client_socket, client_address = server_socket.accept()  
print(f"Connection established with {client_address}")  

# Send a response to the client  
message = "Hello from the server!"
client_socket.send(message.encode())  

# Close the connection  
client_socket.close()  
server_socket.close()  
