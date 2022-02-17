import socket

host, port=("localhost",5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host,port))
    print("client connecte")    
    data ="bonjour a toi, je suis le client"
    data=data.encode("utf8")
    socket.sendall(data)
except:
    print("connexion au serveur echoué")
finally:
    socket.close()