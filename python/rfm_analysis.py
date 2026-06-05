import pandas as pd

transactions = pd.read_csv(
    "../data/cleaned/transactions_cleaned.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

snapshot_date = (
    transactions["transaction_date"].max()
    + pd.Timedelta(days=1)
)

rfm = transactions.groupby(
    "customer_id"
).agg({
    "transaction_date":
        lambda x: (snapshot_date - x.max()).days,

    "transaction_id": "count",

    "amount": "sum"
})

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

rfm.to_csv(
    "../outputs/rfm/rfm_table.csv"
)

print("RFM table created.")