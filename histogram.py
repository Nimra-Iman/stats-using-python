import seaborn as sns
import matplotlib.pylab as plt
import math
# kde=kernal density estimator
data=[23,14,32,45,12,67,45,32,56,32]
# sns.histplot(data,kde=True)
# plt.show() #this will show log normal distribution


df=sns.load_dataset("iris")
print(df.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa
# PS C:\code_fun\python_stats> 

# sns.histplot(df["sepal_length"],kde=True)
# plt.show()

# sns.histplot(df["sepal_width"],kde=True)
# plt.show()

sns.histplot(df["petal_length"],kde=True)
plt.show()

# hm logo ko y bbhi check krna hota h k y given distribution normal distribution h bhi ya
# nhi, sirf graph dekh kr y nhi bta skty k distribution normal h
# or is cheeze ko check krny k liye hm q_q plot ko use krty hn
