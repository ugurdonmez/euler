import math

def primeFactor(n):
	for i in xrange(2,int(math.sqrt(n))+1):
		if i != n and n % i == 0:
			n = n / i
			i = i - 1
	print(n)


primeFactor(600851475143)
