from sklearn.preprocessing import StandardScaler

def demo04():
    # 1. 数据准备
    data = [[90,2,10,40],[60,4,15,45],[75,3,13,46]]
    # 2. 初始化标准化对象
    transformer = StandardScaler()
    # 3. 对原始特征进行变换
    data = transformer.fit_transform(data)
    # 4. 打印归一化结果
    print(data)

    # 5. 打印每一列数据的均值和方差
    print("transformer.mean--->",transformer.mean_)
    print("transformer.var-->",transformer.var_)

if __name__ == '__main__':
    demo04()