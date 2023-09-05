def knapsack_01_with_items(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected_items = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
                selected_items[i][w] = selected_items[i - 1][w]
            else:
                without_item = dp[i - 1][w]
                with_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                if with_item > without_item:
                    dp[i][w] = with_item
                    selected_items[i][w] = selected_items[i - 1][w - weights[i - 1]] + [i]
                else:
                    dp[i][w] = without_item
                    selected_items[i][w] = selected_items[i - 1][w]
    
    return dp[n][capacity], selected_items[n][capacity]

# Example items (values, weights)
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack_01_with_items(values, weights, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {selected_items}")