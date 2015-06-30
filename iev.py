__author__ = 'pconn'

#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa

listin = [0] * 6


for i in range(0,len(listin)):
    listin[i] = int(input('Value number'+ str(i)+":"))

listin[3] = int(listin[3]) * 0.75
listin[4] = int(listin[4]) * 0.5
listin[5] = 0



offspring = 0
for i in range(0,len(listin)):
    offspring += 2 * listin[i]

print(offspring)
