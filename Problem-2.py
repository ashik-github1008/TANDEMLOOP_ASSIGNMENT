def generate_odd_series(a: int):
    result = []
    for i in range(a):
        result.append(2 * i + 1) 
    return result

a = int(input("Enter a number: "))
output = generate_odd_series(a)
print("Output:", ', '.join(map(str, output)))
