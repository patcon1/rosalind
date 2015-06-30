__author__ = 'pconn'


n = int(input("how many generations"))

minus2 = 0
minus1 = 0
thismonth = 1

k = int(input("how many pairs each generation"))


for i in range(1,n+1):
    print("the number of pairs in month",i, 'is', thismonth)
    minus2 = minus1
    minus1 = thismonth
    thismonth = minus1 + (minus2 * k)


