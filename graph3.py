import sys
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

csv_dset = pd.read_csv('datasetELE.csv')
df = pd.DataFrame(csv_dset)
#states =df.loc[:,"Union_Territory"]
#print(states)

choice2=input("Enter the Year of interest from 2008 - 2012 : ")

#print(df)
if(choice2=='2008'):
	a1=df['Hydro_ 2008'].max()
	a2=df['Steam_ 2008'].max()
	a3=df['Diesel_Wind_2008'].max()
	a4=df['Gas_ 2008'].max()
	a5=df['Total_2008'].max()
	a6=df[['Union_Territory']][df['Hydro_ 2008']==a1].values
	a7=df[['Union_Territory']][df['Steam_ 2008']==a2].values
	a8=df[['Union_Territory']][df['Diesel_Wind_2008']==a3].values
	a9=df[['Union_Territory']][df['Gas_ 2008']==a4].values
	a10=df[['Union_Territory']][df['Total_2008']==a5].values
	print (a1,a6,a2,a7,a3,a8,a4,a9,a5,a10)
    

elif(choice2=='2009'):
	a1=df['Hydro_ 2009'].max()
	a2=df['Steam_ 2009'].max()
	a3=df['Diesel_Wind_2009'].max()
	a4=df['Gas_ 2009'].max()
	a5=df['Total_2009'].max()
	a6=df[['Union_Territory']][df['Hydro_ 2009']==a1].values
	a7=df[['Union_Territory']][df['Steam_ 2009']==a2].values
	a8=df[['Union_Territory']][df['Diesel_Wind_2009']==a3].values
	a9=df[['Union_Territory']][df['Gas_ 2009']==a4].values
	a10=df[['Union_Territory']][df['Total_2009']==a5].values
	print (a1,a6,a2,a7,a3,a8,a4,a9,a5,a10)


	

elif(choice2=='2010'):
	a1=df['Hydro_ 2010'].max()
	a2=df['Steam_ 2010'].max()
	a3=df['Diesel_Wind_2010'].max()
	a4=df['Gas_ 2010'].max()
	a5=df['Total_2010'].max()
	a6=df[['Union_Territory']][df['Hydro_ 2010']==a1].values
	a7=df[['Union_Territory']][df['Steam_ 2010']==a2].values
	a8=df[['Union_Territory']][df['Diesel_Wind_2010']==a3].values
	a9=df[['Union_Territory']][df['Gas_ 2010']==a4].values
	a10=df[['Union_Territory']][df['Total_2010']==a5].values
	print (a1,a6,a2,a7,a3,a8,a4,a9,a5,a10)


	
elif(choice2=='2011'):
	a1=df['Hydro_ 2011'].max()
	a2=df['Steam_ 2011'].max()
	a3=df['Diesel_Wind_2011'].max()
	a4=df['Gas_ 2011'].max()
	a5=df['Total_2011'].max()
	a6=df[['Union_Territory']][df['Hydro_ 2011']==a1].values
	a7=df[['Union_Territory']][df['Steam_ 2011']==a2].values
	a8=df[['Union_Territory']][df['Diesel_Wind_2011']==a3].values
	a9=df[['Union_Territory']][df['Gas_ 2011']==a4].values
	a10=df[['Union_Territory']][df['Total_2011']==a5].values
	print (a1,a6,a2,a7,a3,a8,a4,a9,a5,a10)



	

elif(choice2=='2012'):
	a1=df['Hydro_ 2012'].max()
	a2=df['Steam_ 2012'].max()
	a3=df['Diesel_Wind_2012'].max()
	a4=df['Gas_ 2012'].max()
	a5=df['Total_2012'].max()
	a6=df[['Union_Territory']][df['Hydro_ 2012']==a1].values
	a7=df[['Union_Territory']][df['Steam_ 2012']==a2].values
	a8=df[['Union_Territory']][df['Diesel_Wind_2012']==a3].values
	a9=df[['Union_Territory']][df['Gas_ 2012']==a4].values
	a10=df[['Union_Territory']][df['Total_2012']==a5].values
	print (a1,a6,a2,a7,a3,a8,a4,a9,a5,a10)
	
objects=[a6,a7,a8,a9,a10]
ypos=np.arange(len(objects))
values=[a1,a2,a3,a4,a5]
mylist=plt.bar(ypos,values,align='center')
print (values)
x=['Hydro','steam','diesel','gas','total']
a=mylist[0].set_color('r') 
b=mylist[1].set_color('g') 
c=mylist[2].set_color('y') 
d=mylist[3].set_color('b') 
e=mylist[4].set_color('m') 
plt.xticks(ypos,objects)
plt.title('ELectricity Production')
plt.legend(mylist,x)
plt.show()






 










	

