import csv
import pandas as pd
import nltk
import lucene
import lucene
lucene.initVM()
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.analysis.tokenattributes import CharTermAttribute






porter=nltk.PorterStemmer()
reader=None
path_to_file='./wiki_movie_plots.csv'

with open('./wiki_movie_plots.csv',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    data=list(reader)
    

def make_inverted_index(path_to_file):
    csv_file=pd.read_csv(path_to_file)
    
    for movie in csv_file['Plot']:
        
        words=nltk.word_tokenize(movie)
        lower_case_tokens=[w.lower() for w in words if w.isalnum()]
        # print(lower_case_tokens)
        pos_tagged_tokens=nltk.pos_tag(words)

        stemmd_tokens=[porter.stem(w) for w in lower_case_tokens]
        print(stemmd_tokens)
        

# make_inverted_index(path_to_file)


def make_inverted_index_using_lucene(path_to_file):


    csv_file=pd.read_csv(path_to_file)
    
    for movie in csv_file['Plot']:
        tokens= WhitespaceAnalyzer().tokenStream("field", movie)
        term_attr = tokens.addAttribute(CharTermAttribute.class_)
        print_tokens(tokens,term_attr)
    

    


   


def print_tokens(tokens,term_attr):
    tokens.reset()
    while tokens.incrementToken():
        print(term_attr.toString())

make_inverted_index_using_lucene(path_to_file)

