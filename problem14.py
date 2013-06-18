list = {}

list[1] = 1
list[0] = 0


def find_squence_size(n,hash_table):
    key_value = hash_table.get(n)
    if key_value == None:
        if n % 2 == 0:
            size = 1 + find_squence_size(n / 2, hash_table)
            hash_table[n] = size
            return size
        else:
            size = 1 + find_squence_size(3 * n + 1, hash_table)
            hash_table[n] = size
            return size
    else:
        return key_value
        

max_size = 1
max_size_no = 1

for i in range (1,1000001):
    size = find_squence_size(i, list)
    if size > max_size:
        max_size_no = i
        max_size = size

print max_size_no