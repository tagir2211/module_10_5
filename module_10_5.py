import multiprocessing
import os
from datetime import datetime

adres = os.getcwd()
all_data = []


def read_info(name):
    local: all_data
    with open(name, 'r') as file:
        for _ in file:
            all_data.append(file.readline())


files = [f'{adres}/file {i}.txt' for i in range(1, 4)]

start = datetime.now()
# линейный подход Время чтения файлов: 0:00:06.017418
for _ in range(1, 5):
    for file in files:
        read_info(file)
end = datetime.now()
print(f'Время чтения файлов: {(end - start) / 5}')
if __name__ == '__main__':
    all_data = []
    # мультипроцессорный подход Время чтения файлов: 0:00:02.314001
    start = datetime.now()
    for _ in range(1, 5):
        with multiprocessing.Pool(processes=4) as pool:
            pool.map(read_info, files)
    end = datetime.now()
    print(f'Время чтения файлов: {(end - start) / 5}')
