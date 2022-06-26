import pandas as pd
import os


def name_table():
    dirname = r'test/'
    files = os.listdir(dirname)
    last_elements = max(files)
    element1, element2 = last_elements.split(sep='.')
    element1_1 = str(int(element1) +1)
    name0 = element1_1.zfill(4) + '.' + element2
    name1 = last_elements
    name3 = element1 + '.txt'
    return [name0, name1, name3]


def conver_xlsx():
    try:
        data = pd.read_excel(r'test/' + name_table()[1])
        itog = data.to_html(r'result/' + name_table()[2], index=None, encoding='utf-8', na_rep='')
        f = open(r'result/' + name_table()[2], 'r', encoding="utf-8")
        gg = f.read()
    except Exception:
        gg = "С Вашим документом что-то не так"
    return gg

if __name__ == '__main__':
    print(name_table())
    print(conver_xlsx())
