# region_year['변동액'] = (region_year['2018'] - region_year['2015']).astype(int)
# 평당분양가격 : pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3

import warnings
warnings.filterwarnings('ignore')

import statsmodels.api as sm
from plotnine import *
import plotnine
import missingno as msno
import pandas as pd
import numpy as np
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 마이너스 폰트 깨짐 현상 수정
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
path = '/usr/share/fonts/truetype/naver-d2coding/D2Coding-Ver1.3.2-20180524-all.ttc'
font_name = fm.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

# csv 파일 읽어오기
pre_sale = pd.read_csv('./data6/pre_sale_2019_11.csv', encoding='EUC-KR')
# print(pre_sale.shape)
# print(pre_sale.head())

# 결측치 보기
msno.matrix(pre_sale, figsize=(18, 6))
print(pre_sale.isnull().sum())

print(pre_sale.head(), '\n')
print(pre_sale.info())

pre_sale_price = pre_sale['분양가격(㎡)']

# 연도와 월은 카테고리 형태의 데이터이기 때문에 스트링 형태로 변경
pre_sale['연도'] = pre_sale['연도'].astype(str)
pre_sale['월'] = pre_sale['월'].astype(str)

# 분양가격의 타입을 숫자로 변경
pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')

# 평당 분양가격 계산
pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3

print(pre_sale.info())
print(pre_sale.isnull().sum())
print(pre_sale.describe())

pre_sale_2017 = pre_sale.loc[pre_sale['연도'] == '2017']
print(pre_sale_2017.shape)
print(pre_sale['규모구분'].value_counts())

pd.options.display.float_format = '{:, .0f}'.format

# plotnine 라이브러리
# (ggplot(shop_201709_01[:1000])
# + aes(x='경도', y='위도', color='구군')
# + geom_point(alpha=0.2, size=0.2)
# + theme(text=element_text(fontproperties=font))
# + scale_fill_gradient(low='blue', high='green')
# )