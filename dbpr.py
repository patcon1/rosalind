__author__ = 'pconn'
from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('B5ZC00')
record = SwissProt.read(handle)

print(record)
