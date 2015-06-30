__author__ = 'pconn'

stringy = input("put in the input string:")

A = 0
C = 0
T = 0
G = 0


for i in range(0, len(stringy)):
    if stringy[i] == "A":
        A += 1
    elif stringy[i]== "C":
        C += 1
    elif stringy[i] == "T":
        T +=1
    elif stringy [i] == "G":
        G += 1
    else:
        print("there is something else in the string")

print(A, C, G, T)

