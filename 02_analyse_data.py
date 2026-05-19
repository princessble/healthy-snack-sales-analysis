import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load cleaned data
data = pd.read_csv("outputs/cleaned_sales_data.csv")

# Step 2: Calculate total revenue and profit
total_revenue = data["Revenue"].sum()
total_profit = data["Profit"].sum()
total_quantity_sold = data["Quantity"].sum()

print("HEALTHY SNACK SALES ANALYSIS")
print("----------------------------")
print(f"Total Revenue: €{total_revenue:.2f}")
print(f"Total Profit: €{total_profit:.2f}")
print(f"Total Quantity Sold: {total_quantity_sold}")

# Step 3: Product with highest quantity sold
product_quantity = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nQuantity Sold by Product:")
print(product_quantity)

# Step 4: Revenue by product
product_revenue = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Product:")
print(product_revenue)

# Step 5: Profit by product
product_profit = data.groupby("Product")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Product:")
print(product_profit)

# Step 6: Revenue by location
location_revenue = data.groupby("Location")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Location:")
print(location_revenue)

# Step 7: Revenue by customer type
customer_revenue = data.groupby("Customer_Type")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Customer Type:")
print(customer_revenue)

# Step 8: Revenue by month
monthly_revenue = data.groupby("Month")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Month:")
print(monthly_revenue)

# Step 9: Save summary to a text file
with open("outputs/sales_summary.txt", "w") as file:
    file.write("HEALTHY SNACK SALES ANALYSIS\n")
    file.write("----------------------------\n")
    file.write(f"Total Revenue: €{total_revenue:.2f}\n")
    file.write(f"Total Profit: €{total_profit:.2f}\n")
    file.write(f"Total Quantity Sold: {total_quantity_sold}\n\n")

    file.write("Quantity Sold by Product:\n")
    file.write(product_quantity.to_string())
    file.write("\n\nRevenue by Product:\n")
    file.write(product_revenue.to_string())
    file.write("\n\nProfit by Product:\n")
    file.write(product_profit.to_string())
    file.write("\n\nRevenue by Location:\n")
    file.write(location_revenue.to_string())
    file.write("\n\nRevenue by Customer Type:\n")
    file.write(customer_revenue.to_string())
    file.write("\n\nRevenue by Month:\n")
    file.write(monthly_revenue.to_string())

print("\nAnalysis completed successfully.")
print("Sales summary saved in the outputs folder.")

# Step 10: Create a simple chart
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (€)")
plt.tight_layout()
plt.savefig("outputs/revenue_by_product.png")
plt.show()