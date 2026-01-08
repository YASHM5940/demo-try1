#code to genrate a fibonacci series up to n terms . n is provided by user
#just demo program to see git and github functionality
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n_terms = int(input("Enter the number of terms for the Fibonacci series: "))
series = fibonacci_series(n_terms)
print(f"Fibonacci series up to {n_terms} terms: {series}")
