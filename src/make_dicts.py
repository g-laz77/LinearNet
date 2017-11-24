import os
import sys
import re
import pickle


no_of_files = len(sys.argv) - 1
final_dict = {}

del(sys.argv[0])

for i in range(0, no_of_files):
    input_file = sys.argv[i]
    cmd = 'cat ' + str(input_file) + ' | wc -l'
    p = os.popen(cmd, "r")

    line = p.readline()
    line = ''.join(list(line)[2:-1])
    no_lines = int(line)
    # print no_lines, type(no_lines)


    line_number = 0
    words = []
    s = 0
    with open(input_file,'r') as f:
        for line in f:       # print line  #, line_number

            # print line  #, line_number

            if line_number%3 == 0:
                pass
                # s += 1
                # if s is 2:
                    # break
            elif line_number%3 == 1:
                words = line.split()
                print '======= NEW SENTENCE ======='
                print line
                # print words
            else:
                # print words
                print line
                flag = 0
                to_delete = []
                hindi_words = line.split()
                list_of_words = list()
                # print hindi_words
                for word in range(len(hindi_words)):
                    # print word, flag, hindi_words[word]
                    if hindi_words[word] == "({":
                        # print 'In 1'
                        flag = 1
                        to_delete.append(word)
                    elif hindi_words[word] == '})':
                        # print 'In 3'
                        to_delete.append(word)
                        flag = 0
                    elif flag == 1:
                        # print 'In 2'
                        to_delete.append(word)
                    else:
                        continue
                to_delete = to_delete[::-1]
                for i in to_delete:
                    del(hindi_words[i])
                list_of_words = hindi_words
                # print list_of_words
                lists = re.findall(r'(\(\{(\s*[0-9]*\s*)*\}\))',line)

                for i in range(len(lists)):
                    lists[i] = lists[i][0]
                # print lists
                del(lists[0])
                del(list_of_words[0])
                for i in range(len(list_of_words)):
                    # print 'NEW MAPPING'
                    hindi_word = list_of_words[i]
                    # print 'hindi_word->', hindi_word
                    mapping = lists[i].split()
                    if len(mapping) == 2:
                        continue
                    else:
                        del(mapping[len(mapping)-1])
                        del(mapping[0])
                        # print mapping
                        eng_words = ''
                        for i in range(len(mapping)):
                            index = mapping[i]
                            # print words[int(i)-1]
                            eng_words += (words[int(index)-1])
                            if i != len(mapping) - 1:
                                eng_words = eng_words + '_'
                        # print eng_words
                        if hindi_word not in final_dict.keys():
                            final_dict[hindi_word] = eng_words



            line_number += 1
    print final_dict
with open('myDictionary.txt','wb') as f:
    pickle.dump(final_dict, f)
f.close()
