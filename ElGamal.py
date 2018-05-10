#! /usr/bin/python3
# File: 		ElGamal.py
# Version: 	Python3.6.4
import math
from Pulverizor import *

class ElGamal:
	def __init__(self, prime, halfMask, g):
		self.prime = prime
		self.halfMask = halfMask
		self.g = g
	
	# Encrypts each character in the message
	# Parameters: a, msg
	# Retuns an array of ascii numbers to represent the cipher
	def encrypt(a, msg):
		fullMask = findFullMask(a)	
		#encrypt each letter		
		cipher = [] 	
		for x in range(0, len(msg) - 1): 
			msg[x] = convert2ASCII(msg[x])							
			cipher.append(findCipher(msg[x],fullMask))				
		return cipher
	
	# Decrypts each character in the cipher
	# Parameters: b, cipher
	# Returns an array of characters to represent the message
	def decrypt(b, cipher):
		decrypt each letter
		fullMask = findFullMask(b)
		msg = []	
		for x in range(0, len(cipher) - 1):
			cipher[x] = findMessage(cipher[x],fullMask)			
		 	msg.append(convert2Char(cipher[x]))			
	
	# Finds the full mask
	# Parameters: a
	# Returns the halfmask raised to the secret value of the caller
	def findFullMask(a):
		return math.pow(self.halfMask,a) % self.prime				
	
	# Finds the cipher
	# Parameters: asciiNum, fullMask
	# Returns the ascii represetnation of message and the full mask
	def findCipher(asciiNum, fullMask):
		return asciiNum * fullMask % self.prime
	
	# Finds the message
	# Parameters: asciiNum, fullMask
	# Returns the product of the cipher and inverted full mask
	def findMessage(asciiNum, fullMask):
		invFullMask = Pulverizor(self.prime, fullMask)
		return asciiNum * invFullMask % prime

	# Converst the ascii number to characters
	# Parameters: letter
	# Returns ascii number of character
	def convert2ASCII(letter):
		return ord(letter)
	
	# Converts the characters to ascii number
	# Parameters: asciiNum
	# Returns the character version of ascii number
	def convert2Char(asciiNum):
		return chr(asciiNum)
