import matplotlib.pyplot as plt
import pandas as pd

# 데이터
data = {
    '1분기': [500, 690, 1100, 1500, 1990, 1020],
    '2분기': [450, 700, 1030, 1650, 2020, 1600],
    '3분기': [520, 820, 1200, 1700, 2300, 2200],
    '4분기': [610, 900, 1380, 1850, 2420, 2550]
}

index = [2015, 2016, 2017, 2018, 2019, 2020]

# DataFrame 생성
df = pd.DataFrame(data, index=index)

# 라인 플롯 그리기
df.plot(kind='line', marker='o')
plt.title('연도별 분기별 판매량')
plt.xlabel('연도')
plt.ylabel('판매량')
plt.grid(True)
plt.legend(loc='best')
plt.show()