import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("用法: python sumif.py <文件名>")
    sys.exit(1)

file_name = sys.argv[1]

# 创建一个字典来存储分组和总和
sum_dict = defaultdict(lambda: defaultdict(float))

# 读取数据文件
try:
    with open(file_name, 'r') as file:
        for line in file:
            # 分割行数据
            parts = line.strip().split()
            if len(parts) >= 2:
                key = parts[0]
                values = map(float, parts[1:])  # 将值解析为浮点数
                # 更新字典中的总和
                for i, value in enumerate(values, start=2):
                    sum_dict[key][i] += value
except FileNotFoundError:
    print(f"文件 '{file_name}' 不存在。")
    sys.exit(1)

# 输出结果
for key, sums in sum_dict.items():
    print(f"{key}", end=' ')
    for i in range(2, int(max(sums.keys())) + 1):
        print(f"{sums[i]}", end=' ')
    print()

