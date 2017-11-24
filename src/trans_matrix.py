import numpy as np
import gensim
import sys
import pickle
import time

final_dict = sys.argv[1]
final_dict = pickle.load(open(final_dict,'rb'), encoding='latin1')
print('Dict loaded')

model2 = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)  
print('Eng model loaded')
model = gensim.models.Word2Vec.load('./models/hi')
print('Hin model loaded')

weight_vec = np.zeros((1, 300))

print(len(final_dict))

time.sleep(10)
alpha = 0.5

for iter in range(1,11,1):
    print(iter)
    sum = 0
    count = 0
    for key in final_dict:
        count += 1
        print(count,iter)
        eng_word = key
        hin_key = ' '.join(final_dict[eng_word].split('_'))
        if hin_key in model.wv.vocab and eng_word in model2.wv.vocab:
            #print('Dono hai')
            eng_vec = model2.wv[eng_word]
            hin_vec = model.wv[hin_key]
            sum = np.subtract(np.multiply(weight_vec, eng_vec), hin_vec)
            sum *= 2 #For differentiation
            weight_vec = np.subtract(weight_vec, alpha*(sum))
        #print(weight_vec)
pickle.dump(weight_vec,open('weight_vec_sys2.p','wb'))
