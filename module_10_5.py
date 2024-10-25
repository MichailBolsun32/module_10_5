import multiprocessing
from datetime import datetime
#Создайте функцию read_info(name), где name - название файла. Функция должна:
    # Создавать локальный список all_data.
    # Открывать файл name для чтения.
    # Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
    # Во время считывания добавлять каждую строку в список all_data.

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                return
            else:
                all_data.append(line)

#  1. Создайте список названий файлов в соответствии с названиями файлов архива.
#  2. Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
#  3. Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
#     контекстный менеджер with и объект Pool. Для вызова функции используйте метод map,
#     передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.

names = [f'file {i}.txt' for i in range(1, 5)]
# start = datetime.now()
#
# for name in names:
#     read_info(name)
#
# end = datetime.now()
#
# print(end - start)

# 0:00:06.996758
if __name__ == '__main__':
    start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool: # launched 4 processes
        pool.map(read_info, names) # calculations into in 'names' processes

    end = datetime.now()
    print(end - start)

# 0:00:02.882271