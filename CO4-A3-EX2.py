# Delivery Vehicle Loading

packages = ['P1', 'P2', 'P3', 'P4']
weights = [10, 20, 30, 25]
profits = [60, 100, 120, 110]
capacity = 50

# ---------------- GREEDY APPROACH ----------------
data = list(zip(packages, weights, profits))

# Sort by profit-to-weight ratio
data.sort(key=lambda x: x[2] / x[1], reverse=True)

greedy_packages = []
total_weight = 0
total_profit = 0

for p, w, pr in data:
    if total_weight + w <= capacity:
        greedy_packages.append(p)
        total_weight += w
        total_profit += pr

print("GREEDY APPROACH")
print("Selected Packages:", greedy_packages)
print("Total Profit:", total_profit)

# ---------------- DYNAMIC PROGRAMMING ----------------
n = len(weights)

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                profits[i - 1] + dp[i - 1][w - weights[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

selected = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(packages[i - 1])
        w -= weights[i - 1]

selected.reverse()

print("\nDYNAMIC PROGRAMMING")
print("Selected Packages:", selected)
print("Maximum Profit:", dp[n][capacity])
