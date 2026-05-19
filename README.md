# Healthy Snack Sales Analysis Using Python and SQL

## Project Overview

This project analyses sales data for a fictional healthy snack business called Derehoboth Healthy Snack Bar. The goal is to understand product performance, revenue, profit, customer behaviour, and location-based sales trends.

The project uses Python, pandas, SQL, SQLite, and data visualisation to turn raw sales data into useful business insights.

## Problem Statement

Derehoboth Healthy Snack Bar wants to understand which products are performing best, which locations generate the most revenue, and which customer types are most valuable. The business also wants to make data-driven decisions about production, marketing, and sales strategy.

## Project Structure

```text
healthy-snack-sales-analysis/
│
├── data/
│   └── healthy_snack_sales.csv
│
├── scripts/
│   ├── 01_clean_data.py
│   ├── 02_analyse_data.py
│   └── 03_sql_analysis.py
│
├── outputs/
│   ├── cleaned_sales_data.csv
│   ├── healthy_snack_sales.db
│   ├── revenue_by_product.png
│   └── sales_summary.txt
│
├── README.md
├── business_insights.md
└── requirements.txt
```

## Tools Used

- Python
- pandas
- matplotlib
- SQLite
- SQL
- Git
- GitHub
- VS Code

## Dataset

The dataset used in this project is a fictional sample dataset created for learning and portfolio purposes. It contains sales records for healthy snack products such as kale chips, sweet potato chips, beetroot chips, carrot chips, and peanut snacks.

## How to Run This Project

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Clean the data:

```bash
python scripts/01_clean_data.py
```

3. Run the Python sales analysis:

```bash
python scripts/02_analyse_data.py
```

4. Run the SQL analysis:

```bash
python scripts/03_sql_analysis.py
```

## Project Process

1. Created a sample healthy snack sales dataset.
2. Loaded the dataset using Python and pandas.
3. Checked for missing values.
4. Created new columns for revenue, total cost, and profit.
5. Analysed sales performance by product, location, month, and customer type.
6. Used SQL queries to answer business questions.
7. Created a simple chart showing revenue by product.
8. Wrote business recommendations based on the results.

## Key Questions Answered

- What is the total revenue?
- What is the total profit?
- Which product sold the most?
- Which product generated the highest revenue?
- Which product generated the highest profit?
- Which location performed best?
- Which customer type generated the most revenue?

## Key Insights

- Peanut Snack had the highest quantity sold.
- Kale Chips generated the highest revenue.
- Kale Chips also generated the highest profit.
- Dublin was the strongest sales location.
- Individual customers generated the highest revenue.

## Business Recommendations

Based on the analysis, the business should:

- Continue producing Peanut Snack because it had the highest quantity sold.
- Prioritise Kale Chips because it generated the highest revenue and profit.
- Focus more marketing efforts in Dublin because it was the strongest sales location.
- Create offers for individual customers because they generated the highest revenue.
- Track monthly sales regularly to understand customer demand and seasonal trends.

## What I Learned

Through this project, I practised:

- Cleaning data with Python.
- Analysing sales data with pandas.
- Writing SQL queries.
- Creating simple data visualisations.
- Turning data into business insights.
- Structuring a portfolio project for GitHub.

## Future Improvements

In the future, I would like to:

- Add a dashboard using Power BI, Tableau, or Streamlit.
- Use a larger dataset.
- Add customer feedback data.
- Predict future sales using machine learning.
