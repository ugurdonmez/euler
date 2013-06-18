result = 2 ** 1000
string_result = str(result)
 
sum = 0
for number in string_result:
    sum = sum + int(number)
         
print sum 


#second
print sum([int(x) for x in str(2**1000)])