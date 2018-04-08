MAX = 100000
f = [0] * MAX
def fibonacci_calculation(n):
    if not isinstance(n, int):
        raise TypeError("Fibonacci sequence must be sliced with an int.")
    if n < 0:
        raise IndexError("Fibonacci sequence doesn't support negative slices")
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    if ((n & 1)):
        f[n] = (fibonacci_calculation(k) * fibonacci_calculation(k) + fibonacci_calculation(k - 1) * fibonacci_calculation(k - 1))
    else:
        f[n] = (2 * fibonacci_calculation(k - 1) + fibonacci_calculation(k)) * fibonacci_calculation(k)
    return f[n]
