def count_multiples(input_list):
    result = {i: 0 for i in range(1, 10)}  

    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1

    return result

input_data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(input_data)
print("Output:", output)
