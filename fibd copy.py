__author__ = 'pconn'

# this is FIBD the mortal fibonacci rabbits
# N is an integer <100 and M is an integer <20
# the number of rabbits alive after N months if rabbits live for M months
# they take a month to mature
# make a list of M elements and step through it n times

n = int(input("put in n the number of months the sim is run for"))
m = int(input("put in m the number of months the rabbits live for"))



agelist = [0] * m


agelist[0] = 1 # set the start- one pair of rabbits in the first month

for i in range(1, n): # the sim starts at 1 as the initial rabbit is already added/ the first step has happened

    newrabbits = 0

    for j in range(m-1, 0, -1):  #  steps through every age from the back starting at the second

        newrabbits += agelist[j] # add the progeny of each month to newrabbits (wont get to zero tho)
        agelist[j] = agelist[j-1] # move the rabbits one month forward in age, the oldest are overwritten

    agelist[0] = newrabbits

    print(agelist)

total = 0
for rabbits in agelist:
    total += rabbits
print(total)