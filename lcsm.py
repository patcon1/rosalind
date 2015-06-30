



def fastareader(filename):
    fastafile = open(filename,'r')
    stringdict = {}
    currentlabel = ''
    for line in fastafile:
        if line[0] == ">":
            currentlabel = line[1:-1]
            stringdict[currentlabel] = ''
        else:
            stringdict[currentlabel] += (line[:].strip())
    return stringdict


print(fastareader('testfasta.fasta'))


# http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
# came across this here
# see if I can understand it

def long_substr(data):                                # define a function with one param start up  a function
    substr = ''                                       # initialise an empty substring
    if len(data) > 1 and len(data[0]) > 0:            # if the inpit strin is not empty
        for i in range(len(data[0])):                 # i is every element in  data
            for j in range(len(data[0])-i+1):         # j is....... i eon quite get it- j is length and i is the start
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr


def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


sequencelist = []
seqdict = fastareader('rosalind_lcsm.txt')
for key in seqdict:
    sequencelist.append(seqdict[key])

print(long_substr(sequencelist))


__author__ = 'pconn'
