import jsonlines
import os
from tqdm import tqdm

REQUIRED_KEYS = ['id', 'claim']


def transform_and_write_fever(file, inpath, outpath):
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    reader = jsonlines.Reader(open(inpath+file, 'r'))
    writer = jsonlines.Writer(open(outpath+file, 'w'))
    for row in tqdm(reader):
        writer.write({k: row[k] for k in REQUIRED_KEYS})


if __name__ == "__main__":
    f_name = 'test.jsonl'
    PATH = '/home/monk/Projects/UnsupervisedQA/data/fever/'
    OUTPATH = '/home/monk/Projects/UnsupervisedQA/data/t_fever/'

    transform_and_write_fever(f_name, PATH, OUTPATH)
