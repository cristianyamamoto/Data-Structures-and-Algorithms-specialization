# python3
import sys


def compute_min_refills(distance, tank, stops):
    numRefills = 0
    currentRefill = 0 
    limit = tank
    n = len(stops)
    while limit < distance:
        if currentRefill >= n or stops[currentRefill] > limit:
            return -1
        while currentRefill < n-1 and stops[currentRefill+1] <= limit:
            currentRefill += 1
        numRefills += 1
        limit = stops[currentRefill] + tank
        currentRefill += 1

    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #print (d, m , stops)
    print(compute_min_refills(d, m, stops))
