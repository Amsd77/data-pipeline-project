import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting transform process")

customers = pd.read_csv('/tmp/customers.csv')
products = pd.read_csv('/tmp/products.csv')
orders = pd.read_csv('/tmp/orders.csv')

orders['customer_id'] = orders['customer_id'].astype(str)
orders['product_id'] = orders['product_id'].astype(str)
orders['quantity'] = pd.to_numeric(orders['quantity'], errors='coerce')
orders = orders.dropna(subset=['quantity'])

customers.to_csv('/tmp/customers_clean.csv', index=False)
products.to_csv('/tmp/products_clean.csv', index=False)
orders.to_csv('/tmp/orders_clean.csv', index=False)

logging.info("Transform completed successfully")