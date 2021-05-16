#!/usr/bin/env python3

#Given two point masses in space, obj1 and obj2. Say obj1 has mass m and obj2 has mass 1. Suppose
#obj1 and obj2 begin at a distance of 1 from one another. Set the gravitational constant G to 1.
#Let x_1(t) be the position of obj1 at time t, and x_2(t) the position of obj2. Then
#x_1(t) - x_2(t) = r(t) satisfies the following differential equation:
#r(0) = 1. r'(0) = 0. r''(t) = (1+m)/(r(t))^2. 
def main():
    stepSize = 0.01
    stepCount = 50
    m = 0.2
    r = [1]
    v = [0]
    a = [-1-m]
    for t in range(stepCount):
        r.append(v[t]*stepSize + r[t])
        v.append(a[t]*stepSize + v[t])
        a.append((-1-m)/(r[t+1]*r[t+1]))
    print(r)
    return

if __name__ == '__main__':
    main()
