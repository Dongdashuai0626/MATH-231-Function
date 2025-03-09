import sympy
import numpy as np
from scipy.integrate import quad

# 定义变量
x = sympy.symbols('x')

# 输入函数表达式
f_expr = input("请输入一个python下的函数表达式，必须以x为变量，不需要引入库的前缀。例如 'sin(x)' 或 'x**2'：")
f = sympy.sympify(f_expr)

# 输入积分区间
jie = input("请输入积分区间，用逗号隔开上下界，先输入下界，圆周率请输入'pi'（不用引号）即可：")
parts = jie.split(',')
for i in range(2):
    if parts[i] == 'pi':
        parts[i] = sympy.pi
a = float(parts[0])
b = float(parts[1])
if a >= b:
    print('上下界输入反了，请先输入下界哦小笨蛋')
    sys.exit()

# 定义函数的导数
f_prime = sympy.diff(f, x)

# 将符号函数转换为数值函数
f_prime_func = sympy.lambdify(x, f_prime, 'numpy')

# 定义函数长度的被积函数
def integrand(x):
    return np.sqrt(1 + f_prime_func(x)**2)

# 计算函数长度
length, _ = quad(integrand, a, b)

# 输出结果
print(f"函数在区间 [{a}, {b}] 上的长度为: {length}")