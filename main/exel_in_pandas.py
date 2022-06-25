import pandas as pd

data = pd.read_excel(r"test\test.xlsx")
itog = data.to_html(r"result\001.txt", index=None, encoding='utf-8', na_rep='')

