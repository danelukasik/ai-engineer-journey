import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\danel\Desktop\ai-engineer-journey\Data Sets\Superstore sales dataset.csv")

# 1. Total sales and profit by Region
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()
print(f"Total sales and profit by Region:\n{region_summary.round(2)}\n")

# 2. Sales by Category, sorted highest to lowest
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(f"Sales by Category, sorted highest to lowest:\n{category_sales.round(2)}\n")

# 3. A quick chart
region_summary["Profit"].plot(kind="bar", title="Profit by Region")
print("Profit by Region chart displayed.\n")

# 4. Quantity Sold by Sub-Category, sorted highest to lowest
subcat_quantity = df.groupby("Sub-Category")["Quantity"].sum().sort_values(ascending=False)
print(f"Quantity Sold by Sub-Category, sorted highest to lowest:\n{subcat_quantity}\n")

# 5. A quick chart
subcat_quantity.plot(kind="bar", title="Quantity Sold by Sub-Category")
print("Quantity Sold by Sub-Category chart displayed.\n")

# 6. Average Sales and Profit by Segment
segment_summary = df.groupby("Segment")[["Sales", "Profit"]].mean()
print(f"Average Sales and Profit by Segment:\n{segment_summary.round(2)}\n")

# 7. Discounted Purchase % by Product Name, sorted Highest to Lowest
discounted_purchase = df[df["Discount"] > 0].groupby("Product Name")
print(f"Discounted Purchase % by Product Name, sorted Highest to Lowest:\n{discounted_purchase.size().sort_values(ascending=False) / df.groupby("Product Name").size() * 100}")