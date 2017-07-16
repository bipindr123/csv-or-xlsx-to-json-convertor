import csv
import json
output=  {}

with open('test.csv') as csv_file:
   for row in csv.DictReader(csv_file):
       if(row['agent']!=""):
           boss = row['agent']
           output.update({ row['agent']:{ row['type']:{ "Jan-17":row['Jan-17'],"Feb-17":row['Feb-17'],"Mar-17":row['Mar-17'] } } })
       else:
           output[boss].update({ row['type']:{ "Jan-17":row['Jan-17'],"Feb-17":row['Feb-17'],"Mar-17":row['Mar-17'] } })

fp = open("god.json","w")
output_json = json.dump(output,fp)
print(output_json)
