import pandas as pd

# =====================================
# CUSTOMERS DATA CLEANING
# =====================================

customers = pd.read_csv("../data/raw/customers.csv")

customers = customers.dropna()

customers["gender"] = customers["gender"].str.upper()

customers = customers[customers["income"] > 10000]

customers["churn_flag"] = customers["churn_flag"].astype(bool)

customers.to_csv(
    "../data/cleaned/customers_cleaned.csv",
    index=False
)

# =====================================
# TRANSACTIONS DATA CLEANING
# =====================================

transactions = pd.read_csv(
    "../data/raw/transactions.csv"
)

transactions = transactions.dropna()

transactions = transactions[
    transactions["amount"] > 0
]

transactions.to_csv(
    "../data/cleaned/transactions_cleaned.csv",
    index=False
)

# =====================================
# CAMPAIGNS DATA CLEANING
# =====================================

campaigns = pd.read_csv(
    "../data/raw/campaigns.csv"
)

campaigns = campaigns.dropna()

campaigns = campaigns[
    campaigns["clicks"]
    <= campaigns["impressions"]
]

campaigns.to_csv(
    "../data/cleaned/campaigns_cleaned.csv",
    index=False
)

print("ETL completed successfully.")