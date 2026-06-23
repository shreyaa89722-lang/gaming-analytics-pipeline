

import pandas as pd

# ── LOAD DATA ─────────────────────────
df = pd.read_csv("vgsales.csv")

# ── EXPLORE ───────────────────────────

# 1. See all columns clearly
print("=" * 50)
print("COLUMNS IN DATASET:")
print("=" * 50)
for col in df.columns:
    print(f"  → {col}")

# 2. See shape
print(f"\nTotal Games  : {len(df)}")
print(f"Total Columns: {len(df.columns)}")

# 3. See first 5 rows properly
print("\n" + "=" * 50)
print("FIRST 5 ROWS:")
print("=" * 50)
print(df.head().to_string())

# 4. See data types
print("\n" + "=" * 50)
print("DATA TYPES:")
print("=" * 50)
print(df.dtypes)

# 5. Check missing values
print("\n" + "=" * 50)
print("MISSING VALUES:")
print("=" * 50)
print(df.isnull().sum())

# 6. Basic stats
print("\n" + "=" * 50)
print("BASIC STATS:")
print("=" * 50)
print(df.describe())