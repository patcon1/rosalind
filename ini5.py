# make a file of all the even numbered lines of another file

infile = open('rosalind_ini5.txt')
evenodd = False
outfile = open('ini5outputfile', 'w')

for line in infile:
    if evenodd:
        outfile.write(line)
        #note that the end='' is needed or the output has newlines in between
    evenodd = not evenodd
infile.close()
outfile.close()
