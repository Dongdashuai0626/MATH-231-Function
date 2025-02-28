import sympy
def trapezoid(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    for i in range(p):
        t = f.subs(x,b+i*gap)
        T+=t
    T=gap*0.5*(T*2-f.subs(x,b)+f.subs(x,a))
    Emax=sympy.diff(f,x,2)
    k1 = sympy.maximum(Emax,x)   #代替绝对值功能
    k2 = sympy.minimum(Emax,x)
    k = max(abs(k1),abs(k2))   #选择绝对值的最大值
    E = k*(a-b)**3/(12*p**2)
    return (T,E)
#midpoint方法
def midpoint(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    for i in range(p):
        t = f.subs(x,b+0.5*gap+i*gap)
        T+=t
    T=T*gap
    Emax=sympy.diff(f,x,2)
    k1 = sympy.maximum(Emax,x)   #代替绝对值功能
    k2 = sympy.minimum(Emax,x)
    k = max(abs(k1),abs(k2))   #选择绝对值的最大值
    E = k*(a-b)**3/(24*p**2)
    return (T,E)
#辛普森方法
def simpson(f,a,b,p,x):
    T = 0
    gap = (a-b)/p
    if p%2!=0:#检测是否为偶数
        print("你他娘输入了个奇数，你是笨蛋吗？？？")
        return 0
    for i in range(0,p,2):#计算approximations integral
        t = f.subs(x,b+i*gap)+4*f.subs(x,b+(i+1)*gap)+f.subs(x,b+(i+2)*gap)
        T+=t
    T=gap/3*T
    Emax=sympy.diff(f,x,4)
    k1 = sympy.maximum(Emax,x)   #代替绝对值功能
    k2 = sympy.minimum(Emax,x)
    k = max(abs(k1),abs(k2))   #选择绝对值的最大值
    E = k*(a-b)**5/(180*p**4)
    return (T,E)


