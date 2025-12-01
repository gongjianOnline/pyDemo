from sklearn.datasets import load_iris


def myFun():
    my_iris = load_iris()
    print(my_iris.data[:5])
    print(my_iris.target)
    print(my_iris.target_names)
    print(my_iris.feature_names)


if __name__ == '__main__':
    myFun()