import socket
import sys
from ElGamal import *
import random

# encrypt returns the encrypted character
# Parameters: b, message, pubKey
# returns the encrypted message in form of an array
def encrypt(b, message, pubKey):
	elgamal = ElGamal(pubKey[0],pubKey[1],pubKey[2])
	message = ElGamal.encrypt(b, message)
  	#print("stub")
  	return message

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
host = socket.gethostbyname(host)
port = 5555

s.connect((host,port))

bit_length = input("Choose a bit length for the Elgamal prime: ")
aes_key = input("Choose a secret key for aes: ")
print("Waiting for input, connected to: " + host + " on port " + str(port))
print("type quit* to disconnect")

#pubKey = public keys received from Chat.py
b = random.randint(100000,99999)	#generate random b

while True:
	msg = sys.stdin.readline()
	if (msg == "quit*\n"):
		break
   #ok here's where we encrypt
   msg = encrypt(b,msg,pubKey)
	#encode turns our string into byte code to be sent to the socket
	s.send(str.encode(msg))

s.close()
