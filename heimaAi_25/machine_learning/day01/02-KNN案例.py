from sklearn.neighbors import KNeighborsClassifier

# 分类问题： 目标值（标签值）是不连续的，分类种类：二分类、多分类等
def create_demo2():

    x = [[39,0,31],[3,2,65],[2,3,55],[9,38,2],[8,34,17],[5,2,57],[21,17,5],[45,2,9]]
    y = [0,1,2,2,2,1,0,0]

    # 实例化 KNN 模型
    estimator = KNeighborsClassifier(n_neighbors=3)
    print('estimator knn',estimator)

    # 模型训练
    estimator.fit(x, y)

    # 模型预测
    mypre = estimator.predict([[23,3,17]])
    print("mypre-->",mypre)

if __name__ == '__main__':
    create_demo2()