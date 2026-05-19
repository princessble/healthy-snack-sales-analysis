import pandas as pd

# Step 1: Load the sales data
data = pd.read_csv("data/healthy_snack_sales.csv")

# Step 2: Check the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Step 3: Check basic information about the dataset
print("\nDataset information:")
print(data.info())

# Step 4: Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Step 5: Create new columns for Revenue, Cost, and Profit
data["Revenue"] = data["Quantity"] * data["Unit_Price"]
data["Total_Cost"] = data["Quantity"] * data["Cost_Per_Unit"]
data["Profit"] = data["Revenue"] - data["Total_Cost"]

# Step 6: Convert Date column to proper date format
data["Date"] = pd.to_datetime(data["Date"])

# Step 7: Create a Month column
data["Month"] = data["Date"].dt.strftime("%B")

# Step 8: Save the cleaned data
data.to_csv("outputs/cleaned_sales_data.csv", index=False)

print("\nData cleaning completed successfully.")
print("Cleaned data saved in the outputs folder.")
