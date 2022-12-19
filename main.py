from datetime import datetime
import csv
# import json

# Task_1
class Logger:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.f = open(file_name, mode)

    def __enter__(self):
        self.f.write(f'{str(datetime.now())} {self.file_name} OPEN \n')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.write(( f'{str(datetime.now())} {self.file_name} CLOSE \n' ))
        self.f.close()

# Task_2
    @staticmethod
    def txt_in_csv(filetxt: str, filecsv: str):
        with open(filetxt) as filetxt:
            txt = []
            for line in filetxt.readlines():
                line = line.strip()
                txt.append(line.split(' '))

            with open(filecsv, 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(txt)


with Logger('loger.txt', 'a+') as loger:
    loger.read()

Logger.txt_in_csv('loger.txt', 'loger.csv')










