import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# ---------------------------
# CUSTOMERS DATA
# ---------------------------

customers = []

for i in range(1, 1001):

    customers.append({
        "customer_id": i,
        "age": random.randint(18, 70),
        "gender": random.choice(["M", "F"]),
        "province": random.choice(["ON", "BC", "QC", "AB"]),
        "income": random.randint(30000, 120000),
        "join_date": fake.date_between(start_date='-3y', end_date='today'),
        "churn_flag": random.choice([0, 1])
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "../data/raw/customers.csv",
    index=False
)

# ---------------------------
# TRANSACTIONS DATA
# ---------------------------

transactions = []

for i in range(1, 5001):

    transactions.append({
        "transaction_id": i,
        "customer_id": random.randint(1, 1000),
        "amount": round(random.uniform(10, 5000), 2),
        "transaction_type": random.choice(["Debit", "Credit"]),
        "transaction_date": fake.date_between(start_date='-2y', end_date='today')
    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "../data/raw/transactions.csv",
    index=False
)

# ---------------------------
# CAMPAIGNS DATA
# ---------------------------

campaigns = []

for i in range(1, 1001):

    impressions = random.randint(100, 10000)
    clicks = random.randint(10, impressions)

    campaigns.append({
        "campaign_id": i,
        "customer_id": random.randint(1, 1000),
        "impressions": impressions,
        "clicks": clicks,
        "conversions": random.randint(1, clicks),
        "ad_spend": round(random.uniform(50, 1000), 2)
    })

campaigns_df = pd.DataFrame(campaigns)

campaigns_df.to_csv(
    "../data/raw/campaigns.csv",
    index=False
)

print("All datasets created successfully.")