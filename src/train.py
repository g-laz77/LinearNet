import sys, gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#Supply as command line args
fname = sys.argv[1]


#If input is in a large file , use this!

class LoadFile(object):
    #Returns an iterator to iterate on...
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for line in open('./'+self.filename):
            yield line.split()


sentences = LoadFile(fname)
model = gensim.models.Word2Vec(sentences, min_count = 4, size = 300)

model.save('./models/en')


