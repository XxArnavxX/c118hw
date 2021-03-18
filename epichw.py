  
import pandas as pd  
import plotly.figure_factory as f

re = pd.read_csv('./data4.csv')
fig = f.create_distplot([re["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()