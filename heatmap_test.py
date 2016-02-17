import numpy as np 
from pandas import *

Index= ['aaa','bbb','ccc','ddd','eee']
Cols = ['A', 'B', 'C','D']
df = DataFrame(abs(np.random.randn(5, 4)), index= Index, columns=Cols)

print(df)


import numpy as np 
from pandas import DataFrame
import matplotlib.pyplot as plt



plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()
