
#### If you want to check whether feature is guassian or normal distributed
#### Q-Q plot
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stat #pip install scipy
import pylab
# def plot_data(sample):
#     plt.figure(figsize=(10,6))
#     plt.subplot(1,2,1)
#     sns.histplot(sample)
#     plt.subplot(1,2,2)
#     stat.probplot(sample,dist='norm',plot=pylab)
#     plt.show()

# s=np.random.normal(0.5,0.2,1000)
# plot_data(s)   #agar yha graph straight line show krta h to yani k y normal distribution h



#### If you want to check whether feature is log normal or not
#### Q-Q plot
def plot_data(sample):
    plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    sns.histplot(sample)
    plt.subplot(1,2,2)
    stat.probplot(sample,dist='norm',plot=pylab)
    plt.show()

s=np.random.lognormal(0.5,0.2,1000)
plot_data(s)   #agar yha graph straight line show krta h to yani k y log_ normal distribution h


