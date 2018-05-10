import socket
import sys
from Elgamal import *

# encrypt returns the encrypted character
# Parameters: b, message, pubKey
# returns the encrypted message in form of an array
def encrypt(message, pubKey):
    list_of_cipher_letters = []
    for i in range(0,len(message) - 1):
        cipher = elgamal_encrypt(message[i],pubKey)
        list_of_cipher_letters.append(cipher)
    return list_of_cipher_letters

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
host = socket.gethostbyname(host)
port = 5555

s.connect((host,port))

bit_length = input("Choose a bit length for the Elgamal prime: ")
s.send(str.encode(bit_length))

pubKey = s.recv(2048).decode()
pubKeyList = pubKey.split(', ')

#prime
pubKeyList[0] = int(pubKeyList[0])
#generator
pubKeyList[1] = int(pubKeyList[1])
#halfMask
pubKeyList[2] = int(pubKeyList[2])

aes_key = input("Choose a secret key for aes: ")

print("Waiting for input, connected to: " + host + " on port " + str(port))
print("type quit* to disconnect")



while True:
    msg = sys.stdin.readline()
    if (msg == "quit*\n"):
        break
    #great lets encrypt a message
    cipher_list = encrypt(msg, pubKeyList)
    cipher_string = ""
    for i in range(0,len(cipher_list) - 1):
        cipher_string += str(cipher_list[i])

    #encode turns our string into byte code to be sent to the socket
    #we send our elgamal encoded cipher to chat
    s.send(str.encode(cipher_string))

s.close()
