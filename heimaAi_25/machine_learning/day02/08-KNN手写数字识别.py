import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import numpy as np  # 新增：导入numpy

import warnings
warnings.filterwarnings("ignore")

# 读取数据并展示
data = pd.read_csv('./data/手写数字识别.csv')
x = data.iloc[:,1:]
y = data.iloc[:,0]
print(Counter(y))

# 数据展示（注释保留）
digit = x.iloc[2].values
img = digit.reshape(28,28)
plt.imshow(img,cmap='gray')
plt.imsave('demo.png',img)
plt.show()

# 分割数据
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=7)
#
# # ========== 新增：将DataFrame转为NumPy数组并修复内存布局 ==========
# x_train = np.ascontiguousarray(np.array(x_train))
# x_test = np.ascontiguousarray(np.array(x_test))
# y_train = np.array(y_train)
# y_test = np.array(y_test)
#
# # 模型训练
# estimator = KNeighborsClassifier(n_neighbors=3)
# estimator.fit(x_train,y_train)
#
# # 模型评估
# acc = estimator.score(x_test,y_test)
# print("测试集准确率",acc)
#
# # 模型保存（注释保留）
# joblib.dump(estimator,'./model/knn.pth')