from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 加载数据
data = load_iris()
X = data.data  # 特征
y = data.target  # 标签

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.linear_model import LogisticRegression

# 选择模型
model = LogisticRegression(random_state=42)
from sklearn.model_selection import cross_val_score

# 使用交叉验证评估模型
scores = cross_val_score(model, X_scaled, y, cv=5)  # cv=5表示5折交叉验证

# 输出交叉验证得分
print(f"交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")
from sklearn.model_selection import StratifiedKFold

# 定义分层K折交叉验证
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 使用分层K折交叉验证评估模型
scores = cross_val_score(model, X_scaled, y, cv=skf)

# 输出交叉验证得分
print(f"分层K折交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")
from sklearn.model_selection import LeaveOneOut

# 定义留一法交叉验证
loo = LeaveOneOut()

# 使用留一法交叉验证评估模型
scores = cross_val_score(model, X_scaled, y, cv=loo)

# 输出交叉验证得分
print(f"留一法交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")
from sklearn.model_selection import LeavePOut

# 定义留P法交叉验证
lpo = LeavePOut(p=2)

# 使用留P法交叉验证评估模型
scores = cross_val_score(model, X_scaled, y, cv=lpo)

# 输出交叉验证得分
print(f"留P法交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold, LeaveOneOut, LeavePOut

# 加载数据
data = load_iris()
X = data.data  # 特征
y = data.target  # 标签

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 选择模型
model = LogisticRegression(random_state=42)

# 使用K折交叉验证评估模型
scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"K折交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")

# 使用分层K折交叉验证评估模型
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_scaled, y, cv=skf)
print(f"分层K折交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")

# 使用留一法交叉验证评估模型
loo = LeaveOneOut()
scores = cross_val_score(model, X_scaled, y, cv=loo)
print(f"留一法交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")

# 使用留P法交叉验证评估模型
lpo = LeavePOut(p=2)
scores = cross_val_score(model, X_scaled, y, cv=lpo)
print(f"留P法交叉验证得分: {scores}")
print(f"平均得分: {scores.mean()}")
print(f"标准差: {scores.std()}")
