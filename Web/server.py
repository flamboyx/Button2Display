import socket
from _thread import *
from settings import *
from server_window import Window



def s_to_c(client, window):
    client.send(str.encode("Connected"))
    while True:
        try:
            data = client.recv(1024)
            reply = data.decode("utf-8")
            
            if not data or not window.running:
                print("Disconnected")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")
                
            if int(reply) != window.light: 
                window.changed = True
                window.light = int(reply)
                
            client.sendall(reply.encode("utf-8"))
        except:
            break
    
    print("Lost connection")
    client.close()
            

HOST = socket.gethostbyname_ex(socket.gethostname())[2][0]
PORT = 61020

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))   
server.listen(1)

print(f"{HOST}, {PORT}")

window = Window(f"{HOST} / {PORT}")
window.run()

while True:
    client, address = server.accept()
    print(f"Connected to: {address}")
    
    start_new_thread(s_to_c, (client, window))
    
    while window.running:
        window.run()
        
    if not window.running:
        break
    