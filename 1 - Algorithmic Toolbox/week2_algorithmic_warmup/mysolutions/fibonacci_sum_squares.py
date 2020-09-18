# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum = 1
    for _ in range((n - 1) % 60):
        previous, current = current, (previous + current) % 10
        sum += current * current
  
    return sum % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
