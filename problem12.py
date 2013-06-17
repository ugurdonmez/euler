def factor_triangle_numbers():
    list = []
    counter = 2
    triangle_number = 1
    temp = triangle_number
    power_counter = 0
    while True:
        triangle_number = triangle_number + counter
        temp = triangle_number
        counter += 1
        list = []
        i = 2
        while i <= temp:
            power_counter = 0
            while temp % i == 0:
                temp = temp / i
                power_counter = power_counter + 1
            power_counter = power_counter + 1
            if power_counter > 1:
                list.append(power_counter)
            i = i + 1
        if len(list) > 0 and reduce(lambda x, y: x * y, list) >= 500:
            print triangle_number
            return

factor_triangle_numbers()

