import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_csv("./kc_house_data.csv")
df = df.drop(labels = ["id", "floors", "zipcode"], axis = 1)
plt.scatter(df["price"], df["sqft_living"], color="black")
print("\n")
print("**PLESE QUIT THE PLOT SCREEN TO PROCEED**")
time.sleep(1)
plt.show()


def enumeratingColumn(col):
	global df
	counter = 0
	for i in df[col]:
		counter += 1
	return counter

def meanCalc(col, length):
	global df
	_sum = 0
	for i in df[col]:
		_sum += i

	return _sum / length

def sigma(x, y):
	global df
	s = 0
	for i in range(enumeratingColumn(x)):
		s += df[x] * df[y]

	return s

def covar(x, y):
	lenX = enumeratingColumn(x)
	lenY = enumeratingColumn(y)
	mean_x = meanCalc(x, lenX)
	mean_y = meanCalc(y, lenY)
	temp = []

	for i in range(len(df[x])):
		temp.append((df[x] - mean_x) * (df[y] - mean_y))
	
	return sum(temp) / lenX

def corelation(x, y):
	covar = covar(x, y)
	p = (df[x].var()) * 0.5
	q = (df[y].var()) * 0.5
	
	return (covar / (p * q))

print("covariance: ", covar("price", "sqft_living"))
print(df.corr())

# QUESTION 2

cf = pd.read_csv("./Customer_Behaviour.csv")
cf = cf.drop(labels = ["User ID", "Age", "Purchased"], axis = 1)

def meanGender(x):
	col_gender = cf["Gender"]
	col_salary = cf["Salary"]
	s = 0
	l = 0
	for i in range(len(col_gender)):
		if col_gender[i] == x:
			s += col_salary[i]
			l += 1
	return s / l

def proportion(x):
	cf_gen = cf["Gender"]
	l = len(cf_gen)
	counter = 0

	for i in cf_gen:
		if i == x:
			counter += 1
	
	return counter / l

def sd(x):
	a = cf[x]
	return a.var() ** 0.5

meanM = meanGender("Male")
meanF = meanGender("Female")
print("\n\n")
print("question 2")
print("Mean of Males: ", meanM)
print("Mean of Females: ", meanF)

propM = proportion("Male")
propF = proportion("Female")
print("Male proportion: ", propM)
print("Female proportion: ", propF)

salary_sd = sd("Salary")
print("Standard deviation of salary: ", salary_sd)
k = meanM - meanF
g = k / salary_sd
an = propM * propF
ak = an ** 0.5
print("Point Biserial Correlation Value : ",g * ak)
