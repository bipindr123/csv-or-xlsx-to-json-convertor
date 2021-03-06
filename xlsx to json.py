import xlrd
from collections import OrderedDict
import simplejson as json

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('myfile.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
output = {}
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
  row = sh.row_values(rownum)
  for i, x in enumerate(row):
    try:
      row[i] = int(x)
    except ValueError:
      pass

  if (row[0] != ""):
    boss = row[0]
    output.update(
      {row[0]: {row[1]: {"Jan-17": row[2], "Feb-17": row[3], "Mar-17": row[4]}}})
  else:
    output[boss].update({row[1]: {"Jan-17": row[2], "Feb-17": row[3], "Mar-17": row[4]}})

# Serialize the list of dicts to JSON
j = json.dumps(output)

# Write to file
with open('data.json', 'w') as f:
  f.write(j)
