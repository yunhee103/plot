# 자전거 공유 시스템(워싱턴 D.C) 관련 파일로 시각화 
import pandas as pd # 데이터 분석 및 조작을 위한 pandas 라이브러리 임포트
import numpy as np # 수치 연산을 위한 라이브러리 (여기서는 직접 사용되지 않음)
import matplotlib.pyplot as plt # 데이터 시각화를 위한 matplotlib.pyplot 임포트
import seaborn as sns # matplotlib 기반의 시각화 라이브러리
plt.rc('font', family='malgun gothic') # matplotlib에서 한글 폰트(맑은 고딕) 사용 설정
plt.rcParams['axes.unicode_minus'] = False # 그래프에서 마이너스 부호가 깨지지 않도록 설정

plt.style.use('ggplot') # ggplot 스타일로 그래프 테마 설정

# 데이터 수집 후 가공(EDA) - train.csv
# 'train.csv' 파일을 읽어와 DataFrame으로 생성.
# parse_dates=['datetime']을 통해 'datetime' 컬럼을 날짜/시간 형식으로 바로 변환
train = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv', parse_dates=['datetime'])
print(train.shape) # DataFrame의 행(row)과 열(column) 개수 출력 (10886, 12)
print(train.columns) # 모든 컬럼 이름 출력
print(train.info()) # 각 컬럼의 구조, 데이터 타입, Non-Null 값 개수 등의 정보 출력
print(train.head(3)) # DataFrame의 상위 3개 행 출력
pd.set_option('display.max_columns', 500) # 출력 시 컬럼 생략 없이 모두 보이도록 설정
# print(train.describe()) # 숫자형 컬럼에 대한 기술 통계량 출력
print(train.temp.describe()) # 'temp' 컬럼에 대한 기술 통계량 출력
print(train.isnull().sum()) # 각 컬럼의 결측치(null) 개수 합계 출력

# 결측치 확인용 시각화 모듈 (missingno)
import missingno as msno # missingno 라이브러리 임포트
# msno.matrix(train, figsize=(12, 5)) # 결측치 위치를 시각화하는 매트릭스 그래프
# plt.show()
# msno.bar(train) # 결측치 개수를 바 그래프로 시각화
# plt.show()

# 'datetime' 컬럼에서 연, 월, 일, 시, 분, 초 데이터를 추출하여 새로운 컬럼으로 추가
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second
print(train.columns) # 새로운 컬럼이 추가된 컬럼 목록 출력
print(train.head(1)) # 변경된 DataFrame의 상위 1개 행 출력

# 연/월/일/시별 자전거 대여량 시각화 (서브플롯)
# 1행 4열의 서브플롯 생성
figure, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)
figure.set_size_inches(15, 5) # 전체 그림(figure) 크기 설정
# Seaborn의 barplot을 사용하여 각 서브플롯에 연도, 월, 일, 시간별 'count'(대여량) 시각화
sns.barplot(data=train, x='year', y='count', ax=ax1)
sns.barplot(data=train, x='month', y='count', ax=ax2)
sns.barplot(data=train, x='day', y='count', ax=ax3)
sns.barplot(data=train, x='hour', y='count', ax=ax4)
# 각 서브플롯에 라벨과 제목 설정
ax1.set(ylabel='건수', title='연도별 대여량')
ax2.set(ylabel='월', title='월별 대여량')
ax3.set(ylabel='일', title='일별 대여량')
ax4.set(ylabel='시', title='시간별 대여량')
plt.show() # 그래프 화면에 표시

# Boxplot으로 시각화 - 대여량 - 계절별, 시간별, 근무일 여부에 따른 대여량
# 2행 2열의 서브플롯 생성
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12, 10) # 전체 그림(figure) 크기 설정
# 'count' 컬럼에 대한 boxplot 시각화
sns.boxplot(data=train, y='count', orient='v', ax=axes[0][0])
# 'season' 컬럼에 따른 'count'의 boxplot 시각화
sns.boxplot(data=train, y='count', x='season', orient='v', ax=axes[0][1])
# 'hour' 컬럼에 따른 'count'의 boxplot 시각화
sns.boxplot(data=train, y='count', x='hour', orient='v', ax=axes[1][0])
# 'workingday' 컬럼에 따른 'count'의 boxplot 시각화
sns.boxplot(data=train, y='count', x='workingday', orient='v', ax=axes[1][1])
# 각 서브플롯에 라벨과 제목 설정
axes[0][0].set(ylabel='건수', title='대여량')
axes[0][1].set(ylabel='계절별', title='계절별 대여량')
axes[1][0].set(ylabel='시간별', title='시간별 대여량')
axes[1][1].set(ylabel='근무일', title='근무일 여부에 따른 대여량')
plt.show() # 그래프 화면에 표시