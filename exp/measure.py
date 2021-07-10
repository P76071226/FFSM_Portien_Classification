import time


class Measure:
    def __init__(self):
        self.times = list()
        self.corrects = list()

    def measure(self, func, *args, **kwargs):
        start_time = time.time()
        vals = func(*args, **kwargs)
        end_time = time.time()
        self.times.append(end_time - start_time)
        self.corrects.append(vals[0] == vals[1])

    def avg_time(self):
        return sum(self.times) / len(self.times)

    def acc(self):
        return sum(map(lambda x: 1 if x else 0, self.corrects)) / len(self.corrects)

    def clear(self):
        self.times.clear()
        self.corrects.clear()

    def show_report(self):
        print('Time spent: %f' % self.avg_time())
        print('Accuracy: %f' % self.acc())


if __name__ == '__main__':
    import random

    def test(a, b):
        time.sleep(random.randint(1, 5))
        return a, b

    m = Measure()
    m.measure(test, 1, 2)
    m.measure(test, 2, 2)
    m.measure(test, 3, 2)

    m.show_report()
