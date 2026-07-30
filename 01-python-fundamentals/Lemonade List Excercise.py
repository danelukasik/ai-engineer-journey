sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
w2_input = int(input('Enter sales'))
sales_w2.append(w2_input)
profit = 1.5
sales_w1.extend(sales_w2)
sales = sales_w1
daily_profit = [x * profit for x in sales]
best_day = max(daily_profit)
worst_day = min(daily_profit)
print(sales)
print(best_day)
print(worst_day)
print(sum(daily_profit))