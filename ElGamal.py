#! /usr/bin/python3
# File: 		ElGamal.py
# Version: 	Python3.6.4
import math
#from Pulverizor import *

class ElGamal:
	def __init__(self, prime, halfMask, g):
		#	self.prime = prime
		#	self.halfMask = halfMask
		#	self.g = g

	def encrypt(a, msg):
		#fullMask = findFullMask(halfMask,a) % prime		#calcualte fullmask
		#encrypt each letter		
		#cipher = [] #initialize our cipher array			
		#for x in range(0, len(msg) - 1): 
		#	msg[x] = convert2ASCII(msg[x])					#convert letters to ascii
		#	cipher.append(findCipher(msg[x],fullMask))	#add ascii numbers to cipher array
		#return cipher

	def decrypt(cipher):
		#invFullMask = pulverizor(prime, fullMask)		#calculate (fullmask)^-1
		#decrypt each letter
		#msg = []	#initialize our message array
		#for x in range(0, len(cipher) - 1):
		#	cipher[x] = findCipher(cipher[x], fullMask)	#multiply fullmask and ascii number
		# 	msg.append(convert2Char(cipher[x])				#add ascii letter to message array
	
	def findFullMask(halfMask, a):
		#return math.pow(halfMask,a) % prime				
	
	def findCipher(number, fullMask):
		#return number * fullMask % prime

	def findMessage(number, invFullMask):
		#return number * invFullMask % prime

	def convert2ASCII(letter):
		#return ord(letter)
	
	def convert2Char(number):
		#return chr(number)
