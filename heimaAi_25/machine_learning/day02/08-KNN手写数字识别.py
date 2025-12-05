import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

import  warnings
warnings.filterwarnings("ignore")

# 读取数据并展示
data = pd.read_csv('./data/手写数字识别.csv')
x = data.iloc[:,1:]
y = data.iloc[:,0]
print(Counter(y))

# 数据展示
digit = x.iloc[5].values
img = digit.reshape(28,28)
plt.imshow(img,cmap='gray')
plt.imsave('demo.png',img)
plt.show()