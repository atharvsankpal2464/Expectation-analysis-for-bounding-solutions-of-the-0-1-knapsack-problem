# Function to solve 0/1 Knapsack Problem using Dynamic Programming
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
capacity = 5
max_value, dp_table = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)