import socket
import sys
#from ElGamal import *

#im not sure what the output will be here since we're doing both aes and elgamal
def encrypt(message):
	#b = randomly generate b
	#elgamal = ElGamal(prime, halfMask, g(	#this takes the public key)
	#message = ElGamal.encrypt(b, message)
    print("stub")
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

while True:
    msg = sys.stdin.readline()
    if (msg == "quit*\n"):
        break
    #ok here's where we encrypt
    msg = encrypt(msg)
    #encode turns our string into byte code to be sent to the socket
    s.send(str.encode(msg))

s.close()
