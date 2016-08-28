from math import sqrt


def s_func(query, article):
    return sum(query[x] * article[x] for x in range(0, len(article)))


def p_func(query, article):
    return sqrt(sum(pow(query[x] * article[x], 2) for x in range(0, len(article))))


def sum_vectors(query, corpus, fn):
    ard = []
    for article in corpus:
        similarity = fn(query, article)
        ard.append(similarity)
    return ard


query = [1,3,2,1,2,1,1]
corpus = [[7,0,2,1,0,0,1],[1,7,0,0,2,0,1],[1,0,0,0,7,1,2],[0,2,0,0,7,1,1]]

print("Traditional is> {}".format(sum_vectors(query, corpus, s_func)), end='\n\n')
print("Normalized is> {}".format(sum_vectors(query, corpus, p_func)), end='\n\n')
