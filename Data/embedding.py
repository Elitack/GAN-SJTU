from gensim.models import Word2Vec
import sys
import numpy as np
import graph

data_dir = './'


    
# stock select: 2016,2015...
# season_select: all, year
# emb:2012, 2013...

def embedding(input_name, output_name):
    weight_matrix = np.load(input_name)
    G = graph.Graph(weight_matrix)

    walks = G.simulate_walks(10, 10)
    walks = [list(map(str, walk)) for walk in walks]
    
    model = Word2Vec(walks, size=32, window=6, min_count=0, sg=1, workers=2, iter=30)
    model.wv.save_word2vec_format(data_dir + '{}.emb'.format(output_name))
        
    # embedding_cluster('{}_{}_{}'.format(
        # str(emb[0])+str(emb[1]), str(stock_select[0])+str(stock_indexselect[1]), season_select))
    
if __name__ == '__main__':
    embedding('WeightMatrix_2014-01-01_2016-01-01.npy', 'Embedding_2014-01-01_2016-01-01')