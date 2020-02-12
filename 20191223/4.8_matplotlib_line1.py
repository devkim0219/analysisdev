import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rc

# excel data를 dataframe으로 변환
df = pd.read_excel('./data4/시도별 전출입 인구수.xlsx', fillna=0, header=0)

# 누락값을 앞 데이터로 채움 (엑셀 양식 병합부분) -> 데이터의 특성에 따라 누락값 처리 방법은 다름
df = df.fillna(method='ffill')

# 부산에서 다른지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '부산광역시') & (df['전입지별'] != '서울특별시')
df_busan = df[mask]

# 방법 3가지 => 전출지별 행 없애기
df_busan = df_busan.drop(['전출지별'], axis=1)    # axis=1은 column
df_busan.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_busan.set_index('전입지', inplace=True)
df_busan.head()

# 부산에서 서울로 이동한 인구 데이터 값만 선택
sr_one = df_busan.loc['부산광역시']  # type이 series로 바뀜

# xy 축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values) # column이 아니라 index로 plot 생성(type: series)

# 판다스 객체를 plot 함수에입력
# plt.plot(sr_one)

# font_name = fm.FontProperties(fname="./data4/malgun.ttf").get_name()
# rc('font', family=font_name)

fm._rebuild()
[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=path, size=15)

# 차트 제목 추가
plt.title('부산 -> 서울 인구 이동', fontproperties=fontprop)

# 축 이름 추가
plt.xlabel('기간', fontproperties=fontprop)
plt.ylabel('이동 인구수', fontproperties=fontprop)

# 변경사항 저장하고 그래프 출력
plt.show()