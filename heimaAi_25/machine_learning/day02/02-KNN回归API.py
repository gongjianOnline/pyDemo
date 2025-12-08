from sklearn.neighbors import KNeighborsRegressor

def demo02_knnapi():
    estimator = KNeighborsRegressor(n_neighbors=5)
    x = [[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80], [92, 94]]
    y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]
    estimator.fit(x, y)

    result = estimator.predict([[20,20]])
    print(result)

if __name__ == '__main__':
    demo02_knnapi()