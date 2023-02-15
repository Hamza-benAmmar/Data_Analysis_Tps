import matplotlib.pyplot as plt
import numpy as np

#p=0.5
x1=np.random.binomial(n=1,p=1/2,size=1000)
example1=[1/(1+x)*sum(x1[:x+1]) for x in range(1000)]
#p=1/3
x2=np.random.binomial(n=1,p=1/3,size=1000)
example2=[1/(1+x)*sum(x2[:x+1]) for x in range(1000)]
#Data visualisation
plt.plot(range(1,1001),example1,label=f"p=1/2")
plt.plot(range(1,1001),example2,label=f"p=1/3")
plt.legend()
plt.show()