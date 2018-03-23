from PIL import Image
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(sys.argv[1])

n = list(df[df.columns[0]])
time = list(df[df.columns[1]])

plt.plot(n, time)
plt.xlabel('n')
# naming the y axis
plt.ylabel('time')
 
# giving a title to my graph
plt.title('No.-Time Graph')
 
# function to show the plot
plt.show()

