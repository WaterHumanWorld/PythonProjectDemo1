import sys

sys.stdout.reconfigure(encoding='utf-8')

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 加载数据
data = load_iris()
X = data.data  # 特征
y = data.target  # 标签

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 选择模型
model = LogisticRegression(random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")

# 生成分类报告
print("分类报告:")
print(classification_report(y_test, y_pred))

# 生成混淆矩阵
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
