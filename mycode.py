import pandas as pd
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan", "Onkar"],
    "Age": [21, 22, 20, 23, 21, 22],
    "Score": [85, 92, 78, 88, 95, 90]
}
# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
file_path = "data/data.csv"
df.to_csv(file_path, index=False)

print("CSV file created successfully!")
print(f"Location: {file_path}")
print("\nDataset:")
print(df)