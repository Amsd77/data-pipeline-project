import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting extract process")

customers = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/customers.csv')
products = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/products.csv')
orders = pd.read_csv('/mnt/c/Users/abhay/data-pipeline-project/data/orders.csv')

customers.to_csv('/tmp/customers.csv', index=False)
products.to_csv('/tmp/products.csv', index=False)
orders.to_csv('/tmp/orders.csv', index=False)

logging.info("Extract completed successfully")