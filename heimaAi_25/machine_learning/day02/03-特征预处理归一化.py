from sklearn.preprocessing import MinMaxScaler

def demo03_MinMaxScaler():
    # 1. 数据准备
    data = [[90,2,10,40],[60,4,15,45],[75,3,13,46]]
    # 初始化归一化对象
    transformer = MinMaxScaler()
    # 对原始特征进行变化
    data = transformer.fit_transform(data)

    # 打印归一化结果
    print(data)

if __name__ == '__main__':
    demo03_MinMaxScaler()