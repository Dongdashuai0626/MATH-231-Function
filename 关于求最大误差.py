import sympy as sp
import sys
from scipy.optimize import minimize_scalar
x = sp.symbols('x')
f_input = input("请输入一个python下的函数表达式，必须以x为变量，不需要引入库的前缀。例如 'sin(x)' 或 'x**2'： ")
f = sp.sympify(f_input)
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
n=int(input('请输入分成的段数：'))
l=int(input('请输入希望保留的小数位数：'))

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

mod=int(input('您想求哪一种方法的误差上限呢少侠/女侠？中点估计输入1，梯形估计输入2，抛物线估计输入3，小孩子才做选择，我是大人我全都要输入4，调戏程序输入其他玩意：'))
def Em(k,b,a,n):
    return  round(k*(a-b)**3/(24*n**2),l)
def Et(k,b,a,n):
    return  round(k*(a-b)**3/(12*n**2),l)
def Es(k,b,a,n):
    return  round(k*(a-b)**5/(180*n**4),l)
if mod==1:
    k=findm2(f,b,a)
    errorm=Em(k,b,a,n)
if mod==2:
    k=findm2(f,b,a)
    errorm=Et(k,b,a,n)
if mod==3:
    k=findm4(f,b,a)
    errorm=Es(k,b,a,n)
if mod in [1,2,3]:
    print(errorm)
if mod==4:
    k=findm2(f,b,a)
    e1=Em(k,b,a,n)
    print('中点估算最大误差',e1)
    e2=Et(k,b,a,n)
    print('梯形估算最大误差',e2)
    k=findm4(f,b,a)
    e3=Es(k,b,a,n)
    print('曲线估算最大误差',e3)
else:
    print('广告位招租。别划走，相信我，不提前看程序代码99%的人都会点进来，这是绝佳广告位。有意向请联系jiacheng.24@intl.zju.edu.cn')
