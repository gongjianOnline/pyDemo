# 导入 Kmeans 聚类算法
# 用途： 用来把数据分成若干组（簇），属于，无监督学习
# 核心思想：自动找出数据中相似的样本，把他们聚在一起
import os
os.environ["OMP_NUM_THREADS"] = "4"
from sklearn.cluster import KMeans
# 生成模拟的聚类样本数据
# 用途：常用测试聚类算法
# 功能：可以制定生成多少个样本点，簇的数量，分布范围
from sklearn.datasets import make_blobs
# 导入可视化图库
import matplotlib.pyplot as plt
# 导入 Calinski-Harabasz 指数（CH指数），一种聚类效果评估指标
# 用途：衡量聚类结果的好坏（数值越大越好）
# 原理：比较簇间离散度和簇内紧密度的比值
from sklearn.metrics import calinski_harabasz_score



def dm04_kmeans():
    x,y = make_blobs(n_samples=1000,n_features=2,centers=[[-1,-1],[0,0],[1,1],[2,2]],
                     cluster_std=[0.4,0.2,0.2,0.2],random_state=1)
    plt.figure()
    plt.scatter(x[:,0],x[:,1],marker='o')
    plt.show()

    # 使用 k-means 进行聚类，并使用CH方法评估
    # 3-1 n_clusters=2
    # fit_predict(x): 同时完成训练和预测，返回每个样本的聚类标签
    # y_pred = KMeans(n_clusters=2,random_state=22,init='k-means++').fit_predict(x)
    # plt.scatter(x[:,0],x[:,1],c=y_pred)
    # plt.show()
    # print("1--->",calinski_harabasz_score(x,y))

    # 3-2 n_clusters=3
    # y_pred = KMeans(n_clusters=3, random_state=22, init='k-means++').fit_predict(x)
    # plt.scatter(x[:, 0], x[:, 1], c=y_pred)
    # plt.show()
    # print("2--->", calinski_harabasz_score(x, y))

    # 3-3 n_clusters=4
    # 拆解
    # 模型实例化
    kmeans_cls = KMeans(n_clusters=4,init='k-means++',n_init="auto")
    # 模型预测
    y_pred = kmeans_cls.fit_predict(x)
    plt.scatter(x[:,0],x[:,1],c=y_pred)
    plt.show()
    # 模型评估
    print(calinski_harabasz_score(x,y))

    # 模型评估
    print("模型评估---->",calinski_harabasz_score(x, y_pred))
if __name__ == '__main__':
    dm04_kmeans()
