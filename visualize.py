import pandas as pd

# Try reading the file with different encodings
try:
    data = pd.read_csv('data/data.csv', encoding='utf-8')
except UnicodeDecodeError:
    try:
        data = pd.read_csv('data/data.csv', encoding='latin-1')
    except UnicodeDecodeError:
        data = pd.read_csv('data/data.csv', encoding='ISO-8859-1')


# 查看前几行数据
print(data.head())

# 获取数据的基本信息
print(data.info())

# 查看数据统计信息
print(data.describe())


# 分组统计
grouped_data = data.groupby('category_column')['value_column'].mean()
print(grouped_data)
