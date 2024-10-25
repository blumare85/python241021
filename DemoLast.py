import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 불러옵니다. 파일 경로를 실제 파일 경로로 바꿔주세요.
file_path = 'birthrate_20241025151504.xlsx'
data_df = pd.read_excel(file_path, sheet_name='데이터')

# 이후의 코드를 실행합니다.
years = data_df.columns[1:].astype(int)  # 연도 컬럼을 추출하고 정수형으로 변환
birth_counts = data_df.iloc[0, 1:]       # 출생아수(명)
fertility_rate = data_df.iloc[4, 1:]     # 합계출산율(명)


# Extract relevant columns for analysis
years = data_df.columns[1:].astype(int)  # Extract year columns and convert to integer type
birth_counts = data_df.iloc[0, 1:]       # 출생아수(명)
fertility_rate = data_df.iloc[4, 1:]     # 합계출산율(명)
natural_increase = data_df.iloc[1, 1:]   # 자연증가건수(명)

# Plotting trends for birth counts, fertility rate, and natural increase
plt.figure(figsize=(15, 8))

# Subplot 1: Birth Counts Over Time
plt.subplot(3, 1, 1)
plt.plot(years, birth_counts, label='Birth Counts', color='blue')
plt.title('Birth Counts in Korea (1970-2023)')
plt.ylabel('Number of Births')
plt.grid(True)

# Subplot 2: Total Fertility Rate Over Time
plt.subplot(3, 1, 2)
plt.plot(years, fertility_rate, label='Total Fertility Rate', color='green')
plt.title('Total Fertility Rate in Korea (1970-2023)')
plt.ylabel('Fertility Rate')
plt.grid(True)

# Subplot 3: Natural Increase in Population Over Time
plt.subplot(3, 1, 3)
plt.plot(years, natural_increase, label='Natural Increase', color='red')
plt.title('Natural Increase in Population in Korea (1970-2023)')
plt.xlabel('Year')
plt.ylabel('Natural Increase (people)')
plt.grid(True)

plt.tight_layout()
plt.show()
