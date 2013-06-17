def factor_triangle_numbers():
    list = []
    counter = 1
    triangle_number = 2
    while True:
        triangle_number = triangle_number + counter
        counter += 1
        list = []
        for i in range (1, int(triangle_number / 2 + 1 ) ):
            if triangle_number % i == 0:
                list.append(i)
                if len(list) >= 500:
                    print triangle_number
                    return 

factor_triangle_numbers()