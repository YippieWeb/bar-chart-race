import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('./2020-championship.csv')
df = df.set_index('race')

bcr.bar_chart_race(
    df=df, 
    filename='2020_motoGP_championship_race.mp4',
    title='2020 MotoGP Championship Race', 
    orientation='h', 
    sort='desc', 
    n_bars=10, 
    steps_per_period=40, 
    period_length=2000
)