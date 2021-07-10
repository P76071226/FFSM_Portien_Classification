from measure import Measure
from workflow import flow
import os
import csv

DATA_PATH = 'db_formate'
OUTPUT_FILE = 'exp_result.csv'

if __name__ == '__main__':
    csv_row = [['class', 'time', 'acc']]
    for cls_ in os.listdir(DATA_PATH):
        m = Measure()
        for dat in os.listdir(os.path.join(DATA_PATH, cls_)):
            print('Classifying %s ...' % os.path.join(DATA_PATH, cls_, dat))
            res = m.measure(flow, os.path.join(DATA_PATH, cls_, dat))
            print('<Result>\nP: %s\nT: %s\n' % res)
        csv_row.append([cls_, m.avg_time(), m.acc()])
    with open(OUTPUT_FILE, 'w') as csv_w:
        csv_writer = csv.writer(csv_w)
        csv_writer.writerows(csv_row)
    print('%s outputed.' % OUTPUT_FILE)
