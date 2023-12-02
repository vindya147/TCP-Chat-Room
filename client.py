import socket
import threading

#Chossing Label
label = input("Enter your Label:")

#Connecting To Server
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

#Listening to Server and Sending Label
def receive():
    while True:
        try:
            #Receive Message From Server
            #if 'vindi' Send Label
            message = client.recv(1024).decode('ascii')
            if message == 'vindi':
                client.send(label.encode('ascii'))
            else:
                print(message)
        except:
            #Close Connection When Error
            print("An error!!!!!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(label,input(''))
        client.send(message.encode('ascii'))


#Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()