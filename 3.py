import os
from zipfile import ZipFile


def human_read_format(a):
    b = int(a)
    if b < 1024:
        return str(b) + "Б"
    else:
        b = round(b / 1024)
        if b < 1024:
            return str(b) + "КБ"
        else:
            b = round(b / 1024)
            if b < 1024:
                return str(b) + "МБ"
            else:
                b = round(b / 1024)
                return str(b) + "ГБ"


with ZipFile('input.zip') as myzip:
    a = (myzip.namelist())
    info = myzip.infolist()
    for i in range(len(a)):
        b = 0
        c = 0
        d = 0
        for u in range(i):
            if a[u] in a[i]:
                b += 2
                c = len(a[u])
        if info[i].orig_filename[-1].isalnum():
            print(b * ' ' + info[i].orig_filename[c:] + ' ' + human_read_format(os.path.getsize(info[i].orig_filename)))
        else:
            print(b * ' ' + info[i].orig_filename[c:-1] + ' ')
