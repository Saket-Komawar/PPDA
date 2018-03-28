from PIL import Image
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(sys.argv[1])
df1 = pd.read_csv(sys.argv[2])
df2 = pd.read_csv(sys.argv[3])

n = list(df[df.columns[0]])

N = 10
timeE = list(df[df.columns[1]])
timeN = list(df1[df1.columns[1]])
timeA = list(df2[df2.columns[1]])

fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.15
opacity = 0.8

rects1 = ax.bar(ind-width, timeE, width,alpha=opacity, color='r',label='Time to Encrypt Data')
rects2 = ax.bar(ind, timeN, width,alpha=opacity, color='g',label='Time to add Noise')
rects3 = ax.bar(ind+width, timeA, width,alpha=opacity, color='b',label='Time for Analysis')

plt.xlabel('Number of records used in Analysis')
plt.ylabel('Time in Seconds')
plt.xticks(ind, n)
plt.legend()


plt.tight_layout()
plt.show()
