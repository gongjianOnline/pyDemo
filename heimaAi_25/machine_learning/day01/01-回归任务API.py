from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics._plot import regression

# 回归问题： 目标值（标签值）是连续的
def dem01_Regression_pred():
    # 准备数据 平时成绩 期末成绩 最终成绩
    x = [[80,86],[82,80],[85,78],[90,90],[86,82],[82,90],[78,80],[92,94]]
    y = [84.2,80.6,80.1,90,83.2,87.6,79.4,93.4]
    # 3. 实例化 线性回归模型
    regression = LinearRegression()
    print("estimator--->",regression)

    # 模型训练
    # 打印线性回归模型参数 coef_ intercept_
    regression.fit(x, y)
    print("regression.coef--->",regression.coef_)
    print("regression.intercept--->",regression.intercept_)

    # # 模型预测
    # mypered = regression.predict([[90,80]])
    # print('mypered',mypered )

    # 模型保存
    joblib.dump(regression, './module/dem01_Regression_pred.bin')


# 模型调用
def handel_module():
    regression2 = joblib.load('./module/dem01_Regression_pred.bin')
    mypred2 =  regression2.predict([[90,80]])
    print(regression2.coef_)
    print(regression2.intercept_)
    print(mypred2)


if __name__ == '__main__':
    # dem01_Regression_pred()
    handel_module()
