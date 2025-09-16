import math as mt

m = int(input())
x = int(input())
y = int(input())
w = int(input())
h = int(input())
maxx = mt.ceil((x + w) / m)
minx = int(x / m)
maxy = mt.ceil((y + h) / m)
miny = int(y / m)
print((maxx - minx) * (maxy - miny))