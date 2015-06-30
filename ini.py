__author__ = 'pconn'

# first go at binf armory

from Bio.Seq import Seq

instring = Seq(input('put in the string'))
print(instring.count("A"), instring.count("C"),
      instring.count("G"), instring.count("T"))

