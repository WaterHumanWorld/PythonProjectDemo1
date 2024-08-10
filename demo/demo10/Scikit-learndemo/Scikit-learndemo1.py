# 导入必要的库
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 加载数据
def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

# 数据预处理
def preprocess_data(X, y):
    # 分割数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 标准化特征
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

# 训练模型
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# 评估模型
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

# 主函数
def main():
    # 加载数据
    X, y = load_data()
    
    # 数据预处理
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    
    # 训练模型
    model = train_model(X_train, y_train)
    
    # 评估模型
    accuracy, report = evaluate_model(model, X_test, y_test)
    
    print(f"模型准确率: {accuracy}")
    print("分类报告:")
    print(report)

if __name__ == "__main__":
    main()
