def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(int(input('Enter a number: '))))

def fibonacci1(n):
    if n <= 1:
        return n
    else:
        return (fibonacci1(n-1) + fibonacci1(n-2))
    
print(fibonacci1(int(input('Enter a number: '))))