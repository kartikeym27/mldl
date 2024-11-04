import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import string

def generate_random_dataset(column_specs, num_rows=100):

    data = {}
    np.random.seed(42)

    for column, specs in column_specs.items():
        data_type = specs['type']
        
        if data_type == 'int':
            low, high = specs.get('range', (0, 100))
            data[column] = np.random.randint(low, high, num_rows)
        
        elif data_type == 'float':
            low, high = specs.get('range', (0.0, 1.0))
            data[column] = np.random.uniform(low, high, num_rows)
        
        elif data_type == 'category':
            categories = specs.get('categories', ['A', 'B', 'C'])
            data[column] = np.random.choice(categories, num_rows)
        
        elif data_type == 'date':
            start_date = specs.get('start', datetime(2000, 1, 1))
            end_date = specs.get('end', datetime.now())
            delta_days = (end_date - start_date).days
            data[column] = [start_date + timedelta(days=random.randint(0, delta_days)) for _ in range(num_rows)]
        
        elif data_type == 'bool':
            data[column] = np.random.choice([True, False], num_rows)
        
        elif data_type == 'string':
            length = specs.get('length', 5) 
            data[column] = [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(num_rows)]
        
        elif data_type == 'char':
            chars = specs.get('chars', string.ascii_letters)  
            data[column] = [random.choice(chars) for _ in range(num_rows)]
        
        else:
            raise ValueError(f"Unsupported data type '{data_type}' for column '{column}'")

    return pd.DataFrame(data)

column_specs = {
    "age": {"type": "int", "range": (18, 65)},
    "salary": {"type": "float", "range": (30000.0, 120000.0)},
    "city": {"type": "category", "categories": ["New York", "Los Angeles", "Chicago", "Houston"]},
    "date_joined": {"type": "date", "start": datetime(2010, 1, 1), "end": datetime.now()},
    "is_active": {"type": "bool"},
    "username": {"type": "string", "length": 8},
    "initial": {"type": "char", "chars": string.ascii_uppercase}
}

df = generate_random_dataset(column_specs, num_rows=100)

print(df.head())

df.to_csv("random_dataset.csv", index=False)
