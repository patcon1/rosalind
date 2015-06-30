__author__ = 'pconn'

# this bit reads in a fasta file and makes a dictionary. The keys are the
# label and the value is a string. it is from 'cons' and its not tolerant of faults

fastafile = open('gcsample.fasta','r')
stringdict = {}
currentlabel = ''
for line in fastafile:
    if line[0] == ">":
        currentlabel = line[1:-1]
        stringdict[currentlabel] = ''
    else:
        stringdict[currentlabel] += (line[:].strip())

gcdict = {}

#go through each dna string and each nucleotide in the string
# increment the counter according to the nucleotide
# make a dictionary with the same keys but the value is the gc%

for dnastring in stringdict:
    currentAT = 0
    currentGC = 0
    for nucleotide in stringdict[dnastring]:
        if nucleotide == 'A' or nucleotide == 'T':
            currentAT +=1
        elif nucleotide == 'G' or nucleotide == 'C':
            currentGC += 1
        else:
            print('s something weird in the string')
   # print(currentAT, currentGC)
    gcdict[dnastring] = currentGC/(currentAT+currentGC)*100


# go through the items in the gc dictionary and poop out the highest or equal highest

#first make a list of the values and keys in teh dictionary
gcdictvalues = list(gcdict.values())
gcdictkeys = list(gcdict.keys())

# this is a bit tricky
# this uses max(gcdictvalues) to find the highest then it uses index to find
#where that is in the list, and grabs the same index from the list of keys
print(gcdictkeys[gcdictvalues.index(max(gcdictvalues))])
print(max(gcdictvalues))

