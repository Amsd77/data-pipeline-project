import pandas as pd
import psycopg2

# Load CSVs (use ABSOLUTE paths for Airflow)
customers = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/customers.csv')
products = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/products.csv')
orders = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/orders.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ecommerce",
    user="postgres",
    password="7113",
    host="172.25.32.1",
    port="5432"
)
 
cursor = conn.cursor()

# Insert customers
for _, row in customers.iterrows():
    cursor.execute("""
        INSERT INTO customers (customer_id, gender, device_type, login_type)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (customer_id) DO NOTHING;
    """, tuple(row))

# Clean products
products = products[['product_id', 'product_name', 'category']]

# Insert products
for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products (product_id, product_name, category)
        VALUES (%s, %s, %s)
        ON CONFLICT (product_id) DO NOTHING;
    """, tuple(row))

# Clean orders
orders = orders[['customer_id', 'product_id', 'quantity', 'sales',
                 'discount', 'profit', 'shipping_cost',
                 'order_date', 'priority', 'payment_method']]

orders['customer_id'] = orders['customer_id'].astype(str)
orders['product_id'] = orders['product_id'].astype(str)

orders['quantity'] = pd.to_numeric(orders['quantity'], errors='coerce')
orders = orders.dropna(subset=['quantity'])

# Insert orders
for _, row in orders.iterrows():
    cursor.execute("""
        INSERT INTO orders (customer_id, product_id, quantity, sales, discount, profit,
                            shipping_cost, order_date, priority, payment_method)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded successfully!")
