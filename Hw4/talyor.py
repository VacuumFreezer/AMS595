import numpy as np
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)  # 示例函数 f(x) = sin(x)

# 计算函数在 x = 0 处的泰勒展开，到 x 的 5 阶
taylor_expansion = sp.series(f, x, 0, 6).removeO()  # 第四个参数指定阶数（6 表示最多到 x 的 5 次方）


print("Taylor expansion of sin(x) around x = 0 up to 5th degree:")
print(taylor_expansion)