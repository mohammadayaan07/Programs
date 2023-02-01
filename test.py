
import json
# JSON string
employee = '  {"id":"09", "name": "Rossum", "department":"IT"}  '
# Convert JSON string to Python dict
print("Type employee=",type(employee))
ed = json.loads(employee)
print(ed,type(ed))
for k,v in ed.items():
	print("{}-->{}".format(k,v))