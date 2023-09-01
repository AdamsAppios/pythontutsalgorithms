def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    
    max_value = 0
    knapsack = [0] * n
    
    for ratio, i in ratios:
        if weights[i] <= capacity:
            knapsack[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            knapsack[i] = capacity / weights[i]
            max_value += values[i] * knapsack[i]
            break
    
    return max_value, knapsack

# Example items (values, weights)
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, knapsack = fractional_knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
print("Knapsack contents:", knapsack)