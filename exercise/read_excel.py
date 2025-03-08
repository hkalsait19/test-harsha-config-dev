import pandas as pd

# Read the Excel file
df = pd.read_excel('project_scope.xlsx')

# Print Header
print("Header:")
print(df.columns.tolist())

# Print Key-Value Pairs
print("\nKey-Value Pairs:")
for index, row in df.iterrows():
    for col in df.columns:
        print(f"{col}: {row[col]}")
    
    # Check for specific condition
    if row['project'] == 'pqr' and 'learning-client' in df.columns and row['learning-client'] == 'learning-client':
        print("Learning project matched")