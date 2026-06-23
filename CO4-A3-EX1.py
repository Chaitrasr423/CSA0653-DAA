# Investment Portfolio Optimization

investments = ['A', 'B', 'C', 'D']
capital = [20000, 30000, 40000, 50000]
returns = [25000, 40000, 50000, 70000]

budget = 80000

# ---------------- GREEDY APPROACH ----------------
data = list(zip(investments, capital, returns))

# Sort by Return/Capital ratio
data.sort(key=lambda x: x[2] / x[1], reverse=True)

greedy_selected = []
greedy_cost = 0
greedy_return = 0

for name, cost, ret in data:
    if greedy_cost + cost <= budget:
        greedy_selected.append(name)
        greedy_cost += cost
        greedy_return += ret

print("GREEDY APPROACH")
print("Selected Investments:", greedy_selected)
print("Total Return:", greedy_return)

# ---------------- DYNAMIC PROGRAMMING ----------------
n = len(capital)

dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(budget + 1):
        if capital[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                returns[i - 1] + dp[i - 1][w - capital[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

selected = []
w = budget

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(investments[i - 1])
        w -= capital[i - 1]

selected.reverse()

print("\nDYNAMIC PROGRAMMING")
print("Selected Investments:", selected)
print("Maximum Return:", dp[n][budget])
