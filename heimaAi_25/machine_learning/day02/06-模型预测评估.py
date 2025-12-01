from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def demo04():
    # 1. 获取数据：Iris 鸢尾花数据集，150 条样本，4 个特征，3 个类别
    mydataSet = load_iris()          # 返回的是 Bunch 对象，类似字典
    # mydataSet.data     → 形状 (150, 4) 的 ndarray，特征矩阵
    # mydataSet.target   → 形状 (150,)   的 ndarray，标签 0/1/2

    # 2. 数据基本处理：随机 80 % 训练，20 % 测试，random_state 固定可复现
    x_train, x_test, y_train, y_test = train_test_split(
        mydataSet.data, mydataSet.target,
        test_size=0.2, random_state=22)

    # 3. 特征工程：标准化（Z-score），使每个特征均值≈0，方差≈1
    #    注意：测试集只能用训练集得到的均值/方差，防止“信息泄漏”
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)  # 先 fit 再 transform
    x_test  = transfer.transform(x_test)       # 只 transform

    # 4. 机器学习：选 KNN 分类器，K=3
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)            # 训练过程

    # 5. 模型评估：在测试集上计算准确率
    myscore = estimator.score(x_test, y_test)  # 返回正确预测的比例
    print("模型评估", myscore)                 # 输出如 0.9667

    # 模型预测
    mydata = [[5.1,3.5,1.4,0.2],[4.6,3.1,1.5,0.2]]
    mydata = transfer.transform(mydata)
    mypred = estimator.predict(mydata)
    print("直接输出结果",mypred)
    mypred = estimator.predict_proba(mydata)
    print("预测概率",mypred)

if __name__ == '__main__':
    demo04()
