import pandas as pd
import numpy as np

# Create a sample student performance dataset matching the Kaggle dataset structure
np.random.seed(42)

data = {
    'gender': np.random.choice(['male', 'female'], 1000),
    'race/ethnicity': np.random.choice(['group A', 'group B', 'group C', 'group D', 'group E'], 1000),
    'parental level of education': np.random.choice(['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"], 1000),
    'lunch': np.random.choice(['standard', 'free/reduced'], 1000),
    'test preparation course': np.random.choice(['none', 'completed'], 1000),
    'math score': np.random.randint(0, 101, 1000),
    'reading score': np.random.randint(0, 101, 1000),
    'writing score': np.random.randint(0, 101, 1000),
}

df = pd.DataFrame(data)
df.to_csv('notebooks/data/stud.csv', index=False)
print(f"Created sample dataset with {len(df)} records")
print(f"\nDataset shape: {df.shape}")
print(f"\nColumn names: {list(df.columns)}")
print(f"\nFirst few rows:")
print(df.head())
