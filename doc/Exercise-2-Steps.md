# Exercise-2: Read Excel Sheet Using Python

## Objective
Read the attached Excel sheet using Python and manage the output to print the header, key-value pairs, and a specific message when certain conditions are met.

## Technologies Used
- Python
- pandas
- openpyxl

## Steps

### Step 1: Install Required Packages
Install the necessary Python packages using pip:
```sh
pip install pandas openpyxl
```

### Step 2: Create Python Script to Generate the Excel File
Create a Python script named `create_project_scope.py` with the following content:
```python name=create_project_scope.py
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
```

Run the script to create the `project_scope.xlsx` file:
```sh
python create_project_scope.py
```

### Step 3: Create Python Script to Read the Excel File
Create a Python script named `read_excel.py` with the following content:
```python name=read_excel.py
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
```

### Step 4: Run the Script to Read the Excel File
Execute the script using the following command:
```sh
python read_excel.py
```

## Explanation

1. **Install Required Packages**:
   The first step is to install the necessary Python packages (`pandas` and `openpyxl`).

2. **Create Python Script to Generate the Excel File**:
   The script `create_project_scope.py` generates an Excel file named `project_scope.xlsx` with sample data.

3. **Create Python Script to Read the Excel File**:
   The script `read_excel.py` reads the `project_scope.xlsx` file, prints the header, key-value pairs, and checks for specific conditions to print custom messages.

4. **Run the Script**:
   The final step is to run the `read_excel.py` script to process the data and print the required output.

## Conclusion
By following these steps, you can read an Excel file using Python, print the header and key-value pairs, and check for specific conditions to print custom messages. This exercise demonstrates the ability to handle Excel files and process data efficiently using Python.