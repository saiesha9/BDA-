import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_dset = pd.read_csv('datasetELE.csv')
df = pd.DataFrame(csv_dset)
states =df.loc[:,"Union_Territory"]
print(states)
choice=input("Enter the State Name:")

a1=df[df['Union_Territory']==choice].values

x=['2008','2009','2010','2011','2012']
line1=a1[0][1:6]
line2=a1[0][6:11]
line3=a1[0][11:16]
line4=a1[0][16:21]

plt.plot(x,line1,label='hydro')
plt.plot(x,line2,label='steam')
plt.plot(x,line3,label='diesel_wind')
plt.plot(x,line4,label='gas')
#plt.xticks(x)
plt.ylabel('Production values')
plt.xlabel('Years')
plt.legend()
plt.title('Electricity Production of a State')

plt.show()
