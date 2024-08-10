""" 3. 通过 API 获取数据
Scikit-learn 提供了 fetch_openml 函数，可以从 OpenML 平台获取数据集。

示例代码： """
from sklearn.datasets import fetch_openml
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 从 OpenML 获取数据集
mnist = fetch_openml('mnist_784')
X, y = mnist.data, mnist.target
