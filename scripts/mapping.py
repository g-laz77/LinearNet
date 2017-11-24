import os, sys


hi_dict = {}
i=0
with open('IITB.en-hi.hi.vcb') as hi_vcb:
    for line in hi_vcb:
        temp = line.split()
        if (i==1419):
            print temp
            print temp[2]
            print temp[1]
        i=i+1
        
        hi_dict[temp[1]] = (temp[2], temp[0])
i=0
for x, y in hi_dict.items():
    if (i<5):
        print x.decode('utf-8')
        print y
    i=i+1