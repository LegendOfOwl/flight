import math
g=-9.81
m=float(input("enter your mass value:"))
v0=float(input("enter your velocity value:"))
F=g*m
t=0
x0=float(input("enter your axis value:"))
y0=float(input("enter your ordinate value:"))
angle=float(input("enter your angle in degrees:"))
a=math.radians(angle)
v0x=v0*math.cos(a)
v0y=v0*math.sin(a)
h=y0
iteration=0
while h>=0:
    vx = v0x
    vy = v0y + g*t
    v = math.sqrt(vy**2 + vx**2)
    x = x0 + v0x * t
    h=y0 + v0y*t + g*(t**2) / 2
    if iteration % 100 == 0:
        print(f"time:{round(t,4)} \ncoordinates:{round(x,4)},{round(h,4)}\nvelocities:{round(vx,4)},{round(vy,4)}-----")
    t+=0.0001
    iteration+=1
if h<0:
    h=0
print(f"time={round(t,4)} \ncoordinates={round(x,4)},{round(h,4)} \nvelocities={round(v,4)},{round(vx,4)},{round(vy,4)} \nForce={round(F,4)}")