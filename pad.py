import pandas as pd
import numpy as np

product = ["rice", "bean", "garry", "soup"]
print(pd.Series(product))
print(type(pd.Series(product)))

num = np.array([44, 48, 94, 39])
d = pd.Series(num)
print(d)