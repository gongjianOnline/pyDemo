import joblib
from matplotlib import pyplot as plt
from numpy.ma.core import reshape
from sklearn.neighbors import KNeighborsClassifier

def test_model():
    img = plt.imread("./data/demo.png")
    plt.imshow(img)
    plt.show()

    # 加载模型
    knn = joblib.load("./model/knn.pth")

    # 预测图片
    y_pred = knn.predict(img.reshape(1, -1))
    print("推理数据",y_pred)

if __name__=="__main__":
    test_model()