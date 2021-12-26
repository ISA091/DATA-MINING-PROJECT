import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer

#Original DataSet we can choose any one of them
dataset = pd.read_csv("MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv")

X = np.nan_to_num(dataset[dataset.columns[0:78]])


X_ = X.astype(np.float32)

plt.figure(1)
plt.hist(X_[:,1])
plt.title('Flow Duration')

plt.figure(2)
plt.hist(X_[:,13])
plt.title('Bwd Packet Length Std')

plt.figure(3)
plt.hist(X_[:,17])
plt.title('Flow IAT Std')
