-- Day 3: Star Schema Design
-- Retail Order Management Data Warehouse

CREATE TABLE dim_customer (
    customer_id   INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_city VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(100) NOT NULL,
    category      VARCHAR(100),
    unit_price    DECIMAL(10, 2) NOT NULL
);

CREATE TABLE dim_date (
    date_id       INT PRIMARY KEY,
    full_date     DATE NOT NULL,
    year          INT NOT NULL,
    month         INT NOT NULL,
    quarter       INT NOT NULL,
    day_of_week   VARCHAR(50)
);

CREATE TABLE fact_orders (
    order_id      INT PRIMARY KEY,
    customer_id   INT NOT NULL,
    product_id    INT NOT NULL,
    date_id       INT NOT NULL,
    quantity      INT NOT NULL,
    total_amount  DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id)  REFERENCES dim_product(product_id),
    FOREIGN KEY (date_id)     REFERENCES dim_date(date_id)
);

-- Star Schema Structure:
--         dim_customer
--              |
-- dim_date — fact_orders — dim_product
