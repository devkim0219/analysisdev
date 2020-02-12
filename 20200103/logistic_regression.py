# 학습용 데이터
from sklearn import datasets

# 데이터를 학습용과 테스트용으로 나눌 수 있는 함수
from sklearn.model_selection import train_test_split

# 데이터 표준화
from sklearn.preprocessing import StandardScaler

# Percenptron 머신러닝을 위한 클래스
from sklearn.linear_model import Perceptron

# 로지스틱 회귀를 위한 클래스
from sklearn.linear_model import LogisticRegression

# 정확도 계산을 위한 함수
from sklearn.metrics import accuracy_score

import pickle
import numpy as np

names = None

def step1_get_data():

    # 아이리스 데이터 추출
    iris = datasets.load_iris()
    # print(iris)

    # 꽃 정보 데이터 추출
    X = iris.data[:150, [2, 3]]     # 꽃잎 정보
    y = iris.target[:150]           # 꽃 종류
    names = iris.target_names[:3]   # 꽃 이름
    
    print(X[0])
    print(y[0])
    print(names[0])

    return X, y

def step2_learning():
    X, y = step1_get_data()

    # 학습 데이터와 테스트 데이터로 나눔
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # 표준화 작업 : 데이터들을 표준 정규분포로 변환하여
    #              적은 학습 횟수와 높은 학습 정확도를 갖기 위해 하는 작업
    sc = StandardScaler()

    # 데이터 표준화
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)

    # 학습
    ml = LogisticRegression(C=1000.0, random_state=0)
    ml.fit(X_train_std, y_train)

    # 학습 정확도를 확인
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)

    print('학습 정확도 : ', accuracy_score(y_test, y_pred))

    # 학습이 완료된 객체를 저장
    with open('./output/ml.dat', 'wb') as fp:
        pickle.dump(sc, fp)
        pickle.dump(ml, fp)

    print('학습 완료')

    # 시각화를 위한 작업
    # X_combined_std = np.vstack((X_train_std, X_test_std))
    # y_combined_std = np.hstack((y_train, y_test))
    # plot_decision_region(X=X_combined_std, y=y_combined_std, classifier=ml, test_idx=range(70, 100), title='perceptron')

def step3_using():

    # 학습이 완료된 객체를 복원한다.
    with open('./output/ml.dat', 'rb') as fp:
        sc = pickle.load(fp)
        ml = pickle.load(fp)

    X = [
        [1.4, 0.2], [1.3, 0.2], [1.5, 0.2],
        [4.5, 1.5], [4.1, 1.0], [4.5, 1.5],
        [5.2, 2.0], [5.4, 2.3], [5.1, 1.8]
    ]
    
    X_std = sc.transform(X)

    # 결과를 추출한다.
    y_pred = ml.predict(X_std)

    for value in y_pred:
        if value == 0:
            print('Iris-setosa')
        
        elif value == 1:
            print('Iris-versicolor')
        
        elif value == 2:
            print('Iris-virginica')

# step1_get_data()
# step2_learning()
step3_using()