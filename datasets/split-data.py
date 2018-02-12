import numpy as np
import pandas as pd


n = 4

df = pd.read_csv("Employee_Payroll.csv")
#print df

df = df.drop('Fiscal Year', 1)
df = df.drop('Fiscal Period', 1)
df = df.drop('First Name', 1)
df = df.drop('Last Name', 1)
df = df.drop('Middle Init', 1)
df = df.drop('Office', 1)
df = df.drop('Office Name', 1)
df = df.drop('Job Code', 1)
df = df.drop('Job Title', 1)
df = df.drop('Position ID', 1)
df = df.drop('Employee Identifier', 1)
df = df.drop('Original Hire Date', 1)



bureau = list(df['Bureau'])
#bureau = [x.replace('.', 'Bureau of Human Resources') for x in bureau]
#print bureau
bur1 = list(set(bureau))
#for i in bur1:
#	print i

file = open('bureau-list.txt', 'w')
for item in bur1:
	print >> file, item
file.close()

bur2 = [bur1.index(x) for x in bureau]
df = df.drop('Bureau', 1)
df['Bureau'] = bur2


basepay = list(df['Base Pay'])
basepay = [x.lstrip('$') for x in basepay]
df = df.drop('Base Pay', 1)
df['Base Pay'] = basepay

l = len(df) - (len(df) % n)
df = df[: l]

led = l / n

df0 = df[ : led]
df1 = df[led : 2 * led]
df2 = df[2 * led : 3 * led]
df3 = df[3 * led :]

'''print df0
print df1
print df2
print df3'''

df0.to_csv("endpoint0.csv")
df1.to_csv("endpoint1.csv")
df2.to_csv("endpoint2.csv")
df3.to_csv("endpoint3.csv")
