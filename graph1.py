import sys
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

csv_dset = pd.read_csv('datasetELE.csv')
df = pd.DataFrame(csv_dset)
states =df.loc[:,"Union_Territory"]
print(states)
choice1=input("Enter the State Name:")
choice2=input("Enter the Year of interest:")

#print(df)
if(choice2=='2008'):
	a1=df[['Hydro_ 2008','Steam_ 2008','Diesel_Wind_2008','Gas_ 2008','Total_2008']][df['Union_Territory']==choice1].values
elif(choice2=='2009'):
	a1=df[['Hydro_ 2009','Steam_ 2009','Diesel_Wind_2009','Gas_ 2009','Total_2009']][df['Union_Territory']==choice1].values
elif(choice2=='2010'):
	a1=df[['Hydro_ 2010','Steam_ 2010','Diesel_Wind_2010','Gas_ 2010','Total_2010']][df['Union_Territory']==choice1].values	
elif(choice2=='2011'):
	a1=df[['Hydro_ 2011','Steam_ 2011','Diesel_Wind_2011','Gas_ 2011','Total_2011']][df['Union_Territory']==choice1].values
elif(choice2=='2012'):
	a1=df[['Hydro_ 2012','Steam_ 2012','Diesel_Wind_2012','Gas_ 2012','Total_2012']][df['Union_Territory']==choice1].values

objects=['hydro','steam','deisel_wind','gas','total']
ypos=np.arange(len(objects))
values=[a1[0][0],a1[0][1],a1[0][2],a1[0][3],a1[0][4]]
plt.bar(ypos,values)
plt.xticks(ypos,objects)
plt.ylabel('Production values')
plt.title('ELectricity Production')
plt.show()

