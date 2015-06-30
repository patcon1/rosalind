__author__ = 'pconn'
stringcheese = input("put in the string:")

shunary = {}

for word in stringcheese.split(' '):
    if word not in shunary:
        shunary[word] = 1
    else:
        shunary[word] += 1

for key, value in shunary.items():
    print(key, end=' ')
    print(value)
