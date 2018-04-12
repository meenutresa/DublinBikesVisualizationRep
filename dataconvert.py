import pandas as pd
import numpy as np
import datetime
import re
data_csv =  pd.read_csv('dataset.csv')
#print(data_csv)
data_csv = data_csv.dropna()
data_csv = data_csv.sort_values(by=['name'])

data_csv['last_update'] = data_csv['last_update'].astype(float)/1000.0
data_csv['DateTime'] =  data_csv['last_update'].apply(lambda x:datetime.datetime.fromtimestamp(x).strftime('%c'))
data_csv[['Lat','Long']] = pd.DataFrame((data_csv['position'].apply(lambda x:re.findall(r"[+-]?\d+(?:\.\d+)?",x))).tolist(),index= data_csv.index)
#print(pd.DataFrame((data_csv['position'].apply(lambda x:re.findall(r"[+-]?\d+(?:\.\d+)?",x))).tolist(),index= data_csv.index))
#print(data_csv)
data_csv['Lat'] = data_csv['Lat'].astype(float)
data_csv['Long'] = data_csv['Long'].astype(float)

del data_csv['banking']
del data_csv['bonus']

positionname_list = data_csv.name.unique()
print(len(positionname_list))
filename = "responseData1.js"
file1 = "datetimetext1.txt"
i=1
with open(filename,'w') as outfile:
    for pn in positionname_list:
        temp_df = data_csv.ix[(data_csv['name'] == pn)]
        temp_df = temp_df.sort_values(by=['last_update'])
        d = datetime.datetime(2017, 12, 5, 19, 00, 00)
        tt=0
        for index, row in temp_df.iterrows():
            d2 = d + datetime.timedelta(hours=tt)
            #temp_df.iloc[x]['DateTime'] = d2.isoformat(' ')
            temp_df.set_value(index,'DateTime',d2.isoformat(' '))
            #print(row['DateTime'])
            tt=tt+1
        temp_df_dict = temp_df.to_dict(orient='records')
        sent = "var sensor"+str(i)+"Data="
        sent = sent+str(temp_df_dict)+";"
        outfile.write(sent)
        i=i+1
    outfile.close()

with open(file1,'w') as outfile:
    for pn in positionname_list:
        temp_df = data_csv.ix[(data_csv['name'] == pn)]
        temp_df = temp_df.sort_values(by=['last_update'])
        outfile.write(str(temp_df['DateTime']))
        outfile.write('\n')

        #print(temp_df)
#print(temp_df_dict)
