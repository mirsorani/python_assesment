import pandas as pd

# Extracting and reading the original CSV file
file_path = 'games.csv'
data = pd.read_csv(file_path)

# Transform: Convert release_date column to datetime data type
data['release_date'] = pd.to_datetime(data['release_date'])

# Convert 'metascore' and 'userscore' columns to float, handling errors
data['metascore'] = pd.to_numeric(data['metascore'], errors='coerce')
data['userscore'] = pd.to_numeric(data['userscore'], errors='coerce')

# Handle any remaining non-convertible values (if any)
data['metascore'] = data['metascore'].astype(float)
data['userscore'] = data['userscore'].astype(float)

# Load the cleaned data to a new CSV file
cleaned_file_path = 'games_clean.csv'
data.to_csv(cleaned_file_path, index=False)
