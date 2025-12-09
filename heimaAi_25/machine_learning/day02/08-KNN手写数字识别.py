import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import numpy as np  # 新增：导入numpy
from sklearn.model_selection import GridSearchCV, cross_val_score


import warnings
warnings.filterwarnings("ignore")

# 读取数据并展示
data = pd.read_csv('./data/手写数字识别.csv')
x = data.iloc[:,1:]
y = data.iloc[:,0]


print(y)


# 数据展示（注释保留）
# digit = x.iloc[2].values
# img = digit.reshape(28,28)
# plt.imshow(img,cmap='gray')
# plt.imsave('demo.png',img)
# plt.show()

# 分割数据
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=7)

# ========== 新增：将DataFrame转为NumPy数组并修复内存布局 ==========
x_train = np.ascontiguousarray(np.array(x_train))
x_test = np.ascontiguousarray(np.array(x_test))
y_train = np.array(y_train)
y_test = np.array(y_test)

knn = KNeighborsClassifier()
# 2）定义要搜索的超参数网格
param_grid = {
    "n_neighbors": [3, 5, 7, 9, 11],    # K 值
    "weights": ["uniform", "distance"], # 距离权重：均匀 / 距离加权
    "p": [1, 2]                          # 距离度量：1=曼哈顿，2=欧式
}

# 3）构造 GridSearchCV：带 5 折交叉验证
grid_search = GridSearchCV(
    estimator=knn,
    param_grid=param_grid,
    cv=5,                 # 5 折交叉验证
    scoring="accuracy",   # 评估指标：准确率
    n_jobs=-1,            # 用所有CPU核并行
    verbose=2             # 输出搜索过程
)

print("开始进行网格搜索 + 交叉验证...")
grid_search.fit(x_train, y_train)

print("搜索结束！")
print("最佳参数：", grid_search.best_params_)
print("训练集 5 折交叉验证的最高平均准确率：", grid_search.best_score_)

# 4）取出最优模型，在测试集上评估
best_knn = grid_search.best_estimator_
y_pred = best_knn.predict(x_test)
test_acc = accuracy_score(y_test, y_pred)
print("在测试集上的准确率：", test_acc)

# 6）保存最优模型（路径不存在的话记得先建 ./model 目录）
joblib.dump(best_knn, "./model/knn.pth")
print("最优模型已保存到 ./model/knn.pth")

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