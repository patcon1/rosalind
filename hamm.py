__author__ = 'pconn'

string1 = (input('put in the first string'))
string2 = (input("put in the second string"))

mismatches = 0

for i in range(0,len(string1)):
    if string1[i] != string2[i]:
        mismatches += 1
print(mismatches)