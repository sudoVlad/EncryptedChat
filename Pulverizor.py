#! /usr/bin/python3
#	File:			Pulverizor.py
#	Version:		Python 3.6.4

class Pulverizor:

	def __init__(self, prime, value):
		self.prime = prime
		self.value = value
		pulverizor(value, prime, 0, 0, 1, 0, 0, 1, prime)
	

	# Calculates the inverse using the pulverizor
	# Parameters: large value, small value, quotient, remainder, x1, y1, x2, y2, prime p
	# Returns: value
	def pulverizor(large, small, Q, R, x1, y1, x2, y2, p):
		#deals with negative modulos in the large/small arguments
		if large < 0:
			large = large % p
		if small < 0:
			small = small % p
	
		#check for proper order
		if small > large :
			temp = small
			small = large
			large = temp

		#initialize variables
		Q = int(large/small)
		R = abs(large - (Q * small))

		#base case
		if R == 0:	
			if y2 < 0:
				y2 = y2 % p
			return y2		 
		else:
			#reset variables
			x0 = x1 - (Q * x2)
			y0 = y1 - (Q * y2)		
			x1 = x2
			y1 = y2
			large = small
			small = R	

		#recurisve step
		return pulverizor(large, small, Q, R, x1, y1, x0, y0, p)
