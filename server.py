import socket
import threading

#Connection Data
host = '127.0.0.1'#local host
port = 55555

#Starting Server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
 
#List For Clients and Their Label
clients=[]
labels=[]

#Sending Message To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

#Handling Messages From Clients
def handle(client):
    while True:
        try:
            #Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            #Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            label = labels[index]
            broadcast('{}left!'.format(index).encode('ascii'))
            labels.remove(label)
            break

#Receiving / Listening Function
def receive():
    while True:
        #Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        #Request And Store Label
        client.send('vindi'.encode('ascii'))
        label = client.recv(1024).decode('ascii')
        labels.append(label)
        clients.append(client)

        #Print And Broadcast Lable
        print("Label is {}".format(label))
        broadcast("{} Joined!!".format(label).encode('ascii'))

        #Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is Running.....!!")
receive()