import math
g=-9.81
m=float(input("enter your mass value:"))
v0=float(input("enter your velocity value:"))
F=g*m
t=0
h0=float(input("enter your height value:"))
h=h0
iteration=0
while h>=0:
    v=v0 + g*t
    h=h0 + v0*t + g*(t**2) / 2
    if iteration % 100 == 0:
        print("velocity =",round(v,4),"height =",round(h,4),"time =",round(t,4))
    t+=0.0001
    iteration+=1
if h<0:
    h=0
print("velocity =",round(v,4),"height =",round(h,4),"time =",round(t,4))