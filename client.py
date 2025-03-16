
import socket  

# Create a socket object  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Define server address  
HOST = '127.0.0.1'  
PORT = 12345  

# Connect to the server  
client_socket.connect((HOST, PORT))  

# Receive message from the server  
response = client_socket.recv(1024).decode()  
print(f"Server says: {response}")  

# Close the connection  
client_socket.close()  
