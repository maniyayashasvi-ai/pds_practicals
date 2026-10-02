import pandas as pd
import numpy as np
df=pd.read_csv("employee.csv")
income=df["MonthlyIncome"]
print(df["MonthlyIncome"].describe())
import matplotlib.pyplot as plt
plt.hist(df["MonthlyIncome"],bins=10)
plt.xlabel("Monthlyincome")
plt.ylabel("Number of employees")
plt.title("Distribution of monthly income")
plt.show()
plt.scatter(df["TotalWorkingYears"],df["MonthlyIncome"])
plt.xlabel("Total Working years")
plt.ylabel("Monthly Income")
plt.title("Total Working years vs Monthly Income")
plt.show()
correlation = df["TotalWorkingYears"].corr(df["MonthlyIncome"])
print("correlation= ",correlation)
vars=["MonthlyIncome","TotalWorkingYears","YearsAtCompany","JobSatisfaction"]
correlation_matrix=df[vars].corr()
print(correlation_matrix.round(2))
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation matrix of emmployee variables")
plt.show()