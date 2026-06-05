import pandas as pd

# LOADING DATA

customers = pd.read_csv(
    "../data/cleaned/customers_cleaned.csv"
)

transactions = pd.read_csv(
    "../data/cleaned/transactions_cleaned.csv"
)

campaigns = pd.read_csv(
    "../data/cleaned/campaigns_cleaned.csv"
)

# TOTAL CUSTOMERS

total_customers = customers["customer_id"].nunique()

print("\nTotal Customers:")
print(total_customers)

# CHURN RATE

churn_rate = (
    customers["churn_flag"].mean()
) * 100

print("\nChurn Rate:")
print(round(churn_rate, 2), "%")

# TOTAL TRANSACTION AMOUNT

total_revenue = transactions["amount"].sum()

print("\nTotal Revenue:")
print(round(total_revenue, 2))

# TOP 5 CUSTOMERS BY SPENDING

top_customers = (
    transactions
    .groupby("customer_id")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Customers:")
print(top_customers)


# CAMPAIGN CTR

ctr = (
    campaigns["clicks"].sum()
    /
    campaigns["impressions"].sum()
) * 100

print("\nCampaign CTR:")
print(round(ctr, 2), "%")

# CONVERSION RATE

conversion_rate = (
    campaigns["conversions"].sum()
    /
    campaigns["clicks"].sum()
) * 100

print("\nConversion Rate:")
print(round(conversion_rate, 2), "%")