import pandas as pd
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting load process")

customers = pd.read_csv('/tmp/customers_clean.csv')
products = pd.read_csv('/tmp/products_clean.csv')
orders = pd.read_csv('/tmp/orders_clean.csv')

try:
    conn = psycopg2.connect(
        dbname="ecommerce",
        user="postgres",
        password="7113",
        host="172.25.32.1",
        port="5432"
    )

    cursor = conn.cursor()

    for _, row in customers.iterrows():
        cursor.execute("""
            INSERT INTO customers (customer_id, gender, device_type, login_type)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO NOTHING;
        """, tuple(row))

    products = products[['product_id', 'product_name', 'category']]

    for _, row in products.iterrows():
        cursor.execute("""
            INSERT INTO products (product_id, product_name, category)
            VALUES (%s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING;
        """, tuple(row))

    orders = orders[['customer_id', 'product_id', 'quantity', 'sales',
                     'discount', 'profit', 'shipping_cost',
                     'order_date', 'priority', 'payment_method']]

    for _, row in orders.iterrows():
        cursor.execute("""
            INSERT INTO orders (customer_id, product_id, quantity, sales, discount, profit,
                                shipping_cost, order_date, priority, payment_method)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    logging.info("Load completed successfully")

except Exception as e:
    logging.error(f"Error occurred: {e}")
    raise