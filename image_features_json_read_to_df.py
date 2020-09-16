import pandas as pd
import json
import openpyxl

#df = pd.read_json('image_feature_json.json') did not work

#df = pd.read_json('image_feature_json.json', lines=True) did not work

#df = read_json(r'C:/Users/jisernhagen/PycharmProjects/PythonProgrammingZelle/image_feature_json.json', orient='split')

#df = read_json(r'C:/Users/jisernhagen/PycharmProjects/PythonProgrammingZelle/data.json') example functional

with open('image_feature_json.json') as f:
    json_data = json.load(f)  #not sure what this is doing

#df = pd.DataFrame.from_dict(data, orient='index') error:  data has not been defined before this

#df = pd.DataFrame.from_dict(json_data, orient='index') #error: list object has no attibute "items"

#df = pd.DataFrame.from_dict(json_data) #error:  arrays must all be same length

json_data.keys()
df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in json_data.items() ]))
#print(df)

print(json_data.keys())

#print(df.head()) prints first five lines of boundingPoly

#df.to_excel('test.xlsx', index=False) #df.to_excel('test.xlsx', index=False)

#for i in json_data.keys():
#    df=pd.DataFrame.from_dict(json_data.get(i))

#for i in json_data.keys():
#    df=pd.DataFrame.from_dict(json_data.get(i), orient='index') # error:  list object has no attribute "values"

#for i in json_data.keys():
#    d = json_data.get(i)
#    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
#    df.to_excel('test_{}.xlsx'.format(str(i)), index=False)  #error:  'list' object has no attribute 'items'

#for i in json_data.keys():
#    d = json_data.get(i)
#    try:
#        df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
#    except:
#        df = pd.Dataframe(d)
#    df.to_excel('test_{}.xlsx'.format(str(i)), index=False) #attributeError:  module 'pandas' has no attribute 'Dataframe'

for i in json_data.keys():
    d = json_data.get(i)
    try:
        df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
    except:
        df = pd.DataFrame(d)
    df.to_excel('test_{}.xlsx'.format(str(i)), index=False)

