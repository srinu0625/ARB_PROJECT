import pandas as pd

# Replace 'file_path.csv.gz' with the path to your compressed CSV file
file_path = r'C:\\Users\\srinu\\Downloads\\downloaded softwares\\TimeAndSalesGCcv1-20190101-20240426.csv'

# Use Pandas' read_csv function with the 'compression' parameter set to 'gzip'
data = pd.read_csv(file_path, compression='gzip')

# Now you can work with your data as a Pandas DataFrame
print(data.head())  # Display the first few rows of the DataFrame
