from measure import Measure
from workflow import flow
import os
import csv

DATA_PATH = 'db_formate'

if __name__ == '__main__':
    csv_row = [['class', 'time', 'acc']]
    for cls_ in os.listdir(DATA_PATH):
        m = Measure()
        for dat in os.listdir(os.path.join(DATA_PATH, cls_)):
            m.measure(flow, os.path.join(DATA_PATH, cls_, dat))
        csv_row.append([cls_, m.avg_time, m.acc])
    with open('exp_result.csv', 'w') as csv_w:
        csv_writer = csv.writer(csv_w)
        csv_writer.writerows(csv_row)
