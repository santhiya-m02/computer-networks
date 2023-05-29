import socket 
# Define the server address and port 
SERVER_ADDRESS = '127.0.0.1' 
SERVER_PORT = 8888 
# Create a socket object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Bind the socket to the address and port 
server_socket.bind((SERVER_ADDRESS, SERVER_PORT)) 
# Listen for incoming connections (backlog of 5) 
server_socket.listen(5) 
print(f"Server is listening on {SERVER_ADDRESS}:{SERVER_PORT}") while True: 
 # Accept incoming connections 
 client_socket, client_address = server_socket.accept() 
 print(f"New client connected: {client_address}") 
 # Receive data from the client 
 data = client_socket.recv(1024) 
 # Process the data (TODO) 
 # Send a response back to the client 
 response = "Hello from the server!" 
 client_socket.send(response.encode()) 
 # Close the client socket 
 client_socket.close() 
