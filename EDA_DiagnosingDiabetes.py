import codecademylib3	
import pandas as pd	
import numpy as np	
	
diabetes_data = pd.read_csv("diabetes.csv")	
print(diabetes_data.head(10))	
	
x = diabetes_data.Pregnancies.count()	
print(x)	
	
missing_data = diabetes_data.isnull().sum()	
print(missing_data)	
	
print(diabetes_data.describe())	
	
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)	
	
print(diabetes_data)	
	
missing_data = diabetes_data.isnull().sum()	
#print(missing_data)	
	
print(diabetes_data[diabetes_data.isnull().any(axis = 1)])	
	
print(diabetes_data.dtypes)	
	
print(diabetes_data.Outcome.unique())	