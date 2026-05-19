import pandas as pd
import sqlite3

# Step 1: Load cleaned CSV data
data = pd.read_csv("outputs/cleaned_sales_data.csv")

# Step 2: Connect to SQLite database
connection = sqlite3.connect("outputs/healthy_snack_sales.db")

# Step 3: Save the data into a SQL table
data.to_sql("sales", connection, if_exists="replace", index=False)

# Step 4: Create a cursor to run SQL queries
cursor = connection.cursor()

print("SQL ANALYSIS")
print("------------")

# Query 1: Total revenue and profit
query_1 = """
SELECT 
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales;
"""

print("\nTotal Revenue and Profit:")
print(pd.read_sql_query(query_1, connection))

# Query 2: Revenue by product
query_2 = """
SELECT 
    Product,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""

print("\nRevenue by Product:")
print(pd.read_sql_query(query_2, connection))

# Query 3: Profit by product
query_3 = """
SELECT 
    Product,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Product
ORDER BY Total_Profit DESC;
"""

print("\nProfit by Product:")
print(pd.read_sql_query(query_3, connection))

# Query 4: Revenue by location
query_4 = """
SELECT 
    Location,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales
GROUP BY Location
ORDER BY Total_Revenue DESC;
"""

print("\nRevenue by Location:")
print(pd.read_sql_query(query_4, connection))

# Query 5: Most popular customer type
query_5 = """
SELECT 
    Customer_Type,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales
GROUP BY Customer_Type
ORDER BY Total_Revenue DESC;
"""

print("\nCustomer Type Performance:")
print(pd.read_sql_query(query_5, connection))

# Step 5: Close database connection
connection.close()

print("\nSQL analysis completed successfully.")
