__author__ = 'pconn'
a = int(input("put in the first value"))
b = int(input("put in the second value"))

c = 0

for i in range(a, b+1):
    if i%2 != 0:
        c += i
print(c)
