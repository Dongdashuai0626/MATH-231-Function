import sympy
import sys
x=sympy.S('x')
f=input("请输入一个python下的函数表达式，必须以x为变量，不需要引入库的前缀。例如 'sin(x)' 或 'x**2'：")
f=sympy.sympify(f)
jie=input("请输入积分区间，用逗号隔开上下界，先输入上界，圆周率请输入'pi'（不用引号）即可：")
parts = jie.split(',')
for i in range(2):
    if parts[i]=='pi':
        parts[i]=sympy.pi
a=float(parts[0])
b=float(parts[1])
if b>=a:
    print('上下界输入反了，请先输入上界哦小笨蛋')
    sys.exit()
p=int(input('请输入分成的段数：'))
l=int(input('请输入希望保留的小数位数：'))

#midpoint方法
def midpoint(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    for i in range(p):
        t = f.subs(x,b+0.5*gap+i*gap)
        T+=t
    T=T*gap
    return (round(T,l))

#梯形估计
def trapezoid(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    for i in range(p):
        t = f.subs(x,b+i*gap)
        T+=t
    T=gap*0.5*(T*2-f.subs(x,b)+f.subs(x,a))
    return (round(T,l))

#辛普森方法
def simpson(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    if p%2!=0:
        print("你输入了个奇数，你笨蛋啊~ 不要为难程序宝宝了。。。不跟你玩了嘤嘤嘤")
        sys.exit()
    for i in range(0,p,2):
        t=f.subs(x,b+i*gap)+4*f.subs(x,b+(i+1)*gap)+f.subs(x,b+(i+2)*gap)
        T+=t
    T=gap/3*T
    return (round(T,l))

mod=int(input('您想使用哪一种估计积分的方法呢少侠/女侠？中点估计输入1，梯形估计输入2，抛物线估计输入3，小孩子才做选择，我是大人我全都要输入4，调戏程序输入其他玩意：'))
dic={1:midpoint,2:trapezoid,3:simpson}
name={1:'中点',2:'梯形',3:'曲线'}
ott=[1,2,3]
if mod in ott:
    print('近似积分结果为',dic[mod](f,a,b,p,x))
elif mod==4:
    for o in ott:
        print(name[o],'近似积分结果为',dic[o](f,a,b,p,x))
else:
    print('广告位招租。别划走，相信我，不提前看程序代码99%的人都会点进来，这是绝佳广告位。有意向请联系jiacheng.24@intl.zju.edu.cn')
