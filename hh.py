


import json

# text ={"h":"value somthing"}
# json_text =json.dumps(text)
# f  =open('xyz.txt','w')
# f.write(json_text)
# f.close()

f  =open('xyz.txt','r')
data =f.read()
data1 = json.loads(data)
print(data1,type(data1))
print(data1['h'])




