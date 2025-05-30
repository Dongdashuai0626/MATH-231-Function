import sympy as sp
import sys
from scipy.optimize import minimize_scalar
import math
x=sympy.S('x')
f=input("请输入一个python下的函数表达式，必须以x为变量，不需要引入库的前缀。例如 'sin(x)' 或 'x**2'：")
f=sympy.sympify(f)
jie=input("请输入积分区间，用逗号隔开上下界，先输入上界，圆周率请输入'pi'（不用引号）即可：")
parts = jie.split(',')
for i in range(2):
    if parts[i]=='pi':
        parts[i]=sp.pi
a=float(parts[0])
b=float(parts[1])
if b>=a:
    print('上下界输入反了，请先输入上界哦小笨蛋')
    sys.exit()
r=float(input('请输入要求精度'))
    
def findm2(f,b,a):
    sd= sp.diff(f,x,2)
    sd= sp.lambdify(x, sd, 'numpy')
    def func_to_maximize(val):
        return -abs(sd(val))
    result = minimize_scalar(func_to_maximize, bounds=(b,a), method='bounded')
    k= -result.fun
    return k

def findm4(f,b,a):
    fd= sp.diff(f,x,4)
    fd= sp.lambdify(x, fd, 'numpy')
    def func_to_maximize(val):
        return -abs(fd(val))
    result = minimize_scalar(func_to_maximize, bounds=(b,a), method='bounded')
    k= -result.fun
    return k
mod=int(input('您想求哪一种方法的n呢少侠/女侠？中点估计输入1，梯形估计输入2，抛物线估计输入3，小孩子才做选择，我是大人我全都要输入4'))
def nm(f,b,a,r):
    k=findm2(f,b,a)
    n=math.ceil(math.sqrt(k*(a-b)**3/24/r))
    return n
def nt(f,b,a,r):
    k=findm2(f,b,a)
    n=math.ceil((k*(a-b)**3/12/r)**0.5)
    return n
def ns(f,b,a,r):
    k=findm4(f,b,a)
    n=math.ceil((k*(a-b)**5/180/r) **0.25)
    if n%2==1:
        n+=1
    return n
dic={1:nm,2:nt,3:ns}
name={1:'中点',2:'梯形',3:'曲线'}
ott=[1,2,3]
if mod in ott:
    print(dic[mod](f,b,a,r))
if mod==4:
    for o in ott:
        print(name[o],'所需的n值为',dic[o](f,b,a,r))
