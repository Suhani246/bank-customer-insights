# Data Dictionary

## Customers Table

| Column Name | Data Type | Description |
|---|---|---|
| customer_id | SERIAL | Unique customer identifier |
| age | INT | Customer age |
| gender | VARCHAR | Customer gender |
| province | VARCHAR | Province of residence |
| income | NUMERIC | Annual income |
| join_date | DATE | Customer join date |
| churn_flag | BOOLEAN | Indicates whether customer churned |

---

## Transactions Table

| Column Name | Data Type | Description |
|---|---|---|
| transaction_id | SERIAL | Unique transaction identifier |
| customer_id | INT | Linked customer ID |
| amount | NUMERIC | Transaction amount |
| transaction_type | VARCHAR | Type of transaction |
| transaction_date | DATE | Date of transaction |

---

## Campaigns Table

| Column Name | Data Type | Description |
|---|---|---|
| campaign_id | SERIAL | Unique campaign identifier |
| customer_id | INT | Linked customer ID |
| impressions | INT | Ad impressions |
| clicks | INT | Total clicks |
| conversions | INT | Successful conversions |
| ad_spend | NUMERIC | Advertising spend |