#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
from queue import Queue

# Все фотографии добавляем в очередь c фотографиями для обработки
queue_photos = Queue()

# Заполняем очередь заданиями
for photo_name_file in os.listdir('Source'):
    queue_photos.put(photo_name_file)


class Worker:
    """
    Класс-обертка над процессом обработчиком фотографий
    """
    def __init__(self):
        self.process = None

    def run(self, queue):
        if self.process is not None and self.process.returncode is not None:  # если экземпляр процесса не был создан или был создан, но он занят
            return
        if queue.empty():  # если очередь с фотографиями уже пуста, то ничего не делать
            return
        new_photo = queue.get()
        if new_photo is not None:
            result_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "Result", new_photo))
            source_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "Source", new_photo))
            self.process = subprocess.Popen(["convert.exe", source_file, "-resize", "200", result_file])
            print(str(self.process.pid) + " in " + result_file)  # выводит pid процесса, который обработал фотографию

# Создадим массив из 4 процесов
workers = [Worker(), Worker(), Worker(), Worker()]

while not queue_photos.empty():  # пока очередь не пуста
    for worker in workers:
        worker.run(queue_photos)

# Завершение всех процессов
for worker in workers:
    worker.process.kill()
print("Готово! Все 4 процесса обработали очередь фотографий!")





