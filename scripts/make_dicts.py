import os
import sys
import re

input_file = sys.argv[1]

cmd = 'cat ' + str(input_file) + ' | wc -l'
p = os.popen(cmd, "r")

line = p.readline()
line = ''.join(list(line)[2:-1])
no_lines = int(line)
print no_lines, type(no_lines)
final_dict = {}

line_number = 0
print 'hll'
words = []
s = 0
with open(input_file,'r') as f:
    for line in f:
        print line  #, line_number
        if line_number%3 == 0:
            s += 1
            if s is 2:
                break
        elif line_number%3 == 1:
            words = line.split()
            print words
        else:
            # print words
            hindi_words = line.split()
            # lists1 = re.findall(ur'^\(.*',line)
            lists = re.findall(r'(\(\{(\s*[0-9]*\s*)*\}\))',line)
            print lists
        line_number += 1