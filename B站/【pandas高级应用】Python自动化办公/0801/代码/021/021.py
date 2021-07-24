import pandas as pd

pd.options.display.max_columns = 999
videos = pd.read_excel('C:/Temp/Videos.xlsx', index_col='Month')
# table = videos.transpose()
table = videos.T
print(table)
