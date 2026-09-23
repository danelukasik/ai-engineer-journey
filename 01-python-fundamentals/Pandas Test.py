import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "department": ["Sales", "Sales", "Engineering", "Engineering"],
    "revenue": [500, 700, 0, 0]
}
df = pd.DataFrame(data)

# 1. Print only the rows where department is "Sales"
sales = df[df["department"]=="Sales"]
print(sales)
# 2. Print the average revenue per department
avg_rev = df.groupby("department")["revenue"].mean()
print(avg_rev)
# 3. Add a new column "high_performer" that's True if revenue > 600
df = df.assign(high_performer=df["revenue"] > 600)
print(df)