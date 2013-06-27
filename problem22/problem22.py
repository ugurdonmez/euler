list = open('names.txt').read()

names = list.split(',')

names.sort()

score = 0
order = 1

for name in names:
   for c in name:
      if c != '"':
	 score = score + order * (ord(c)-64)
   order = order + 1
   
print score