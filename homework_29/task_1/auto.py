import time
import os
import random
import string
import requests
from multiprocessing.pool import ThreadPool

import plotly.graph_objects as go


def clear_img_folder():
    """Clean img directory after download images"""
    path = os.path.join(os.getcwd(), 'img')
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.end_time = time.time()

    def get_elapsed_time(self):
        return self.end_time - self.start_time


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


DATA_SIZE = 150

number_workers = []
time_work = []

for workers in range(10, 101, 10):
    with Timer() as timer:
        with ThreadPool(workers) as pool:
            input_data = [DATA_SIZE // workers for _ in range(workers)]
            pool.map(fetch_pic, input_data)
    number_workers.append(workers)
    elapsed_time = round(timer.get_elapsed_time(), 2)
    time_work.append(elapsed_time)
    clear_img_folder()
    time.sleep(1)
    print(f"number {workers} done")

fig = go.Figure(
    data=[go.Scatter(x=number_workers,
                     y=time_work, mode='lines+markers')],
)
fig.show()
