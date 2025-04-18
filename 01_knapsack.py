def greedy_knapsack(weights, profits, capacity):
    # Sort items by profit-to-weight ratio in decreasing order
    items = sorted(zip(weights, profits), key=lambda x: x[1]/x[0], reverse=True)
    
    total_weight = 0
    total_profit = 0

    for w, p in items:
        if total_weight + w <= capacity:
            total_weight += w
            total_profit += p
        else:
            break

    return total_profit

# Get user input
capacity = int(input("Enter the knapsack capacity: "))
num_items = int(input("Enter the number of items: "))

weights = []
profits = []

print("\nEnter weight and profit for each item:")
for i in range(num_items):
    w = int(input(f"Weight of item {i+1}: "))
    p = float(input(f"Profit of item {i+1}: "))
    weights.append(w)
    profits.append(p)

# Run the Greedy algorithm
greedy_profit = greedy_knapsack(weights, profits, capacity)

print(f"\nMaximum profit using Greedy approach: {greedy_profit}")
