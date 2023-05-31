# -*- coding: utf-8 -*-
"""fish trajectory plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNtAd5w0JpL0WUHga0VT8OoTKtAuH2Oo
"""

import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_csv('result_mf2.csv')
df1 = df1.drop('W1', axis=1)
df1 = df1.drop('H1',axis=1)
df1 = df1.drop('W2', axis=1)
df1 = df1.drop('H2', axis=1)

print(df1)

# swap columns X1 and X2
df1['X1'], df1['X2'] = df1['X2'], df1['X1']

# swap columns Y1 and Y2
df1['Y1'], df1['Y2'] = df1['Y2'], df1['Y1']

df1[['X1', 'Y1', 'X2', 'Y2']] = df1[['Y1', 'X1', 'Y2', 'X2']]

print(df1)

min_values = df1.min()
max_values = df1.max()
print(min_values,max_values)

df2 = pd.read_csv('For-Id.csv')
print(df2)

min_values = df2.min()
max_values = df2.max()
print(min_values,max_values)

xmin = 427.690
xmax = 980.09
ymin = 70.291
ymax = 618.55

# normalization

df1['X1'] = (df1['X1'] - df1['X1'].min()) / (df1['X1'].max() - df1['X1'].min()) * (xmax - xmin) + xmin
df1['X2'] = (df1['X2'] - df1['X2'].min()) / (df1['X2'].max() - df1['X2'].min()) * (xmax - xmin) + xmin
df1['Y1'] = (df1['Y1'] - df1['Y1'].min()) / (df1['Y1'].max() - df1['Y1'].min()) * (ymax - ymin) + ymin
df1['Y2'] = (df1['Y2'] - df1['Y2'].min()) / (df1['Y2'].max() - df1['Y2'].min()) * (ymax - ymin) + ymin

print(df2)

min_values = df2.min()
max_values = df2.max()
print(min_values,max_values)

print(df1)

# export the DataFrame to a CSV file
df1.to_csv('adjusted_results.csv', index=False)

# extract the x and y coordinates of fish 1 and fish 2 from code
x1_code = df1['X1']
y1_code = df1['Y1']
x2_code = df1['X2']
y2_code = df1['Y2']

# extract the x and y coordinates of fish 1 and fish 2 from tool
x1_tool = df2['X1']
y1_tool = df2['Y1']
x2_tool = df2['X2']
y2_tool = df2['Y2']

# plot the trajectories of fish 1 and fish 2
plt.plot(x1_code, y1_code, label='Fish 1(Code)')
plt.plot(x1_tool, y1_tool, label='Fish 1(Tool)')

# plot the trajectories of fish 1 and fish 2
plt.plot(x2_code, y2_code, label='Fish 2(Code)')
plt.plot(x2_tool, y2_tool, label='Fish 2(Tool)')

# add axis labels and legend
plt.xlabel('X position')
plt.ylabel('Y position')
plt.legend()

# show the plot
plt.show()