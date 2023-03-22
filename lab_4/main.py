from sklearn.datasets import load_boston
boston = load_boston()
print(boston.keys())
import numpy as np
import pandas as pd
X = pd.DataFrame(boston.data,columns=boston.feature_names)
X['target'] = boston.target
print(X.head())
X.to_csv("marcinello.csv")