import socket
import math
import pycrypto
from ElGamal import *

#run Chat.py first
#then run Client.py
#type things into Client.py's terminal
#they will be sent to Chat.py's socket

# getG generates an odd g
# Parameters: prime
# returns the value of g 
def getG(prime):
	q = 2 * prime + 1
	g = 1 
	while True:
		if (g is not 1) and (math.pow(g,2) is not 1) and (math.pow(g,q) is not 1):
			return g
		else:
			g = (2 * g) + 1

# getPublicKey creates the public key
# Parameters: a, prime
# Rieturns the public key in from of an array where
def getPublicKey(a, prime):
	pubKey = []
	g = getG(prime)				
	pubKey.append(prime) 			
	pubKey.append(g)					
	pubKey.append(math.pow(g,a))	
	return pubKey

# decrypt returns the decrypted text
# Parameters: a, cipher
# Returns the decrypted message in an array
def decrypt(a, cipher,pubKey):
	elgamal = ElGamal(pubKey[0],pubKey[1],pubKey[2])
	message = elgamal.decrypt(a, cipher)
   #print("stub")
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
	prime = crypto.util.number.getPrime() 
	b = random.randint(100000,99999)
	pubKey = getPublicKey(a,prime)	#this needs to be sent to client
	while True:
		#decode takes recieved byte code and turns it into ascii
     	message = conn.recv(2048).decode("utf-8")
    	if message:
     		#decrypt me!!
         message = decrypt(b,message,pubKey)
        	#getting rid of the new line at the end
        	message = message[:len(message)-1]
        	print("<from: " + str (addr[0]) + "> " + message)
		else:
      	break
	conn.close()

while True:
	conn,addr = s.accept()
	client(conn,addr)
