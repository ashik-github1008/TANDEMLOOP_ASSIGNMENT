def generate_custom_odd_series(a: int):
    count = a if a % 2 != 0 else a - 1  
    result = [2 * i + 1 for i in range(count)]
    return result

a = int(input("Enter a number: "))
output = generate_custom_odd_series(a)
print("Output:", ', '.join(map(str, output)))
