import random
import time
import multiprocessing
import plotly.graph_objects as go

DATA_SIZE = 1_000_000


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


def fill_data(n):
    lst = []
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


if __name__ == '__main__':
    time_work = []
    number_workers = []
    for workers in range(1, 9):
        with Timer() as timer:
            with multiprocessing.Pool(workers) as pool:
                input_data = [DATA_SIZE // workers for _ in range(workers)]
                pool.map(fill_data, input_data)
        number_workers.append(workers)
        elapsed_time = timer.get_elapsed_time()
        time_work.append(elapsed_time)
        print(f"workers {workers} done during {elapsed_time}s")
    fig = go.Figure(
        data=[go.Scatter(x=number_workers,
                         y=time_work, mode='lines+markers')],
        layout_title_text="A Figure Displayed with fig.show()"
    )
    fig.show()

# workers = [1, 2, 3, 4, 5, 6, 7, 8]
# result = [0.860, 0.614, 0.504, 0.478, 0.522, 0.553, 0.616, 0.604]
