import socket
import math
from Crypto.Util import number
import random
from ElGamal import *

#run Chat.py first
#then run Client.py
#type things into Client.py's terminal
#they will be sent to Chat.py's socket


# Parameters: prime
# returns the value of g 
def getG(prime):
    q = int((prime - 1) / 2)
    # we have a safe prime p
    #p = 2q + 1
    # now we need a generator of Zp*
    # any g < p is a generator iff:
    # g^1 not congruent 1 mod P
    # g^2 not congruent 1 mod P
    # and
    # g^q not congruent 1 mod P
    Generator = 2
    isGen = False
    while (isGen == False):
        if ((Generator - 1) % prime == 0 or (pow(Generator, 2) - 1) % prime == 0 or pow(int(Generator),q,int(prime)) == 1):
            Generator += 1
        else:
            isGen = True
    return Generator

# getPublicKey creates the public key
# Parameters: a, prime
# Returns the public key in from of an array where
def getPublicKey(a, prime):
    pubKey = []
    g = getG(prime)
    pubKey.append(prime)
    pubKey.append(g)
    pubKey.append(pow(g,a,prime))
    return pubKey


# decrypt returns the decrypted text
# Parameters: a, cipher
# Returns the decrypted message in an array
def decrypt(cipher, pubKey, a):
    return(elgamal_decrypt(cipher,pubKey,a))

#AF_INET specifies the adress family of the socket.. whatever that means
#SOCK_STREAM specifies TCP connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555

s.bind((host,port))
#listen for up to 5 incoming connections
s.listen(5)


def client(conn,addr):
    bit_length = conn.recv(2048).decode()

    #prime = number.getPrime(int(bit_length))
    prime = 1367

    a = random.randint(1,prime - 1)
    print("a: " + str(a))
    pubKey = getPublicKey(a,prime)

    pub_key_string = (str(pubKey[0]) + ", " + str(pubKey[1]) + ", "+ str(pubKey[2]))
    #prime,generator,halfmask
    conn.sendall(str.encode(pub_key_string))
    while True:

        #decode takes recieved byte code and turns it into ascii
        message = conn.recv(2048).decode("utf-8")

        if message:
			#decrypt me!!
            #great we have the cipher
            message = decrypt(message, pubKey, a)
            print("<from: " + str (addr[0]) + "> " + message)
        else:
            break
    conn.close()

while True:
    conn,addr = s.accept()
    client(conn,addr)
