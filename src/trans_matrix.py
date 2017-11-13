Init W = random()
import numpy as np
while 1:
    sum = 0
    for i in (1,no_of_eng_words):
        sum += np.norm(W*vec(eng_word) - vec(hin_word))
    sum *= 2
    sum *= summation(x)
    W = W + alpha*(sum)
    
    