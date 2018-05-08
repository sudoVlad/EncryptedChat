import socket
#from ElGamal import *

#run Chat.py first
#then run Client.py
#type things into Client.py's terminal
#they will be sent to Chat.py's socket

def publicKey():
	#generate prime #make global
	#generate a	#make global
	#generate g	#creat this function

def decrypt(cipher):
	#elgamal = ElGamal(prime,halfMask, g)
	#message = elgamal.decrypt(cipher)
    print("stub")
    return message


#AF_INET specifies the adress family of the socket.. whatever that means
#SOCK_STREAM specifies TCP connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555

s.bind((host,port))
#listen for up to 5 incoming connections
s.listen(5)

def client(conn,addr):
    while True:
        #decode takes recieved byte code and turns it into ascii
        message = conn.recv(2048).decode("utf-8")
        if message:
            #decrypt me!!
            message = decrypt(message)
            #getting rid of the new line at the end
            message = message[:len(message)-1]
            print("<from: " + str (addr[0]) + "> " + message)
        else:
            break
    conn.close()

while True:
    conn,addr = s.accept()
    client(conn,addr)
