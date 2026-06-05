import pandas as pd
from sqlalchemy import create_engine

# =====================================
# DATABASE CONNECTION
# =====================================

engine = create_engine(
    "postgresql://postgres:root123@localhost:5432/banking_project"
)

# =====================================
# LOAD CUSTOMERS
# =====================================

customers = pd.read_csv(
    "../data/cleaned/customers_cleaned.csv"
)

customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

# =====================================
# LOAD TRANSACTIONS
# =====================================

transactions = pd.read_csv(
    "../data/cleaned/transactions_cleaned.csv"
)

transactions.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False
)

# =====================================
# LOAD CAMPAIGNS
# =====================================

campaigns = pd.read_csv(
    "../data/cleaned/campaigns_cleaned.csv"
)

campaigns.to_sql(
    "campaigns",
    engine,
    if_exists="append",
    index=False
)

print("All data loaded successfully.")