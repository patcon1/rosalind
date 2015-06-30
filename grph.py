__author__ = 'pconn'

# this bit reads in a fasta file and makes a dictionary. The keys are the
# label and the value is a string. it is from 'cons' and its not tolerant of faults

fastafile = open('grphfastas.fasta','r')

fastadict = {}
currentlabel = ''
for line in fastafile:
    if line[0] == ">":
        currentlabel = line[1:-1]
        fastadict[currentlabel] = ''
    else:
        fastadict[currentlabel] += (line[:].strip())

for seeknode in fastadict:
    for targetnode in fastadict:
        if targetnode != seeknode:
            if fastadict[seeknode][-3:] == fastadict[targetnode][0:3]:
                print(seeknode, targetnode)

