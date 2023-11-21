import os
import pandas as pd
from ydata_profiling import ProfileReport

wine_quality_path = 'data/winequality.csv'

df = pd.read_csv(wine_quality_path)

profile = ProfileReport(df, title="Profiling Report")
profile_path = 'profiling/report.html'

if os.path.exists(profile_path):
    os.remove(profile_path)

profile.to_file(profile_path)