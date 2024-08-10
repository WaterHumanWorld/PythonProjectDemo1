import sys

sys.stdout.reconfigure(encoding='utf-8')


from sklearn.datasets import load_iris

data = load_iris()
X = data.data  # 特征
y = data.target  # 标签
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
""" 5. 选择模型
选择逻辑回归分类器作为模型：
6. 训练模型
使用训练数据来训练模型： """
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)


""" 7. 评估模型
使用测试数据来评估模型的性能： """
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")
print("分类报告:")
print(classification_report(y_test, y_pred))
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))
""" 8. 调参和优化 """
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2']
}

grid_search = GridSearchCV(LogisticRegression(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳得分: {grid_search.best_score_}")
""" 9. 保存和加载模型
训练好的模型可以保存下来，以便后续使用。 """
import joblib

# 保存模型
joblib.dump(model, 'logistic_regression_model.pkl')

# 加载模型
loaded_model = joblib.load('logistic_regression_model.pkl')


