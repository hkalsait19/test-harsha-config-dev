import pandas as pd

# Sample data for the Excel file
data = {
    'name': ['abc', 'xyz', 'pqr'],
    'domain': ['healthcare', 'automobile', 'learning'],
    'client': ['healthcare-client', 'automobile-client', 'learning-client'],
    'duration': ['Apr-25', 'May-25', 'Jun-25']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('project_scope.xlsx', index=False)

print("project_scope.xlsx file has been created.")

file_path = 'project_scope.xlsx'
df = pd.read_excel(file_path, header=0, engine='openpyxl')  # Use header=0 to use the first row as the header

# Step 2: Print the header
header = df.columns.tolist()
print("Header:", header)

# Step 3: Loop through the DataFrame and print key-value pairs
for index, row in df.iterrows():
    print("\nRow:", index + 1)
    for col in header:
        print(f"{col}: {row[col]}")
    
    # Step 4: Check if the client is in the format {domain}-client
    domain = row['domain']
    expected_client = f"{domain}-client"
    if row['client'] == expected_client:
        print(f"{domain.capitalize()} project matched")