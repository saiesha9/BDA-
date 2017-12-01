import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x, m_y = np.mean(x), np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x - n*m_y*m_x)
	SS_xx = np.sum(x*x - n*m_x*m_x)

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return(b_0, b_1)
	

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	#sai=input("enter the value for production")
	#print (sai)	
	#jeev=b[0] +b[1]*x
	#print (jeev)
	#plt.plot(sai,jeev,color="g")


	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylabel('consumption')
	plt.xlabel('Generation')
	plt.legend()
	plt.title('prediction of Electricity Generation')
	plt.show()

def main():
	# observations
	csv_dset = pd.read_csv('linear.csv')
	df = pd.DataFrame(csv_dset)
	states =df.loc[:,"Union_Territory"]
	print(states)
	choice=input("Enter the State Name:")

	a1=df[df['Union_Territory']==choice].values
	# estimating coefficients
	x=['2008','2009','2010','2011','2012']
	line1=a1[0][1:5]
	line2=a1[0][5:9]

	b = estimate_coef(line1,line2)
	print("Estimated coefficients:\nb_0 = {} \\nb_1 = {}".format(b[0], b[1]))
	
	# plotting regression line
	plot_regression_line(line1,line2, b)
	

if __name__ == "__main__":
	main()
