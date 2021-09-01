from measure import Measure
from workflow import flow
import os
import csv

CONFIG_FILE = '../parameters.txt'
DATA_PATH = 'db_format'
OUTPUT_FILE = 'exp_result.csv'


def parse_parameters():
    B_FACTOR = 60
    THRESHOLD = 15
    try:
        with open(CONFIG_FILE, 'r') as f:
            line = f.readline().strip()
            if line == 'B_FACTOR':
                B_FACTOR = int(f.readline().strip())
            line = f.readline().strip()
            if line == 'THRESHOLD':
                THRESHOLD = int(f.readline().strip())
    except:
        pass
    return B_FACTOR, THRESHOLD


if __name__ == '__main__':
    BF, TH = parse_parameters()

    csv_row = [['class', 'time', 'acc']]
    for cls_ in os.listdir(DATA_PATH):
        m = Measure()
        for dat in os.listdir(os.path.join(DATA_PATH, cls_)):
            print('Classifying %s ...' % os.path.join(
                DATA_PATH, cls_, dat), flush=True)
            res = m.measure(flow, os.path.join(DATA_PATH, cls_, dat), BF, TH)
            print('<Result>\nP: %s\nT: %s\n' % res, flush=True)
        csv_row.append([cls_, m.avg_time(), m.acc()])
    with open(OUTPUT_FILE, 'w') as csv_w:
        csv_writer = csv.writer(csv_w)
        csv_writer.writerows(csv_row)
    print('%s outputed.' % OUTPUT_FILE, flush=True)
