from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle
from time import time
import pandas as pd
from konlpy.tag import Okt
from soynlp.tokenizer import MaxScoreTokenizer

okt = Okt()
# soynlp = MaxScoreTokenizer()

def tokenizer(text):
    return okt.morphs(text)
    # return okt.nouns(text)
    # return soynlp.tokenize(text)

def step3_learning():

    # 데이터를 읽어옴
    train_df = pd.read_csv('./output/movie_train_data.csv')
    test_df = pd.read_csv('./output/movie_test_data.csv')

    X_train = train_df['text'].astype('str').tolist()
    y_train = train_df['star'].astype('str').tolist()

    X_test = test_df['text'].astype('str').tolist()
    y_test = test_df['star'].astype('str').tolist()

    # 학습을 위한 객체 생성
    # vect = CountVectorizer()

    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0)
    pipe = Pipeline([('tfidf', tfidf), ('clf', logistic)])
    # param_grid = [{'clf_C': [1, 3.5, 4.5, 5.5, 10]}]
    # grid_cv = GridSearchCV(pipe, param_grid=param_grid, cv=3, scoring='accuracy', verbose=1)

    # 학습
    stime = time()

    print('학습 시작')

    pipe.fit(X_train, y_train)
    # grid_cv.fit(X_train, y_train)
    
    print('학습 종료')

    etime = time()

    print('총 학습 시간 : %d' % (etime - stime))

    # 학습 정확도 측정
    y_pred = pipe.predict(X_test)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 객체 저장
    with open('./output/pipe.dat', 'wb') as fp:
        pickle.dump(pipe, fp)