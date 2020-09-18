# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    
    if a > b:
        resto = a % b
        return gcd(b, resto)
    else:
        resto = b % a
        return gcd(a, resto)
        

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
