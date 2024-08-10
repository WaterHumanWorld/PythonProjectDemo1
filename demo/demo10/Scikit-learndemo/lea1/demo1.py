""" 1. 内置数据集
Scikit-learn 自带了一些常用的数据集，可以直接加载使用。这些数据集通常用于示例和测试。

示例代码： """
 
from sklearn.datasets import load_iris # type: ignore
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

""" 常用内置数据集：
load_iris()：鸢尾花数据集
load_boston()：波士顿房价数据集（已弃用，建议使用 fetch_openml）
load_digits()：手写数字数据集
load_diabetes()：糖尿病数据集
load_linnerud()：Linnerud 体能训练数据集
load_wine()：葡萄酒数据集
load_breast_cancer()：乳腺癌数据集 """