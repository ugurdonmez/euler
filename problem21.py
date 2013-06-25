import math

list = {}

list[1] = 1
list[0] = 0

def isqrt(n):
   return int(math.floor(math.sqrt(float(n))))

def divisors(n):

   divs = []
   rdivs = []
   for divisor in range(1, isqrt(n)+1):
      if (n % divisor) == 0:
	 divs.append(divisor)
         rdivisor = n / divisor
         if rdivisor != divisor:
	    rdivs.append(rdivisor)
   rdivs.reverse()
   return_value = divs + rdivs
   return_value.remove(n)
   return return_value

def sum_of_proper_division(l):
   return reduce(lambda x, y : x + y , l)

counter = []

for n in range(1,10001):
   proper_div_sum = list.get(n)
   if proper_div_sum == None:
      proper_div_sum = sum_of_proper_division(divisors(n))
      list[n] = proper_div_sum
   rev_proper_div_sum = list.get(proper_div_sum)
   if rev_proper_div_sum == None:
      rev_proper_div_sum = sum_of_proper_division(divisors(proper_div_sum))
      list[proper_div_sum] = rev_proper_div_sum
   if rev_proper_div_sum == n and proper_div_sum != rev_proper_div_sum:
      counter.append(n)
   

print counter  
print reduce(lambda x,y : x + y ,counter)