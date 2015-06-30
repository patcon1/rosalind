__author__ = 'pconn'

n= int(input('n the lifespan'))
m = int(input('m the number of months the sim is run for'))

# remember this bit of syntas: it creates a list with m elements each is 0
#the population is represented by list, the age of each rabbit in months is the
# nth element
rabbitpop = [0] * n

# the program starts with 1 pair rabbits
rabbitpop[0]= 1

print(rabbitpop)

for h in range(0,m):
    #move each month along the list by 1 as they age, the last is overwritten/dies
    for i in range((len(rabbitpop)-1), 0 , -1):
        rabbitpop[i] = rabbitpop[i-1]
    #count all the rabbits older than 1
    gentotal = 0
    for i in range(1, len(rabbitpop)):
        gentotal += rabbitpop[i]
    # add one new rabbit for every mature rabbit
    rabbitpop[0] = gentotal
#    input()
    print(rabbitpop)

poptotal = 0
for monthtotal in rabbitpop:
    poptotal += monthtotal

print(poptotal)






"""
# this is executed every month
for month in range(0,m):
    #count the number of mature rabbits
    thismonthcount = 0
    for i in rabbitages[1:m]:
        print(i)
        thismonthcount += rabbitages[i]
    #move the population forward 1, the rabbits who are older than M fall off/die
    for i in range (len(rabbitages), 2 , -1):
        rabbitages[i-1] = rabbitages[i-2]

    # add 2 rabbits to the youngest group for every mature rabbit
    rabbitages[0] = 2 * thismonthcount
    print(rabbitages)
print('doneski')
"""