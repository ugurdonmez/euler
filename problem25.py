'''

'''


fib = []

fib.append(0)
fib.append(1)

i = 2
while 1:
	f = fib[i-1] + fib[i-2]
	fib.append(f)
	if len(str(fib[i])) == 1000:
		print i
		break
	i = i + 1


