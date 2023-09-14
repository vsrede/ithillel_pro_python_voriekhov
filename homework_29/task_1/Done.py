import time
import os
import random
import string
import requests
from multiprocessing.pool import ThreadPool


def clear_img_folder():
    path = os.path.join(os.getcwd(), 'img')
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


class timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


workers = 256
DATA_SIZE = 10

with timer("Elapsed: {}s"):
    with ThreadPool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fetch_pic, input_data)

    clear_img_folder()


workers_list = [1, 2, 4, 8, 16, 32, 64, 256]
result_list = [4.39, 2.59, 1.82, 0.557,  0.008, 0.003, 0.011, 0.063]

