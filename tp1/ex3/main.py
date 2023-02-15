import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = np.array([19.41, 16.69, 17.71, 18.15, 21.07, 20.54, 19.52, 18.49, 18.69, 18.88,
                 19.59, 15.10, 20.21, 20.14, 20.14, 21.92, 22.64, 21.20, 17.16, 19.75])
#I have used the Q-Q plot
stats.probplot(x, dist="norm", plot=plt)
plt.title("Normal Q-Q plot")
plt.show()

sample_mean=np.mean(x)
sample_std=np.std(x)

t = stats.t.ppf(0.95, df=19)
margin_error=(t*sample_std)/np.sqrt(19)
print("95% Confidence Interval: [{:.3f}, {:.3f}]".format(sample_mean - margin_error, sample_mean + margin_error))
