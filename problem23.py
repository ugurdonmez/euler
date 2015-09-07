def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

abundant = []

for x in xrange(1,28123):
	
	s = sum(factors(x)) - x

	if s > x:
		abundant.append(x)


sums = []

print len(abundant)
print "sums"

for i in range(0, len(abundant)):
	for j in range(i, len(abundant)):
		n = abundant[i] + abundant[j]
		if n not in sums:
			sums.append(n)
		if n > 28124:
			break
	print i

total = 0
for i in xrange(1, 28123):
	if i not in sums:
		total = total + i

print total