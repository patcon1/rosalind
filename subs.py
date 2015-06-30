__author__ = 'pconn'

targetst = input('enter the target string')
searchst = input('enter the search string')

locationlist = []


for i in range(0, len(targetst)-(len(searchst)-1)):
    if searchst == targetst[i:i+len(searchst)]:
        locationlist.append(i+1)

for element in locationlist:
    print(element, end =' ')

