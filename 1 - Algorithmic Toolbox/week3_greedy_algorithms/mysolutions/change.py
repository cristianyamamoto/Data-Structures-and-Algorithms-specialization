# Uses python3
import sys

def get_change(m):
    count = 0
    coins = [10, 5, 1]
    n = len(coins)
    ans = []
    for i in range(0, n):
        while(m >= coins[i]):
            m -= coins[i]
            ans.append(coins[i])
            count += 1
    
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
