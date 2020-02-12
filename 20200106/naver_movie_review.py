import time
import requests
import csv
from bs4 import BeautifulSoup

def time_function(f):
    '''함수 사용 시간을 측정하기 위한 데코레이터
    Args
        f (function) : 함수
    Return
        function : 함수 포인터
    '''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time: {}".format(f.__name__, args[1], end_time))

        return result

    return wrapper

# @time_function
def r_selector(page):
    with open('./naver_movie_review.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames = ['text', 'star']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()

        for i in range(1, page + 1, 1):
            r = requests.get('https://movie.naver.com/movie/point/af/list.nhn' + '?&page=' + str(i))
            bs = BeautifulSoup(r.text, 'lxml')

            list_records = []

            # BeautifulSoup 의 select 함수 사용
            # li 태그의 클래스명이 ah_item 인 요소 하위의 span 태그이며 클래스명이 ah_k 인 요소 선택
            tables = bs.select('table.list_netizen > tbody > tr')

            for tr in tables:
                record = {}

                tds = tr.select('td')
                # print(tds)

                if len(tds) != 3:
                    continue

                text = tds[1].text.split('\n')[5]
                star = tds[1].select('div.list_netizen_score > em')[0].text
                # print(text)
                # print(star)

                record.update({'text': text})
                record.update({'star': star})
                # print(record)

                list_records.append(record)
                # print(list_records)

            writer.writerows(list_records)

r_selector(1000)