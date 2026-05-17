# Import required libraries
import pandas as pd



# Load the dataset
data = pd.read_csv('customer_shopping_behavior.csv')

# Display basic information about the dataset
# print(data.head())
# print(data.describe())
# print(data.columns)
# print(data.isnull().sum())


# Handle Missing Values


# Replace null values in 'Review Rating' column with median value
data['Review Rating'] = data['Review Rating'].fillna(
    data['Review Rating'].median()
)


# Clean Column Names


# Convert column names to lowercase
# Replace spaces with underscores
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Rename column for better readability
data.rename(
    columns={'purchase_amount_(usd)': 'purchase_amount_usd'},
    inplace=True
)
# print(data.columns)


# Create age_group Column


# Create labels for age categories
labels = ["Young", "Adult", "Mid_Aged", "Senior"]

# Divide age into 4 equal groups
data['age_group'] = pd.qcut(
    data['age'],
    q=4,
    labels=labels
)
# print(data['age_group'].head(10))

# Create purchase_frequency_days Column


# Mapping text values to number of days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90,
}

# Create new column with integer values
data['purchase_frequency_days'] = (
    data['frequency_of_purchases']
    .map(frequency_mapping)
    .astype(int)
)

# print(data['purchase_frequency_days'].head(10))


# Check Duplicate Information


# Check if 'discount_applied' and 'promo_code_used'
# columns contain same values
print(
    (data['discount_applied'] == data['promo_code_used']).all()
)


# Remove Unnecessary Column


# Drop 'promo_code_used' column
data.drop(columns=['promo_code_used'], inplace=True)

# print(data.columns)

# Save Cleaned Data into New CSV File

data.to_csv(
    'customer_shopping_cleaned.csv',
    index=False
)

print(
    "Data cleaned and stored successfully "
    "in customer_shopping_cleaned.csv"
)


# Store Cleaned Data into MySQL Database


from sqlalchemy import create_engine

# Create MySQL connection
engine = create_engine(
    "mysql+pymysql://root:server@localhost/customer_behaviour"
)

# Store dataframe into MySQL table
data.to_sql(
    name='customer_shopping_cleaned',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data stored successfully in MySQL")