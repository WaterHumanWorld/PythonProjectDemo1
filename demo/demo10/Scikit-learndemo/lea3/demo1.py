import sys

sys.stdout.reconfigure(encoding='utf-8')
from sklearn.datasets import load_iris

data = load_iris()
X = data.data  # 特征
y = data.target  # 标签
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

""" 33. 数据预处理
在训练模型之前，通常需要对数据进行预处理。常见的预处理步骤包括数据标准化、缺失值处理、特征选择等。对于随机森林分类器，数据标准化不是必须的，但为了保持一致性，我们仍然进行标准化处理 """

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

""" 4. 划分训练集和测试集
为了评估模型的性能，通常将数据划分为训练集和测试集。 """
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
""" 5. 选择模型
选择随机森林分类器作为模型： """
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)


""" 6. 训练模型
使用训练数据来训练模型： """
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

""" 8. 调参和优化
为了提高模型性能，可以进行超参数调优。Scikit-learn提供了多种工具，如GridSearchCV，用于自动搜索最佳参数组合。 """
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳得分: {grid_search.best_score_}")
""" 9. 保存和加载模型
训练好的模型可以保存下来，以便后续使用。 """
import joblib

# 保存模型
joblib.dump(model, 'random_forest_model.pkl')

# 加载模型
loaded_model = joblib.load('random_forest_model.pkl')

