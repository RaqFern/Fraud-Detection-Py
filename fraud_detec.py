# importing libs and dataset
import pandas as pd
import numpy as np
data = pd.read_csv("fraud_detection.csv")
print(data.head())

# null values? let's check
print(data.isnull().sum())

# This data does not have any null values, great! moving on...

# Exploring transaction type
print(data.type.value_counts())

