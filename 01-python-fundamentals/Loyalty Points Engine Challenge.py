# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [3.75,7.20,45.32,1.22,0.9,150]
def earn_points(price):
    points = (price // 1) * 3
    return points
def tier_label(points):
    if points < 100:
        tier = 'Bronze'
    elif points >= 100 and points < 500:
        tier = 'Silver'
    else:
        tier = 'Gold'
    return tier
total_points = 0
for purchase in purchases:
    total_points += earn_points(purchase)
tier = tier_label(total_points)

print('Loyalty Summary')
print(f'Total $ Spent: ${round(sum(purchases),2)}')
print(f'Total Points Earned: {total_points}')
print(f'Tier: {tier}')
print('Thank you for your loyalty!')