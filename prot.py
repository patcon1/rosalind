__author__ = 'pconn'

#read in the codon dictionary

codontablefile = open ('codontable.txt', 'r')
codondict = {}

for line in codontablefile:
    codondict[line[0:3]] = line[4:].strip()
codontablefile.close()

rnastring = input('please enter the rna to be translated')
rnalist = []

for i in range(0, len(rnastring),3):
    rnalist.append(rnastring[i:i+3])

for i in rnalist:
    if codondict[i] == 'Stop':
        break
    else:
        print(codondict[i], end='')


#this took a bloody bloody long time, many problems with the break s
# and other things
#there is definitely something wrong with this