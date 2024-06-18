# creating data of normal distribution
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# s=np.random.normal(0.5,0.2,1000) #yani mean=0.5, std=0.2 and 1000 values create kro
# sns.histplot(s,kde=True)
# plt.show()


# creating data of log normal distribution
l_normal=np.random.lognormal(0.2,0.5,1000) #isi m natural log apply kr du to normal distribution mily ga
# sns.histplot(l_normal,kde=True) 
# plt.show()

sns.histplot(np.log(l_normal),kde=True)
plt.show()