a = 0
for n in range(1000):
	if n % 3 == 0:
		a = a + n
	elif n % 5 == 0:
		a = a + n
print(a)
