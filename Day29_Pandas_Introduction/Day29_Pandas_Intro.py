# ============================================================
#  DAY 29 — Introduction to pandas
#  Topics: Series, DataFrame, Loading Excel, Exploration Methods
#  File: Day29_Pandas_Practice.xlsx  (3 sheets)
# ============================================================

import pandas as pd

# ─────────────────────────────────────────────
#  SECTION 1 — What is a Series?
# ─────────────────────────────────────────────
# A Series is a 1-D labeled array — like a single Excel column.

prices = pd.Series([2845.50, 3520.75, 1612.30, 1295.60, 7240.00],
                   index=["RELIANCE", "TCS", "HDFCBANK", "INFY", "BAJFINANCE"],
                   name="Current_Price")

print("=" * 55)
print("SECTION 1 — Series")
print("=" * 55)
print(prices)                       # Full Series
print("\nType :", type(prices))
print("dtype:", prices.dtype)       # Data type of values
print("Index:", prices.index.tolist())
print("Name :", prices.name)

# Accessing values — just like a dictionary
print("\nTCS price   :", prices["TCS"])
print("INFY price  :", prices["INFY"])

# Basic math on a Series — applies to EVERY element
print("\nPrices after 10% gain:\n", prices * 1.10)
print("\nMin  :", prices.min())
print("Max  :", prices.max())
print("Mean :", prices.mean())


# ─────────────────────────────────────────────
#  SECTION 2 — What is a DataFrame?
# ─────────────────────────────────────────────
# A DataFrame is a 2-D table — like an entire Excel sheet.
# It is a collection of Series sharing the same index.

data = {
    "Ticker"       : ["RELIANCE", "TCS", "HDFCBANK", "INFY", "BAJFINANCE"],
    "Sector"       : ["Energy", "IT", "Banking", "IT", "NBFC"],
    "Buy_Price"    : [2200.00, 3100.00, 1450.00, 1380.00, 6800.00],
    "Current_Price": [2845.50, 3520.75, 1612.30, 1295.60, 7240.00],
    "Shares"       : [50, 30, 80, 45, 25],
}

df_manual = pd.DataFrame(data)

print("\n" + "=" * 55)
print("SECTION 2 — Manual DataFrame")
print("=" * 55)
print(df_manual)
print("\nType:", type(df_manual))


# ─────────────────────────────────────────────
#  SECTION 3 — Loading Excel with pandas
# ─────────────────────────────────────────────

FILE = "Day29_Pandas_Practice.xlsx"

# Load one sheet by name
df_portfolio = pd.read_excel(FILE, sheet_name="Stock_Portfolio")
df_expenses  = pd.read_excel(FILE, sheet_name="Monthly_Expenses")
df_financials= pd.read_excel(FILE, sheet_name="Company_Financials")

# Load ALL sheets at once → returns a dictionary {sheet_name: DataFrame}
all_sheets = pd.read_excel(FILE, sheet_name=None)
print("\n" + "=" * 55)
print("SECTION 3 — Sheets in the file:", list(all_sheets.keys()))
print("=" * 55)


# ─────────────────────────────────────────────
#  SECTION 4 — Exploration Methods
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 4 — Exploring: Stock_Portfolio")
print("=" * 55)

# .head(n) — first n rows (default 5)
print("\n--- head(5) ---")
print(df_portfolio.head(5))

# .tail(n) — last n rows
print("\n--- tail(3) ---")
print(df_portfolio.tail(3))

# .shape — (rows, columns) tuple
print("\n--- shape ---")
rows, cols = df_portfolio.shape
print(f"Rows: {rows}  |  Columns: {cols}")

# .columns — column names as Index object
print("\n--- columns ---")
print(df_portfolio.columns.tolist())

# .dtypes — data type of every column
print("\n--- dtypes ---")
print(df_portfolio.dtypes)

# .info() — concise summary: non-null counts, dtypes, memory
print("\n--- info() ---")
df_portfolio.info()

# .describe() — statistics for numeric columns only
print("\n--- describe() ---")
print(df_portfolio.describe())

# .isnull().sum() — count missing values per column
print("\n--- Missing values ---")
print(df_portfolio.isnull().sum())


# ─────────────────────────────────────────────
#  SECTION 5 — Accessing Columns
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 5 — Selecting Columns")
print("=" * 55)

# Single column → returns a Series
tickers = df_portfolio["Ticker"]
print("Single column (Series):\n", tickers)
print("Type:", type(tickers))

# Multiple columns → returns a DataFrame
subset = df_portfolio[["Stock", "Sector", "Current_Price"]]
print("\nMultiple columns (DataFrame):\n", subset)


# ─────────────────────────────────────────────
#  SECTION 6 — Quick Analysis
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 6 — Quick Analysis on Financials Sheet")
print("=" * 55)

print("\nAll companies:", df_financials["Company"].unique().tolist())
print("FY covered   :", df_financials["FY"].unique().tolist())
print("\nMissing values per column:")
print(df_financials.isnull().sum())

print("\nRevenue stats (₹ Crore):")
print(df_financials["Revenue_Cr"].describe())

print("\n--- Expenses by Category (count) ---")
print(df_expenses["Category"].value_counts())

print("\n--- Expenses describe ---")
print(df_expenses[["Amount_INR", "Budget_INR", "Variance"]].describe())

print("\nDone — Day 29 Complete!")
