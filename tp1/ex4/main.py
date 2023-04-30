import scipy.stats as stats
import numpy as  np
t1 = stats.t.ppf(0.95,df=99)
width=0.82-0.49
s=(width*np.sqrt(100))/(t1*2)
t2 = stats.t.ppf(0.99,df=99)
E=2*(t2*s/np.sqrt(100))
if(E>width):
  print("the width of the 99% confidence interval is larger than the width of the 95% confidence interval")
if(E<width):
  print("the width of the 99% confidence interval is larger than the width of the 95% confidence interval")
print("the width of 99% confidence interval is :{:.2f}".format(E))


