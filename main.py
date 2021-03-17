# -*- coding: utf-8 -*-
import texthero as hero
import pandas as pd
from texthero import preprocessing
import matplotlib.pyplot as plt

df = pd.read_csv(
    #"https://github.com/jbesomi/texthero/raw/master/dataset/bbcsport.csv"
    "words.txt"
)
custom_pipeline = [preprocessing.fillna,
                   preprocessing.lowercase,
                   preprocessing.remove_digits,
                   preprocessing.remove_stopwords,
                   preprocessing.remove_whitespace,
                   preprocessing.remove_punctuation,
                   preprocessing.remove_diacritics]

df['clean'] = hero.clean(df['text'], custom_pipeline)
df['tfidf'] = hero.tfidf(df['clean'])
df['pca'] = hero.pca(df['tfidf'])
print(df['clean'])
#hero.scatterplot(df, col='pca', title='NLPCA')
topwords = hero.top_words(df['clean'])
hero.wordcloud(df['clean'], font_path='CN.ttf')
f = open('result.txt', 'w')
topwords.to_csv(f)
f.close()
#topwords.plot.bar(rot=90, title='Top words')
plt.show(block=True)

