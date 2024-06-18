import numpy 
import matplotlib.pyplot as plt
# %matplotlib inline #%matplotlib inline is used because after this we don't have to write 
# # plt.show command to visualize the graph.

dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

histogram=(plt.hist(dataset))
# print(plt.show()) #histogram dekh kr bhi pta lag jata h k data m outlier h ya nhi

outlier=[]
def outlier_detector(data):
    threshold=3
    mean=numpy.mean(data)
    standard_dev=numpy.std(data)
    for i in data:
        z_score=(i-mean)/standard_dev
        if numpy.abs(z_score)>threshold:
            outlier.append(i)

outlier_detector(dataset)
print("the outliers are : ",outlier)


# 2nd way of removeing outlier is "IQR" technique that is more efficient

import seaborn as sns
dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
dataset.sort()
n=len(dataset)

Q1,Q3=numpy.percentile(dataset,[25,75]) #yani is dataset m s 25 and 75 ka percentile nikalo

IQR=Q3-Q1
lower_fence=Q1-(1.5 * IQR)
higher_fence=Q3+(1.5 * IQR)

print(Q1,Q3)
print(lower_fence,higher_fence)

outlier=[]
for i in dataset:
    if(i<lower_fence):
        outlier.append(i)
    if(i>higher_fence):
        outlier.append(i)

# print("outliers are = ",outlier)
sns.boxplot(data=dataset)


dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
outlier= [102, 107, 108]
for i in dataset:
    for j in outlier:
        if(i==j):
            dataset.remove(j)
print(dataset)