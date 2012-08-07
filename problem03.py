import math

def primeFactor(n):
	limit = n / 2
	for i in reversed(xrange(2,limit)):
		print(i)
		if n % i == 0:
			print(i)
			if testPrime(i):
				print(i)
				break

def testPrime(n):
	limit = int(math.sqrt(n))
	for i in range(2,limit+1):
		if n % i == 0:
			return 0
	return 1


#primeFactor(10000000000)
primeFactor(600851475143)
