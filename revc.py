__author__ = 'pconn'

# this is built from the translate to rna

__author__ = 'pconn'

dnastrand = input("input the dna string")

revcom = []

for i in range(0,len(dnastrand)):
   if dnastrand[i] == 'A':
       revcom.insert(0,"T")
   elif dnastrand[i] == 'C':
       revcom.insert(0,"G")
   elif dnastrand[i] == 'T':
       revcom.insert(0,'A')
   elif dnastrand[i] == 'G':
       revcom.insert(0,"C")
   else:
       print('there is weird stuff in the input string')

outstring = ''.join(revcom)

print('the rna strand is:')
print(outstring)