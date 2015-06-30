__author__ = 'pconn'

dnastrand = input("input the dna string")

rnastrand = []

for i in range(0,len(dnastrand)):
   if dnastrand[i] == 'A':
       rnastrand.append("A")
   elif dnastrand[i] == 'C':
       rnastrand.append("C")
   elif dnastrand[i] == 'T':
       rnastrand.append('U')
   elif dnastrand[i] == 'G':
       rnastrand.append("G")
   else:
       print('there is weird stuff in the input string')

outstring = ''.join(rnastrand)

print('the rna strand is:')
print(outstring)