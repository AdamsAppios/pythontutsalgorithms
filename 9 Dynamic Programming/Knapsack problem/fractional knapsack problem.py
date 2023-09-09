def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    knapsack = []

    for weight, value in items:
        if capacity >= weight:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((capacity, fraction * value))
            total_value += fraction * value
            break

    return total_value, knapsack

# Example items (weight, value)
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50

max_value, selected_items = fractional_knapsack(items, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {selected_items}")
