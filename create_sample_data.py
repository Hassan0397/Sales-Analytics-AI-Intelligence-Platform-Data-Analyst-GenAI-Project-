import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Generate sample sales data
np.random.seed(42)
dates = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(365)]
products = [f'P{str(i).zfill(3)}' for i in range(1, 21)]
regions = ['North', 'South', 'East', 'West']

sales_data = []
for date in dates:
    for _ in range(np.random.randint(5, 20)):
        product = np.random.choice(products)
        quantity = np.random.randint(1, 10)
        price = np.random.uniform(10, 100)
        total_sale = quantity * price
        region = np.random.choice(regions)
        
        sales_data.append({
            'date_parsed': date,
            'product_id': product,
            'quantity': quantity,
            'price': round(price, 2),
            'total_sale': round(total_sale, 2),
            'region': region
        })

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('data/sales_cleaned.csv', index=False)

# Generate sample inventory data
inventory_data = []
for product in products:
    inventory_data.append({
        'product_id': product,
        'current_stock': np.random.randint(0, 100),
        'restock_threshold': 20,
        'last_restock_parsed': datetime(2024, 1, 1) - timedelta(days=np.random.randint(1, 30))
    })

inventory_df = pd.DataFrame(inventory_data)
inventory_df.to_csv('data/inventory_cleaned.csv', index=False)

print("✅ Sample data created successfully!")
print(f"📊 Sales data: {len(sales_df)} rows")
print(f"📦 Inventory data: {len(inventory_df)} rows")
print("📁 Files saved in 'data/' directory")