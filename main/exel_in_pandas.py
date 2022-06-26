import pandas as pd
import os


def name_table():
    dirname = r'test/'
    files = os.listdir(dirname)
    last_elements = max(files)
    element1, element2 = last_elements.split(sep='.')
    element1 = int(element1) + 1
    name0 = str(element1) + '.' + element2
    name1 = last_elements
    return [name0, name1]


def conver_xlsx():
    new_name = name_table()[1].split(sep='.')[0]
    data = pd.read_excel(r'test/' + name_table()[1])
    itog = data.to_html(r'result/' + new_name + '.txt', index=None, encoding='utf-8', na_rep='')
    dirname = r'result/'
    files = os.listdir(dirname)
    last_elements = max(files)
    f = open(new_name + '.txt', 'r', encoding="utf-8")
    gg = f.read()
    return gg

if __name__ == '__main__':
    print(name_table())
    print(conver_xlsx())
