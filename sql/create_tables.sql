
-- CUSTOMERS TABLE

CREATE TABLE customers (

    customer_id SERIAL PRIMARY KEY,

    age INT CHECK (age >= 18 AND age <= 100),

    gender VARCHAR(10) NOT NULL,

    province VARCHAR(20) NOT NULL,

    income NUMERIC(12,2) CHECK (income >= 0),

    join_date DATE NOT NULL,

    churn_flag BOOLEAN DEFAULT FALSE
);


-- TRANSACTIONS TABLE

CREATE TABLE transactions (

    transaction_id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    amount NUMERIC(12,2) NOT NULL CHECK (amount > 0),

    transaction_type VARCHAR(20) NOT NULL,

    transaction_date DATE NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- CAMPAIGNS TABLE

CREATE TABLE campaigns (

    campaign_id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    impressions INT DEFAULT 0 CHECK (impressions >= 0),

    clicks INT DEFAULT 0 CHECK (clicks >= 0),

    conversions INT DEFAULT 0 CHECK (conversions >= 0),

    ad_spend NUMERIC(10,2) DEFAULT 0 CHECK (ad_spend >= 0),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);