#matplotlib 는 플로팅 모듈, 다양한 그래프 지원 함수 지원

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic') #음수는 한글 글꼴을 쓰면 깨짐 
plt.rcParams['axes.unicode_minus'] = False #  음수 지원
"""
x = ['서울', '인천', '수원']
y = [5,3,7]
plt.xlim([-1,3])  # x 범위 값
plt.ylim([0,10])  # y 범위 값

plt.plot(x, y)
plt.yticks(list(range(0,10,3)))
plt.show() # 창을 띄어주고 figure 흐름을 일시정지하는 것
# jupyer notebook 에서는 %matplotlib inline 하면 plt.show() 없어도 됨

data = np.arange(1,11,2)   #  1부터 11 미만까지 2씩 증가하는 숫자 배열을 생성
print(data)   #[1 3 5 7 9] 구간 4
plt.plot(data)
x = [0,1,2,3,4]
for a, b in zip(x, data):  #리스트를 묶어서 튜플 형태 
    plt.text(a, b, str(b))
plt.show()



plt.plot(data)
plt.plot(data, data, 'r')  # r 선 색깔
for a, b in zip(data, data):  #기울기 1의 직선
    plt.text(a, b, str(b))
plt.show()

#sin 곡선
x = np.arange(10)
y = np.sin(x)
print(x,y)

plt.plot(x, y)
# plt.plot(x, y, 'bo')  #스타일 지정  o 표시
#plt.plot(x, y, 'r+')  #스타일 지정  + 표시 
#plt.plot(x, y, 'go--', linewidth=2, markersize=12)  #스타일 지정 , 선두께 2   , - (solid line), --(dashed line)    , color='b'  c='b;', lw=2, marker='o'
plt.show()
"""
# 홀드 명령 : 하나의 영역에 두개 이상의 그래프 표시
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10, 5)) #너비와 높이 사이즈
plt.plot(x, y_sin, 'r')
plt.plot(x, y_cos)
plt.xlabel('X축')
plt.ylabel('Y축')
plt.title('제목')
plt.legend(['sine','cosine']) # 범례창 
plt.show()

# 산점도 
plt.figure(figsize=(10, 5)) #너비와 높이 사이즈
plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)      # 산점도 , => 홀드 기능
plt.xlabel('X축')
plt.ylabel('Y축')
plt.title('제목')
plt.legend(['sine','cosine']) # 범례창 
plt.show()

# Subplot : figure를 여러 개 선언 /// 영역을 나눌 수도 있음 

plt.subplot(2,1,1)
plt.plot(x,y_sin)


plt.title('사인')

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('코사인')

plt.show()

print()
irum = ['a','b','c','d','e']
kor = [80,50,70,70,90]
eng = [60,70,80,70,40]
plt.plot(irum,kor,'ro-')
plt.plot(irum,eng,'gs-')
plt.ylim([0,100])     
plt.legend(['국어','영어'], loc=2) #범례 위치 시계 반대방향   loc = 'best'   ->최적의 위치를 잡아줌
plt.grid(True)
fig = plt.gcf()
plt.show()
fig.savefig('result.png')   #'파일명' 이미지 저장

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('result.png')
plt.imshow(img)
plt.show()