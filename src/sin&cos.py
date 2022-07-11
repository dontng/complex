'''
@Author: djology.w
@Date: 2022/7/12 0:50
@Desc:
'''
import numpy as np
import matplotlib.pyplot as plt

# 设置x, y轴的数值
x1 = np.linspace(0, 15, 100)
y1 = np.sin(x1)
y2 = np.cos(x1)

# 设置图形信息
plt.plot(x1, y1, label="$sin(x)", color="blue", linewidth=2)
plt.plot(x1, y2, label="$cos(x)", color="red", linewidth=2)

# 设置数轴信息
plt.xlabel("Domain")
plt.ylabel("Range")

# 设置图表抬头
plt.title("sin and cos")

# y轴范围
plt.ylim(-1.5, 1.5)

# 显示图示
plt.legend()

# 显示图
plt.show()


