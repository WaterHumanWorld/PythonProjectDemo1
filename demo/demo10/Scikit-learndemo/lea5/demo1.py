import sys

sys.stdout.reconfigure(encoding='utf-8')

from sklearn.datasets import load_iris

# 加载数据
data = load_iris()
X = data.data  # 特征
y = data.target  # 标签
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

# 定义模型
model = RandomForestClassifier(random_state=42)

# 定义参数分布
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 4)
}
from sklearn.model_selection import RandomizedSearchCV

# 初始化RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)

# 训练模型
random_search.fit(X_train, y_train)

# 输出最佳参数和最佳得分
print(f"最佳参数: {random_search.best_params_}")
print(f"最佳得分: {random_search.best_score_}")
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 使用最佳参数的模型进行预测
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")

# 生成分类报告
print("分类报告:")
print(classification_report(y_test, y_pred))

# 生成混淆矩阵
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
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

# 定义模型和参数分布
model = RandomForestClassifier(random_state=42)
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 4)
}

# 使用RandomizedSearchCV进行超参数调优
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)

# 输出最佳参数和最佳得分
print(f"最佳参数: {random_search.best_params_}")
print(f"最佳得分: {random_search.best_score_}")

# 使用最佳参数的模型进行预测
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")

# 生成分类报告
print("分类报告:")
print(classification_report(y_test, y_pred))

# 生成混淆矩阵
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
