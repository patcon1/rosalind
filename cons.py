__author__ = 'pconn'

#lets make a fasta reader to read fasta files into dictionaries

fastafile = open('testfastareader.fasta','r')
stringdict = {}
currentlabel = ''
for line in fastafile:
    if line[0] == ">":
        currentlabel = line[1:-1]
        stringdict[currentlabel] = ''
    else:
        stringdict[currentlabel] += (line[:].strip())

#whats the longest sequence in the fasta file

maxlen = 0
for item in stringdict:
    if maxlen < len(stringdict[item]):
        maxlen = len(stringdict[item])
# print('maxlen is:', maxlen)

# make some lists with max len elements with zero in every element
listA = [0] * maxlen
listC = [0] * maxlen
listG = [0] * maxlen
listT = [0] * maxlen

#go through each item in each sequence and tally them up

for item in stringdict:
    for i in range(0,len(stringdict[item])):
        if stringdict[item][i] == 'A':
            listA[i] += 1
        elif stringdict[item][i] == 'C':
            listC[i] += 1
        elif stringdict[item][i] == 'G':
            listG[i] += 1
        elif stringdict[item][i] == 'T':
            listT[i] += 1
        else:
            print("there's weird stuff in the string")

# see which has the most, this is a slightly dodgy way but it is permitted by
# the rules

consensus = ''

for i in range(0,maxlen):
    if listA[i] >= listC[i] and listA[i] >= listG[i] and listA[i] >= listT[i]:
        consensus += "A"
    elif listC[i] >= listA[i] and listC[i] >= listG[i] and listC[i] >= listT[i]:
        consensus += "C"
    elif listT[i] >= listC[i] and listT[i] >= listG[i] and listT[i] >= listA[i]:
        consensus += "T"
    elif listG[i] >=listC[i] and  listG[i] >=listA[i] and  listG[i] >= listT[i]:
        consensus += "G"
    else:
        print('WWWWooooOOOoOOOOOooo', i)

print(consensus)


# the formatting of this was extremely difficult, i cant work out join

print('A:', *listA, sep=' ')
print('C:', *listC, sep=' ')
print('G:', *listG, sep=" ")
print('T:', *listT, sep=" ")