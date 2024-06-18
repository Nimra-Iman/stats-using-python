# variance, standard deviation
import statistics
import numpy
data=[23,14,32,45,12,67,45,32,56,32]
# print(statistics.stdev(data))
# print(statistics.variance(data)) # use formula of sample variance(yani divided by n-1)
print(statistics.pvariance(data)) # for population variance

# print(numpy.std(data))
print(numpy.var(data)) #population variance( yani divided by n),,, is liye statistics or numpy
# s calculate kiye huy variance m diffenece m

# manually calculate:
# variance=1/n-1(X__ - Xi)
data=[23,14,32,45,12,67,45,32,56,32]
mean=numpy.mean(data)
n=len(data)
sigma=0
for i in data:
    sigma=sigma+((i - mean)**2)
variance=sigma/(n-1)
print("actual sample variance is = ",statistics.variance(data))
print("Sample variance is = ", variance)
