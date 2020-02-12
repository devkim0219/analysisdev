'''
### iris.data info ###

caseno : 일련번호(1 ~ 150)
sepal length : 꽃받침의 길이
sepal width : 꽃받침의 너비
petal length : 꽃잎의 길이
petal width : 꽃잎의 너비
species : 꽃의 종류 (setosa / versicolor / virginica)
'''

import numpy as np
import pandas as pd
from perceptron import Perceptron
import pickle

def step1_get_data():
    
    # iris.data 파일에서 데이터를 읽어온다.
    df = pd.read_csv('./iris/iris.data', header=None)
    # print(df)

    # 꽃잎 데이터를 추출한다.
    X = df.iloc[0:100, [2, 3]].values
    # print(X)

    # 꽃 종류 데이터를 추출한다.
    y = df.iloc[0:100, 4].values
    y = np.where(y=='Iris-setosa', 1, -1)
    # print(y)

    return X, y

def step2_learning():
    ppn = Perceptron(eta=0.1)
    data = step1_get_data()

    X = data[0]
    y = data[1]

    # 학습
    ppn.fit(X, y)
    print(ppn.errors_)
    print(ppn.w_)

    # 학습된 객체를 저장
    # 학습이 완료된 객체를 파일로 저장
    with open('./iris/perceptron.dat', 'wb') as fp:
        pickle.dump(ppn, fp)
    
    print('학습 완료')

def step3_using():

    # 파일로부터 객체를 복원한다.
    with open('./iris/perceptron.dat', 'rb') as fp:
        ppn = pickle.load(fp)

    while True:
        a1 = input('꽃잎의 너비를 입력하세요 :')
        a2 = input('꽃잎의 길이를 입력하세요 :')

        X = np.array([float(a1), float(a2)])

        result = ppn.predict(X)

        if result == 1:
            print('결과 : Iris-setosa')
        
        else:
            print('결과 : Iris-versicolor')

# step1_get_data()
# step2_learning()
step3_using()