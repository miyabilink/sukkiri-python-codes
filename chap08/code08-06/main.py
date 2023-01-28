import pandas as pd
df = pd.read_csv('curry.csv', encoding='Shift_JIS')
df['month'] = pd.to_datetime(df['時間軸(月次)'], format='%Y年%m月').dt.month
df = df.groupby('month').mean()
df.mean(axis=1)
%matplotlib inline
df.mean(axis=1).plot()  # Pandasがmatplotlibを使って可視化する