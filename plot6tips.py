# tips.csv로 요약 처리 후 시각화
import pandas as pd # 데이터 분석 및 조작을 위한 pandas 라이브러리 임포트
import matplotlib.pyplot as plt # 데이터 시각화를 위한 matplotlib.pyplot 라이브러리 임포트

# GitHub에 있는 'tips.csv' 파일을 URL을 통해 직접 읽어와 DataFrame으로 생성
tips = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tips.csv')
print(tips.info()) # DataFrame의 기본 정보(컬럼, Non-Null 개수, 데이터 타입 등) 출력

# 'sex' 컬럼의 이름을 'gender'로 변경
tips['gender'] = tips['sex']
del tips['sex'] # 기존 'sex' 컬럼 삭제
print(tips.head(3)) # 변경된 DataFrame의 상위 3개 행 출력

# tip 비율: 파생 변수 생성
# 'tip'을 'total_bill'로 나누어 'tip_pct'라는 새로운 컬럼 추가
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head(3)) # 'tip_pct' 컬럼이 추가된 DataFrame의 상위 3개 행 출력

# 'gender'와 'smoker' 컬럼을 기준으로 'tip_pct'를 그룹화
tip_pct_group = tips['tip_pct'].groupby([tips['gender'], tips['smoker']])

# 그룹별로 'tip_pct'의 합계, 최대값, 최소값 계산 및 출력
print(tip_pct_group.sum())
print(tip_pct_group.max())
print(tip_pct_group.min())

# 그룹별로 'tip_pct'의 기술 통계량(count, mean, std, min, max 등) 계산 및 출력
result = tip_pct_group.describe()
print(result)

print()
# agg() 함수를 사용하여 그룹별 합계, 평균, 분산 계산 및 출력
print(tip_pct_group.agg('sum'))
print(tip_pct_group.agg('mean'))
print(tip_pct_group.agg('var'))

# 사용자 정의 함수(myFunc) 정의
# 그룹 내의 최대값과 최소값의 차이를 반환하는 함수
def myFunc(group):
    diff = group.max() - group.min()
    return diff

# agg() 함수에 내장 함수와 사용자 정의 함수를 리스트 형태로 전달하여 한 번에 여러 연산 수행
# 'var', 'mean', 'max', 'min'는 내장 함수, myFunc는 사용자 정의 함수
result2 = tip_pct_group.agg(['var', 'mean', 'max', 'min', myFunc])
print(result2)

# 결과(result2)를 막대 그래프(barh: 가로 막대 그래프)로 시각화
# stacked=True로 설정하여 각 그룹의 결과가 누적되도록 함
result2.plot(kind='barh', title='agg func result', stacked=True)
plt.show() # 그래프 화면에 표시