import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('dbip-city-lite-2023-02-WithHeader.csv')

# Write the DataFrame to a Parquet file
df.to_parquet('dbip-city-lite-2023-02-WithHeader.parquet', compression='snappy')
