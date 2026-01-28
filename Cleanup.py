import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'data\air_brum_bris.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df[['nox', 'no2', 'no']] = df[['nox', 'no2', 'no']].interpolate(method='time', limit_direction='both')


print(df[['nox', 'no2', 'no']].isna().sum())

print(df.columns)

df.to_csv('air_brum_bris_cleaned_dates', index=True)

#Big graphs, needs some filters

for site in df['site'].unique():
    site_df = df[df['site'] == site]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(site_df.index, site_df['nox'], label='NOx', linestyle='-')
    ax.plot(site_df.index, site_df['no2'], label='NO2', linestyle='-')
    ax.plot(site_df.index, site_df['o3'], label='O3', linestyle='-')

    ax.set_title(f'NOx, NO2, and O3 Over Time — Site: {site}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Concentration')
    ax.legend()

    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()

df[df['site'] == df['site'].iloc[0]]['nox'].plot()
plt.show()
