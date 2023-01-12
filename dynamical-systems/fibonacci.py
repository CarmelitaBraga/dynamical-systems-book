def fibonacci(n):
    fibonacciList = []
    a, b = 0, 1
    fibonacciList.append(a)
    fibonacciList.append(b)
    for _ in range(n - 2):
        a, b = b, a + b
        fibonacciList.append(b)
    return fibonacciList