# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    index = list(range(len(values)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(values, weights)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(values)
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity/weights[i]
            max_value += values[i]*capacity/weights[i]
            break
    #print (fractions[i])
    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
