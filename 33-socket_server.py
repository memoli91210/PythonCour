import socket
import threading

class ThreadForClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn=conn
        
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)


host, port=('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("serveur st demarer ...")

while True:
    socket.listen(5)
    conn, address= socket.accept()
    print("en ecoute...")
    
    my_thread= ThreadForClient(conn)
    my_thread.start()
    
conn.close()
socket.close()