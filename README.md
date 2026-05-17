# 🛍️ Customer Shopping Behavior Analysis

A full-stack data analytics project that uncovers insights from 3,900 retail transactions using Python, SQL, and Power BI.

---

## 📌 Project Overview

This project analyzes customer shopping behavior using transactional data across multiple product categories. The goal is to uncover actionable insights into spending patterns, customer segments, product preferences, and subscription behavior to support strategic business decisions.

---

## 📁 Project Structure

```
customer-shopping-behavior-analysis/
│
├── data/
│   ├── raw/                        # Original dataset
│   └── cleaned/                    # Cleaned and processed dataset
│
├── notebooks/
│   └── eda_analysis.ipynb          # Exploratory Data Analysis notebook
│
├── sql/
│   └── business_queries.sql        # All SQL queries used for analysis
│
├── dashboard/
│   └── customer_behavior.pbix      # Power BI dashboard file
│
└── README.md
```

---

## 📊 Dataset Summary

| Property        | Details                            |
|-----------------|------------------------------------|
| Total Records   | 3,900 transactions                 |
| Total Columns   | 18 features                        |
| Missing Data    | 37 values in `Review Rating`       |

### Key Features

- **Customer Demographics** — Age, Gender, Location, Subscription Status
- **Purchase Details** — Item Purchased, Category, Purchase Amount (USD), Season, Size, Color
- **Shopping Behavior** — Discount Applied, Promo Code Used, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type

---

## 🐍 Exploratory Data Analysis (Python)

Data preparation and cleaning was performed using **pandas** in Python.

### Steps Performed

1. **Data Loading** — Imported dataset using `pandas`
2. **Initial Exploration** — Used `df.info()` and `.describe()` for structure and summary statistics
3. **Missing Data Handling** — Imputed missing `Review Rating` values using the **median rating per product category**
4. **Column Standardization** — Renamed all columns to `snake_case` for consistency
5. **Feature Engineering**
   - Created `age_group` column by binning customer ages
   - Created `purchase_frequency_days` column from purchase data
6. **Data Consistency Check** — Verified redundancy between `discount_applied` and `promo_code_used`; dropped `promo_code_used`
7. **Database Integration** — Connected Python script to **PostgreSQL** and loaded the cleaned DataFrame for SQL analysis

---

## 🗄️ SQL Analysis (MySQL Workbench)

Structured analysis was performed in **MySQL Workbench** to answer 10 key business questions:

| # | Analysis | Key Finding |
|---|----------|-------------|
| 1 | **Revenue by Gender** | Male: $157,890 · Female: $75,191 |
| 2 | **High-Spending Discount Users** | 839 customers used discounts yet spent above average |
| 3 | **Top 5 Products by Rating** | Gloves (3.86), Sandals (3.84), Boots (3.82), Hat (3.80), Skirt (3.78) |
| 4 | **Shipping Type Comparison** | Express avg: $60.48 · Standard avg: $58.46 |
| 5 | **Subscribers vs. Non-Subscribers** | Avg spend nearly equal (~$59.49 vs $59.87); non-subscribers drive higher total revenue |
| 6 | **Discount-Dependent Products** | Hat (50%), Sneakers (49.66%), Coat (49.07%), Sweater (48.17%), Pants (47.37%) |
| 7 | **Customer Segmentation** | Loyal: 3,116 · Returning: 701 · New: 83 |
| 8 | **Top 3 Products per Category** | Jewelry, Blouse, Sandals, Jacket top their categories |
| 9 | **Repeat Buyers & Subscriptions** | Non-subscribers (2,518) outnumber subscribers (958) among repeat buyers |
| 10 | **Revenue by Age Group** | Young Adult: $62,143 · Middle-aged: $59,197 · Adult: $55,978 · Senior: $55,763 |

---

## 📈 Power BI Dashboard

An interactive dashboard was built in **Power BI** with the following KPIs and visuals:

- **KPI Cards** — Total Customers (3.9K), Average Purchase Amount ($59.76), Average Review Rating (3.75)
- **Donut Chart** — % of Customers by Subscription Status (Yes: 27% · No: 73%)
- **Bar Charts** — Revenue by Category, Sales by Category
- **Horizontal Bar Charts** — Revenue by Age Group, Sales by Age Group
- **Slicers/Filters** — Subscription Status, Gender, Category, Shipping Type

---

## 💡 Business Recommendations

1. **Boost Subscriptions** — Promote exclusive benefits to convert the 73% non-subscriber base; current avg spend is nearly equal, so incentives could tip the balance.
2. **Customer Loyalty Programs** — Reward repeat buyers to transition more customers from "Returning" to "Loyal" status.
3. **Review Discount Policy** — Products like Hat, Sneakers, and Coat have ~50% discount rates; balance promotion strategy with margin control.
4. **Product Positioning** — Highlight top-rated products (Gloves, Sandals, Boots) and best-selling items (Jewelry, Blouse) in marketing campaigns.
5. **Targeted Marketing** — Focus on Young Adults and Middle-aged groups, who contribute the highest revenue; also target express-shipping users who show higher average spend.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning & feature engineering |
| PostgreSQL | Data storage |
| MySQL Workbench | SQL-based business analysis |
| Power BI | Interactive dashboard & visualization |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas sqlalchemy psycopg2
```

### Run the EDA Notebook

```bash
jupyter notebook notebooks/eda_analysis.ipynb
```

### Load Data to PostgreSQL

Update the connection string in the notebook with your PostgreSQL credentials:

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql://username:password@localhost:5432/shopping_db")
df.to_sql("customer_shopping", engine, if_exists="replace", index=False)
```

### Run SQL Queries

Open `sql/business_queries.sql` in MySQL Workbench and execute the queries against your connected database.

---

## 📄 License

This project is for educational and analytical purposes.
