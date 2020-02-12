# 학습용 데이터
from sklearn import datasets

# 데이터를 학습용과 테스트용으로 나눌 수 있는 함수
from sklearn.model_selection import train_test_split

# 데이터 표준화
from sklearn.preprocessing import StandardScaler

# 의사결정 나무를 위한 클래스
from sklearn.tree import DecisionTreeClassifier

# 그리드서치 클래스
from sklearn.model_selection import GridSearchCV

# 교차검증
# from sklearn.model_selection import KFold

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
    ml = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
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

def step2_learning2():
    X, y = step1_get_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)

    ml = DecisionTreeClassifier()

    parameters = {'max_depth':[1,2,3,4,5,6,7], 'min_samples_split':[2,3]}
    grid_ml = GridSearchCV(ml, param_grid=parameters, cv=3, refit=True)
    grid_ml.fit(X_train_std, y_train)

    # 학습 정확도를 확인
    print('GridSearchCV 최적 파라미터: ', grid_ml.best_params_)
    print('GridSearchCV 최적 정확도: {0:.4f}'.format(grid_ml.best_score_))

    estimator = grid_ml.best_estimator_
    X_test_std = sc.transform(X_test)
    y_pred = estimator.predict(X_test_std)

    print('테스트 데이터 세트 정확도: {0:.4f}'.format(accuracy_score(y_test, y_pred)))

    # 학습이 완료된 객체를 저장
    with open('./output/ml.dat', 'wb') as fp:
        pickle.dump(sc, fp)
        pickle.dump(grid_ml, fp)

    print('학습 완료')

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
# step2_learning2()
step3_using()