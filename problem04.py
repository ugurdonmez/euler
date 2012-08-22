#def palindrome():
#	for i in range(100,999):
#		for j in range(100,999):
#			number = i * j
#			print(number)
#
#
#def isPalindrome(n):
#	
#
#palindrome()

print max( x * y 
	for x in xrange(100,1000)
		for y in xrange(100,1000)
			if str(x*y) == str(x*y)[::-1])
