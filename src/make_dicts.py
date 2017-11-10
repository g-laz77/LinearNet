import os
import sys
import re

input_file = sys.argv[1]

cmd = 'cat ' + str(input_file) + ' | wc -l'
p = os.popen(cmd, "r")

line = p.readline()
line = ''.join(list(line)[2:-1])
no_lines = int(line)
<<<<<<< HEAD
# print no_lines, type(no_lines)
final_dict = {}

line_number = 0
=======
print no_lines, type(no_lines)
final_dict = {}

line_number = 0
print 'hll'
>>>>>>> cdea5f9ddecc331f9e22369a4757867457305166
words = []
s = 0
with open(input_file,'r') as f:
    for line in f:
<<<<<<< HEAD
        # print line  #, line_number
=======
        print line  #, line_number
>>>>>>> cdea5f9ddecc331f9e22369a4757867457305166
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
<<<<<<< HEAD
            list_of_words = list()
            for word in hindi_words:
                if word == "({" or word == "})" or word in ["1","2","3","4","5","6","7","8","9","0"]:
                    continue
                else:
                    list_of_words.append(word)
            
            lists = re.findall(r'(\(\{(\s*[0-9]*\s*)*\}\))',line)

            for i in range(len(lists)):
                lists[i] = lists[i][0]
            print lists
            del(lists[0])
            del(list_of_words[0])
            for i in range(len(list_of_words)):
                hindi_word = list_of_words[i]
                print hindi_word
                mapping = lists[i].split()
                if len(mapping) == 2:
                    continue
                else:
                    del(mapping[len(mapping)-1])
                    del(mapping[0])
                    print mapping
                    eng_words = ''
                    for i in range(len(mapping)):
                        index = mapping[i]
                        # print words[int(i)-1]
                        eng_words += (words[int(index)-1])
                        if i != len(mapping) - 1:
                            eng_words = eng_words + '_'
                    print eng_words
                    if hindi_word not in final_dict.keys():
                        final_dict[hindi_word] = eng_words



        line_number += 1
print final_dict
=======
            # lists1 = re.findall(ur'^\(.*',line)
            lists = re.findall(r'(\(\{(\s*[0-9]*\s*)*\}\))',line)
            print lists
        line_number += 1
>>>>>>> cdea5f9ddecc331f9e22369a4757867457305166
