__author__ = 'pconn'
k = int(input ('k, the number of homozygous dominant organisms'))
m = int(input('input m the number of heterozygous organsims'))
n = int(input('input n the number of homozygous recessive organisms'))


# probability the first drawing is from k is k/(k+m+n)
kk = 0
km = 0
kn = 0
mm = 0
mn = 0
nn = 0


total = k+m+n

kk = k/total * (k-1) / (total-1)

km = k/total * m / (total-1)
km += m/total * k / (total-1)

kn = k/total * n/(total-1)
kn += n/total * k/(total-1)

mm = m/total * (m-1)/(total-1)

mn = m/total * n/(total-1)
mn += n/total * m/(total-1)


# disregard nn is has no effect

dom = 1*kk + 1*km + 1*kn + .75*mm + .5*mn

print (dom)
