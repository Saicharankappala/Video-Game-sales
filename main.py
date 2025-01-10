from zipfile import ZipFile
import pandas as pd

# Load the data into a Pandas DataFrame
csv_file_path = f'/Users/saicharankappala/Downloads/vgsales.csv'
df = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe
print(df.head())# Get a concise summary of the dataframe
print(df.info())

# Generate descriptive statistics
print(df.describe())

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)
# Example: Handling missing values by dropping them
# df.dropna(inplace=True)

# Example: Removing duplicates
# df.drop_duplicates(inplace=True)
import matplotlib.pyplot as plt

# Assuming 'Name' is your Game name and 'Global_Sales' is your global sales data
plt.figure(figsize=(100, 6))
plt.plot(df['Name'], df['Global_Sales'], marker='o', linestyle='-')
plt.title('Game Sales')
plt.xlabel('Name')
plt.ylabel('Global_Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

