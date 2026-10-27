INSERT INTO customers (first_name, last_name, email, country, created_at) VALUES
('John', 'Smith', 'john@example.com', 'USA', '2024-01-15'),
('Marie', 'Dubois', 'marie@example.com', 'France', '2024-02-20'),
('Ahmed', 'Ali', 'ahmed@example.com', 'Egypt', '2024-03-10'),
('Sofia', 'Garcia', 'sofia@example.com', 'Spain', '2024-04-05'),
('Li', 'Wei', 'li@example.com', 'China', '2024-05-12');

INSERT INTO products (product_name, category, price, stock_quantity) VALUES
('Laptop Pro', 'Electronics', 1299.99, 50),
('Wireless Mouse', 'Electronics', 29.99, 200),
('Office Chair', 'Furniture', 299.49, 30),
('Desk Lamp', 'Furniture', 45.75, 80),
('Coffee Mug', 'Kitchen', 12.50, 150),
('Bluetooth Headphones', 'Electronics', 89.99, 75);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2026-09-15', 'completed'),
(2, '2026-09-20', 'completed'),
(3, '2026-10-05', 'completed'),
(4, '2026-10-10', 'completed'),
(5, '2026-09-28', 'completed');

INSERT INTO sales (order_id, product_id, quantity, unit_price, sale_date) VALUES
(1, 1, 1, 1299.99, '2026-09-15'),
(1, 2, 2, 29.99, '2026-09-15'),
(2, 3, 1, 299.49, '2026-09-20'),
(3, 4, 2, 45.75, '2026-10-05'),
(4, 1, 1, 1299.99, '2026-10-10'),
(5, 5, 3, 12.50, '2026-09-28'),
(5, 6, 1, 89.99, '2026-09-28');
