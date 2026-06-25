import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------
# Analysis 1
# Churn Distribution
# -------------------

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

# -------------------
# Analysis 2
# Monthly Charges
# -------------------

print("\nAverage Monthly Charges:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# -------------------
# Analysis 3
# Contract Type
# -------------------

print("\nContract vs Churn:")
print(pd.crosstab(df["Contract"], df["Churn"]))

# -------------------
# Analysis 4
# Tenure
# -------------------

print("\nAverage Tenure:")
print(df.groupby("Churn")["tenure"].mean())

# -------------------
# Chart 1
# -------------------

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")

plt.savefig("charts/churn_distribution.png")

plt.show()