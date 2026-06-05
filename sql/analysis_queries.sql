
-- 1. TOTAL CUSTOMERS & CHURN RATE
-- How many customers do we have and how many churned?

SELECT
    COUNT(*) AS total_customers,

    COUNT(*) FILTER (
        WHERE churn_flag = TRUE
    ) AS churned_customers,

    ROUND(
        COUNT(*) FILTER (
            WHERE churn_flag = TRUE
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage

FROM customers;


-- 2. CUSTOMER SEGMENTATION BY INCOME
-- Which customer segments are most valuable?

SELECT
    customer_id,
    province,
    income,

    CASE
        WHEN income >= 100000 THEN 'High Income'
        WHEN income >= 60000 THEN 'Medium Income'
        ELSE 'Low Income'
    END AS customer_segment

FROM customers
ORDER BY income DESC;

-- 3. TOP 10 HIGHEST SPENDING CUSTOMERS
-- Who are the bank's highest value customers?


SELECT
    c.customer_id,
    c.province,
    c.income,

    ROUND(SUM(t.amount), 2) AS total_spending,

    RANK() OVER (
        ORDER BY SUM(t.amount) DESC
    ) AS spending_rank

FROM customers c

JOIN transactions t
ON c.customer_id = t.customer_id

GROUP BY
    c.customer_id,
    c.province,
    c.income

ORDER BY total_spending DESC
LIMIT 10;


-- 4. PROVINCE-WISE CUSTOMER PERFORMANCE
-- Which provinces generate the most revenue?

SELECT
    c.province,

    COUNT(DISTINCT c.customer_id)
        AS total_customers,

    ROUND(SUM(t.amount), 2)
        AS total_transaction_amount,

    ROUND(AVG(t.amount), 2)
        AS avg_transaction_amount

FROM customers c

JOIN transactions t
ON c.customer_id = t.customer_id

GROUP BY c.province

ORDER BY total_transaction_amount DESC;

-- 5. CUSTOMER TRANSACTION BEHAVIOR
-- How active are customers?

WITH customer_transactions AS (

    SELECT
        customer_id,
        COUNT(*) AS total_transactions,
        SUM(amount) AS total_amount

    FROM transactions

    GROUP BY customer_id
)

SELECT
    customer_id,
    total_transactions,

    ROUND(total_amount, 2) AS total_amount,

    DENSE_RANK() OVER (
        ORDER BY total_transactions DESC
    ) AS activity_rank

FROM customer_transactions

ORDER BY activity_rank
LIMIT 20;

-- 6. CAMPAIGN PERFORMANCE ANALYSIS
-- Which campaigns performed best?

SELECT
    campaign_id,

    impressions,
    clicks,
    conversions,
    ad_spend,

    ROUND(
        clicks * 100.0 / impressions,
        2
    ) AS ctr_percentage,

    ROUND(
        conversions * 100.0 / clicks,
        2
    ) AS conversion_rate_percentage,

    ROUND(
        ad_spend / conversions,
        2
    ) AS cost_per_conversion

FROM campaigns

ORDER BY conversion_rate_percentage DESC;

-- 7. HIGH-RISK CHURN CUSTOMERS
-- Which high-income customers are likely to churn?

SELECT
    customer_id,
    province,
    income,
    churn_flag

FROM customers

WHERE
    churn_flag = TRUE
    AND income >= 80000

ORDER BY income DESC;

-- 8. CUSTOMER LIFETIME VALUE (LTV)
-- What is the estimated value of each customer?

SELECT
    c.customer_id,

    c.province,

    ROUND(SUM(t.amount), 2)
        AS customer_lifetime_value,

    RANK() OVER (
        ORDER BY SUM(t.amount) DESC
    ) AS ltv_rank

FROM customers c

JOIN transactions t
ON c.customer_id = t.customer_id

GROUP BY
    c.customer_id,
    c.province

ORDER BY customer_lifetime_value DESC;

-- 9. PROVINCE CHURN ANALYSIS
-- Which provinces have highest churn?

SELECT
    province,

    COUNT(*) AS total_customers,

    COUNT(*) FILTER (
        WHERE churn_flag = TRUE
    ) AS churned_customers,

    ROUND(
        COUNT(*) FILTER (
            WHERE churn_flag = TRUE
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY province

ORDER BY churn_rate DESC;

-- 10. MONTHLY TRANSACTION TREND
-- Are transactions increasing over time?

SELECT
    DATE_TRUNC(
        'month',
        transaction_date
    ) AS transaction_month,

    ROUND(
        SUM(amount),
        2
    ) AS monthly_transaction_amount

FROM transactions

GROUP BY transaction_month

ORDER BY transaction_month;