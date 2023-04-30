import numpy as np
import matplotlib.pyplot as plt
x=np.random.uniform(size=(100,100))
#normalization of the first column xi
x0=[x[i][0] for i in range(100)]
s0=(x0-np.mean(x))/np.std(x)
plt.hist(s0, bins=20)
plt.ylabel('Frequency')
plt.title("one column")
plt.show()
#visualization of the central theorem
columns_average=np.mean(x,axis=0)
plt.hist(columns_average, bins=20)
plt.xlabel('sample means')
plt.ylabel('Frequency')
plt.title("visualization of the central theorem")
plt.show()
#visualization of the central theorem with normalization
columns_average=np.mean(x,axis=0)
l=(columns_average-np.mean(x))/np.std(x)
plt.hist(l, bins=20)
plt.xlabel('sample means')
plt.ylabel('Frequency')
plt.title("visualization of the central theorem with normalization ")
plt.show()
