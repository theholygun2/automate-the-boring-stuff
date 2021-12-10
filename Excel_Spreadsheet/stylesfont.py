import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
# font keyword argument ex: Font(name=str, size=int,
#bold=bool, italic=bool)

# DEFAULT FONT STYLE FOR OPENPYXL = size = 11 style = calibri

italic24Font = Font(size=24, italic=True) # Create a Font
sheet['A1'].font = italic24Font # Apply the font to A1.
sheet['A1'] = 'Hello, world!''

fontObj1 = Font(name='Times New Roman', bold=true)
fontObj2 = Font(size=24, italic=true)

sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'

sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt italic'
# wb.save('styles.xlsx')
