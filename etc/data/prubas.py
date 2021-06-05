import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

df = pd.read_csv('./files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.reset_index()
df = df.loc[1,0]
print (df)
# df = df.loc[1,'0']
# print (df)
# df = df.reset_index()
# # df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
# # print (co)
# # df = pd.to_numeric(df[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34])
# # cols = df.columns.drop(5)
# df = df.drop(['index', 0, 1,2,3,5,6,7,8,9,10,11,12,13,14,15,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45], axis=1)
# cols = df.columns.drop(4)
# df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
# df = df.groupby([4]).agg(
#     {16:'sum',
#      17:'sum',
#      18:'sum',
#      19:'sum',
#      20:'sum',
#      21:'sum',
#      22:'sum',
#      23:'sum',
#      24:'sum',
#      25:'sum',
#      26:'sum',
#     }).reset_index()
# df = df.rename(columns={
#     4: 'CONGRESO',
#     16:'PAN',
#     17:'PRI',
#     18:'PRD',
#     19:'PT',
#     20:'PVEM',
#     21:'MC',
#     22:'MOR',
#     23:'PES',
#     24:'RSP',
#     25:'FM',
#     26:'PAN_PRI_PRD_a',
# })
# df = df.rename(index={0: 'I',1: 'II',2: 'III',3: 'IV',4: 'V',5: 'VI',6: 'VII',7: 'VIII',8: 'IX',9: 'X',10: 'XI',11: 'XII',12: 'XIII',13: 'XIV',14: 'XV',15: 'XVI',16: 'XVII',17: 'XVIII',18: 'XIX',19: 'XX',20: 'XXI'})
# rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
# df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
# df = df.drop(['CONGRESO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
# df = df.T
# # print (df)
# # df = df.T
# # print (df)
# # I = df['I']
# # # I = I.max()
# # print (I)
# # I = pd.DataFrame(df['I'], columns =['I'])
# # # I = df['I'].idxmax
# # II = pd.DataFrame(df['II'], columns =['III'])
# # III = pd.DataFrame(df['III'], columns =['III'])
# # IV = pd.DataFrame(df['IV'], columns =['IV'])
# # f = I.idxmax()
# # a = f.astype(str)
# # a = a.strip(["dtype: object"])

# # I = pd.DataFrame(df, columns =['I','II','III''IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI' ])
# # print (f)
# # df = len(set(df.index))
# # result = df.to_json(orient="index")
# # parsed = json.loads(result)
# # a = json.dumps(parsed, indent=4)
# # print (a)






# # df = df.drop(['CONGRESO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
# # df = df.T
# # # print (df)
# # # df = df.T

# # # I = df['I']
# # # # I = I.max()
# # # # print (I)
# # # I = pd.DataFrame(df['I'], columns =['I']).T
# # # # I = pd.DataFrame(df, columns =['I','II','III''IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI' ])
# # # print (I)
# # # df = len(set(df.index))
# # * result = df.to_json(orient="index")
# # * parsed = json.loads(result)
# # * a = json.dumps(parsed, indent=4)
# # * print (a)