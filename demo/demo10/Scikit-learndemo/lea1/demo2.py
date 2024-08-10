""" 2. 从文件加载数据
你可以从 CSV 文件、Excel 文件等加载数据。通常使用 pandas 库来处理这些文件。

示例代码： """
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 从 CSV 文件加载数据
data = pd.read_csv('path/to/your/file.csv')
X = data.drop('target_column', axis=1).values
y = data['target_column'].values
