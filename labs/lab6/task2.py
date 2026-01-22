def calculate_profit(deposit, years):
    if deposit < 30000:
        return 0.0
    if years <= 3:
        base_rate = 0.03
    elif years <= 6:
        base_rate = 0.05
    else:
        base_rate = 0.02
    extra = min(deposit // 10000 * 0.003, 0.05 - base_rate)
    rate = min(base_rate + extra, 0.05)
    profit = deposit * ((1 + rate) ** years - 1)
    return round(profit, 2)

d = int(input())
y = int(input())
print(calculate_profit(d, y))