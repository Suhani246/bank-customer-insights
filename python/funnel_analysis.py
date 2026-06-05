import pandas as pd

campaigns = pd.read_csv(
    "../data/cleaned/campaigns_cleaned.csv"
)

impressions = campaigns["impressions"].sum()
clicks = campaigns["clicks"].sum()
conversions = campaigns["conversions"].sum()

print("Impressions:", impressions)
print("Clicks:", clicks)
print("Conversions:", conversions)

print(
    "CTR:",
    round(
        clicks/impressions*100,
        2
    )
)

print(
    "Conversion Rate:",
    round(
        conversions/clicks*100,
        2
    )
)