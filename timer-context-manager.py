import time


class Timer:

    # The return self is mandatory since the return of the __enter__ is
    # passed to the target variables after the as
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args, **kwargs):
        self.end = time.perf_counter()
        self.elapsed_time = self.end - self.start

    def __str__(self):
        return f"Elapsed time: {self.elapsed_time:3.2f}s"


if __name__ == "__main__":

    with Timer() as timer:
        time.sleep(0.54)

    print(timer)
