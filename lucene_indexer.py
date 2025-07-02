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
        tokens= StandardAnalyzer().tokenStream("field", movie)
        term_attr = tokens.addAttribute(CharTermAttribute.class_)
        print_tokens(tokens,term_attr)