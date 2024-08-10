from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 将数据集分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

""" 2. 标准化处理
标准化处理通常使用 StandardScaler 类，将特征缩放到均值为 0，标准差为 1 的标准正态分布。 """


from sklearn.preprocessing import StandardScaler

# 创建 StandardScaler 对象
scaler = StandardScaler()

# 对训练集进行拟合和转换
X_train_scaled = scaler.fit_transform(X_train)

# 对测试集进行转换
X_test_scaled = scaler.transform(X_test)
