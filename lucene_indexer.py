import csv
import pandas as pd
import nltk
import lucene
import lucene
import pickle

lucene.initVM()
from org.apache.lucene.analysis.standard import StandardAnalyzer

from org.apache.lucene.analysis.tokenattributes import CharTermAttribute

from java.io import StringReader

analyzer=StandardAnalyzer()

test="Lucene is a library"

stream=analyzer.tokenStream(None,StringReader(test))

stream.reset()
tokens=[]
while stream.incrementToken():
    tokens.append(stream.getAttribute(CharTermAttribute.class_).toString())
print(tokens)

def make_inverted_index_using_lucene(path_to_file):


    csv_file=pd.read_csv(path_to_file)
    
    for movie in csv_file['Plot']:
        stream= StandardAnalyzer().tokenStream("field", StringReader(movie));
        stream.reset()
        while stream.incrementToken():
            # term_attr = tokens.addAttribute(CharTermAttribute.class_)
            tokens.append(stream.getAttribute(CharTermAttribute.class_).toString())
            print(tokens)

make_inverted_index_using_lucene("./wiki_movie_plots.csv")