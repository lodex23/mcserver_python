import os
import socket
def server_program():
	# get the hostname
	host = socket.gethostname()
	port = 5000 

	server_socket = socket.socket()
	server_socket.bind((host, port))
	

	server_socket.listen(2)
	conn, adress = server_socket.accept()
	print("Connection from: " + str(adress))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("from connected user: " + str(data))

		if data == "connect":
			os.system('open bedrock')
		elif data == "disconnect":
			os.system('pkill mousepad')
		else:
		    print("Failed")

		data = "Task Completed"
		conn.send(data.encode())
	
	if not conn:
		os.system('python3 mcserver_controller.py')
server_program()
