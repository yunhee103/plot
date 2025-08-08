import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10)
"""
# #figure 구성 방법

# 1) matplotlib 스타일의 인터페이스
plt.figure()
plt.subplot(2,1,1)   #row, column, panel number
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))


plt.show()
# 2) 객체 지향 인터페이스
fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
"""


fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.hist(np.random.randn(10),bins=10, alpha=0.9) #도수분표포 , 구간수, 투명도
ax2.plot(np.random.randn(10))
plt.show()

#bar
data = [50, 80, 100, 70, 90]
plt.bar(range(len(data)), data)  # 세로막대그래프
plt.show()

loss = np.random.rand(len(data))
plt.barh(range(len(data)), data, xerr=loss, alpha=0.7)  # 가로막대그래프  , errorbar 
plt.show()

#pie
plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow', 'red', 'blue']) #추출양 
plt.show()
# 다양한 데이타 작업이 불가능 , 데이타 양이 적어야함

#boxplot : 사분위 등에 대한 데이터 분포 확인
plt.boxplot(data)  #최소 , 최대값, Q1,Q2,Q3   Q2 = 중앙값   많은 양에 대한 분포를 확인할때
plt.show()

#bubble chart    데이터의 양에 따라 원의 크기가 커짐
n = 30
np.random.seed(0)
x= np.random.rand(n)
y= np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (15 * np.random.rand(n)) **2
plt.scatter(x,y, c=color, s=scale)  #산포도
plt.show()

import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4),  # 정규분포를 따르는 난수 발생, 1000행 4열
                     index = pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))

# 누적 데이타
fdata = fdata.cumsum()
print(fdata.head(3))
plt.plot(fdata)
plt.show()

# matplotlib를 통해 시각화 시킴 
# -> pandas가 지원하는 plot
fdata.plot()
fdata.plot(kind='bar') 
fdata.plot(kind='box') 
plt.xlabel("time")
plt.ylabel("data")
plt.show()