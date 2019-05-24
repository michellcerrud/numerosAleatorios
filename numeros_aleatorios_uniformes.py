import numpy as np
import matplotlib.pyplot as plt
s = np.random.uniform(-1,0,32000)
#len(s)
count, bins, ignored = plt.hist(s,15, density= True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()
