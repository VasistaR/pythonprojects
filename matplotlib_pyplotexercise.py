#age vs time spent watching tv
import numpy as np
import matplotlib.pyplot as plt
xvalues = np.random.normal(234,12,100)
yvalues = np.random.normal(254,10,100)
plt.xlabel("age")
plt.ylabel("time spent watching tv")
plt.scatter(xvalues,yvalues)
plt.show()
