import numpy
import seaborn as sns
import matplotlib.pyplot as plt
d=numpy.random.normal(0.2,0.5,1000)
sns.histplot(numpy.exp(d),kde=True)
plt.show()
