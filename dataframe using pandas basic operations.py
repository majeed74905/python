
import pandas as pd

# Program 11: Basic Pandas operations

# Series
s = pd.Series([10, 20, 30, 40, 50], name="Marks")
print("Series:\n", s)

# DataFrame
data = {'Name': ['Afzal', 'Rahul', 'Sara'],
        'Age': [20, 21, 22],
        'Marks': [85, 90, 95]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Selection
print("\nSelect Name column:\n", df['Name'])

# Filtering
print("\nStudents with Marks > 85:\n", df[df['Marks'] > 85])

# Adding data
df['Grade'] = ['A', 'A+', 'A+']

# Summary statistics
print("\nSummary Statistics:\n", df.describe())
