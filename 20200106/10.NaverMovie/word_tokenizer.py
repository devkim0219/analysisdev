from konlpy.tag import *
import pandas as pd
from soynlp.noun import LRNounExtractor

okt = Okt()

def tokenizer_morphs(text):
    return okt.morphs(text)

def tokenizer_nouns(text):
    # noun_extractor = LRNounExtractor()
    # nouns = noun_extractor.train_extract(text)
    # print(nouns)

    # return nouns
    return okt.nouns(text)

def word_tokenizer():
    train_df = pd.read_csv('./output/movie_train_data.csv')
    train_df['text_token'] = train_df['text'].apply(tokenizer_nouns)
    print(train_df['text_token'])