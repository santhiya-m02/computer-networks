import socket 
# Define the server address and port 
SERVER_ADDRESS = '127.0.0.1' 
SERVER_PORT = 8888 
# Create a socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT)) # Send data to the server 
data = "Hello from the client!" 
client_socket.send(data.encode()) 
# Receive a response from the server 
response = client_socket.recv(1024) 
print(response.decode()) 
# Close the socket 
client_socket.close() 
