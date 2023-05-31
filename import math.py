import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import random 
import csv
import pandas as pd

df = pd.read_csv('1.csv')
df1 = df.drop('X1', axis=1)
df1 = df.drop('Y1',axis=1)
df1 = df.drop('X2', axis=1)
df1 = df.drop('X2', axis=1)


df1['X1'] = df['X1']
df1['X2'] = df['X2']
df1['Y1'] = df['Y1']
df1['Y2'] = df['Y2']
print(df)
# with open('2.csv', 'w', encoding='UTF8',newline='') as f1:
#     header=["X1","Y1","W1","H1","X2","Y2","W2","H2"]
#     writer = csv.writer(f1)

#     writer.writerow(header) 
#     for i in range(df1.size):
#         if(i % random.randint(1,3) != 0):
#             df1['X1'] = df1(['X1']) + random.random()*0.1*random.randint(1,5)
#             df1['X2'] = df1(['X2']) + random.random()*0.1*random.randint(1,4)
#             df1['Y1'] = df1(['Y1'])  - random.random()*0.1*random.randint(1,6)
#             df1['Y2'] = df1(['Y2'])  + random.random()*0.01*random.randint(1, 5)
        
#         else:
#             df1['X1'] = df1(['X1']) 
#             df1['X2'] = df1(['X2'])  
#             df1['Y1'] = df1(['Y1'])  
#             df1['Y2'] = df1(['Y2'])  
#     df1.to_csv('2.csv', index=False)
# normalization

