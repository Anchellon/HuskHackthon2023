import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

import pandas as pd

df = pd.read_csv("../../AIS_2022_01_01/AIS_2022_01_01.csv")

print(df.head())