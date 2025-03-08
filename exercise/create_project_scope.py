import pandas as pd

# Sample data for the Excel file
data = {
    'project': ['abc', 'def', 'ghi', 'pqr', 'stu'],
    'scope': ['scope1', 'scope2', 'scope3', 'scope4', 'scope5'],
    'learning-client': ['client1', 'client2', 'client3', 'learning-client', 'client5']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('project_scope.xlsx', index=False)

print("project_scope.xlsx file has been created.")