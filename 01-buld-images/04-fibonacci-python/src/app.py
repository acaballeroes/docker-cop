def fibonacci(n):
    a, b = 0, 1
    
    for i in range(1, n+1):
        a, b = b, a + b
        
        print(f"term {i} of the Fibonacci series es: {b}")
    return b

# Calcs the term of the series
n = 9
fibonacci(n)
