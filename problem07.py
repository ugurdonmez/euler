def prime_sieve(limit):
	not_prime= set()
	primes = []

	for i in range(2 , limit + 1):
		if i in not_prime:
			continue

		for f in range(i * 2 , limit + 1 , i):
			not_prime.add(f)

		primes.append(i)

	return primes

prime_list = prime_sieve(2000000)

print prime_list[10000]
