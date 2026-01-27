import pandas as pd

df = pd.read_csv(r'air_brum_bris.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df[['nox', 'no2', 'no']] = df[['nox', 'no2', 'no']].interpolate(method='time', limit_direction='both')


print(df[['nox', 'no2', 'no']].isna().sum())
