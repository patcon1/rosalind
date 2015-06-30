__author__ = 'pconn'


fastafile = open('mprt.fasta','r')
stringdict = {}
currentlabel = ''
for line in fastafile:
    if line[0] == ">":
        currentlabel = line[1:-1]
        stringdict[currentlabel] = ''
    else:
        stringdict[currentlabel] += (line[:].strip())

print(stringdict.keys())

# Looking for N (asparigine) then Not p (not proline) then
# S or T serine or threonine then not P:  N{P}[ST]{P}

# if we are looking for a pattern of n residues the last one we want to search is len - n
# for [ABCDE] len = 5 element [4] is E and is sufficient for a 1 character search
# element 5-2 = 3 is the last for a

#was going to use a pattern match counter but i was concerned i might miss a new start
#if the pattern was a little established already
# so i am going to reach forward which will be a bit inefficient

for protein in stringdict:
    for i in range(0, len(stringdict[protein])-4):
        if stringdict[protein][i] == "N":
            if stringdict[protein][i+1] != "P":
                if stringdict[protein][i+2] == "S" or stringdict[protein][i+2] == "T":
                    if stringdict[protein][i+3] != 'P':
                        print ('woopdy', i, protein )

