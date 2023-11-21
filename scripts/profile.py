import numpy as np
import os
import pandas as pd
from ydata_profiling import ProfileReport

df_red = pd.read_csv('data/winequality-red.csv')
df_wht =  pd.read_csv('data/winequality-white.csv')

df = pd.concat([df_red, df_wht])

if os.path.exists('data/winequality.csv'):
    os.remove('data/winequality.csv')
df.to_csv('data/winequality.csv')

profile = ProfileReport(df, title="Profiling Report")
if os.path.exists('profiling/report.html'):
    os.remove('profiling/report.html')
    profile.to_file("profiling/report.html")