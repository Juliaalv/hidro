import pandas as pd
import numpy as np
import sweetviz as sv
import pandas_profiling as pp

df = pd.read_csv('data/65925770_Vazoes.csv', encoding='cp1252', sep=';', skiprows=15)
report = sv.analyze(df)
report.show_html('report.html', layout='widescreen', scale=1)