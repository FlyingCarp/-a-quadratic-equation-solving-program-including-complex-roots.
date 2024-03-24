import math
while(True):
    print("请输入：ax^2+bx+c=0的参数a,b,c：")
    a=b=c=0
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    print(f"一元二次方程：{'+' if a > 0 else ''}{a}x^2 {'+' if b > 0 else ''}{b}x {'+' if c > 0 else ''}{c} = 0 的解是：")
    delta=b*b-4*a*c
    if delta>0:
        print("x1=",(-b+math.sqrt(delta))/(2*a),"x2=",(-b-math.sqrt(delta))/(2*a))
    if delta == 0:
        print("x1=x2=",-b/(2*a))
    if delta <0:
        print("x1=",-b/(2*a),f"+{math.sqrt(-delta)/(2*a)}i","x2=",-b/(2*a),f"-{math.sqrt(-delta)/(2*a)}i")
    print("\n")