""" 4. 生成数据集
Scikit-learn 还提供了一些函数来生成合成数据集，用于测试和演示。 """
from sklearn.datasets import make_classification

# 生成一个分类数据集
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

"""  常用生成数据集的函数：
make_classification()：生成一个分类数据集
make_regression()：生成一个回归数据集
make_blobs()：生成聚类数据集
make_moons()：生成两个交错的半圆形数据集
make_circles()：生成两个嵌套的圆形数据集"""

""" 总结
内置数据集：使用 load_* 函数加载常用数据集。
从文件加载数据：使用 pandas 读取 CSV、Excel 等文件。
通过 API 获取数据：使用 fetch_openml 从 OpenML 获取数据集。
生成数据集：使用 make_* 函数生成合成数据集。
这些方法提供了灵活的方式来加载和处理数据，适用于不同的场景和需求。 """