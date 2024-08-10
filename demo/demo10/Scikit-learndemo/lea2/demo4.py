from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 将数据集分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#其他预处理方法
""" 除了标准化处理，Scikit-learn 还提供了其他多种预处理方法，例如：

归一化 (Normalization)：使用 MinMaxScaler 将特征缩放到一个指定的范围（例如 [0, 1]）。
正则化 (Normalization)：使用 Normalizer 将每个样本缩放到单位范数。
缺失值处理 (Handling Missing Values)：使用 SimpleImputer 填充缺失值。
编码分类变量 (Encoding Categorical Variables)：使用 OneHotEncoder 或 LabelEncoder 将分类变量转换为数值。 """

from sklearn.preprocessing import MinMaxScaler, Normalizer,  OneHotEncoder
from sklearn.impute import SimpleImputer
# 归一化
min_max_scaler = MinMaxScaler()
X_train_normalized = min_max_scaler.fit_transform(X_train)
X_test_normalized = min_max_scaler.transform(X_test)

# 正则化
normalizer = Normalizer()
X_train_normalized = normalizer.fit_transform(X_train)
X_test_normalized = normalizer.transform(X_test)

# 缺失值处理
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# 编码分类变量
encoder = OneHotEncoder()
X_train_encoded = encoder.fit_transform(X_train)
X_test_encoded = encoder.transform(X_test)

""" 总结
分割数据集：使用 train_test_split 函数。
标准化处理：使用 StandardScaler 类。
其他预处理方法：包括归一化、正则化、缺失值处理和编码分类变量等。
通过这些方法，你可以有效地预处理数据，为后续的机器学习模型训练做好准备。 """