from openpyxl import Workbook
import pandas as pd

# Create a new Excel file and add a worksheet
wb = Workbook()
sheet = wb.active
sheet.title = 'Test Data'

# Write headers to cells A1 and B1
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'

# Save the Excel file
excel_path = 'new_excel_text.xlsx'
wb.save(excel_path)

# Read the data from the specified sheet
df = pd.read_excel(excel_path, sheet_name='Test Data')

# Print the DataFrame
print(df)
