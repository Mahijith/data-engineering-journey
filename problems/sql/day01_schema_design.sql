-- Day 1: Relational Schema Design
-- Order Management System

CREATE TABLE Customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(50) NOT NULL,
    email         VARCHAR(100) NOT NULL UNIQUE,
    signup_date   DATE
);

CREATE TABLE Products (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(150) NOT NULL,
    price         DECIMAL(10, 2) NOT NULL,
    category      VARCHAR(100)
);

CREATE TABLE Orders (
    order_id      INT PRIMARY KEY,
    customer_id   INT NOT NULL,
    order_date    DATE NOT NULL,
    amount        DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    order_id      INT NOT NULL,
    product_id    INT NOT NULL,
    quantity      INT NOT NULL,
    price         DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id)   REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
