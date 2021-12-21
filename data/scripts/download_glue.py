# The codes are adapted from https://raw.githubusercontent.com/nyu-mll/jiant/master/scripts/download_glue_data.py
import os
import sys
import shutil
import argparse
import tempfile
import urllib.request
import zipfile

TASKS = ["MNLI", "SNLI"]
TASK2PATH = {
    "MNLI":'https://cims.nyu.edu/~sbowman/multinli/multinli_1.0.zip',
    "SNLI":'https://nlp.stanford.edu/projects/snli/snli_1.0.zip',
}

def download_and_extract(task, data_dir):
    print("Downloading and extracting %s..." % task)
    data_file = "%s.zip" % task
    urllib.request.urlretrieve(TASK2PATH[task], data_file)
    with zipfile.ZipFile(data_file) as zip_ref:
        zip_ref.extractall(data_dir)
    os.remove(data_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', help='directory to save data to', type=str)
    parser.add_argument('--tasks', nargs="+", help='list of tasks to get downloaded', type=str)
    args = parser.parse_args()
    if not os.path.isdir(args.data_dir):
        os.mkdir(args.data_dir)
    tasks = args.tasks
    for task in tasks:
       download_and_extract(task, args.data_dir)

if __name__ == '__main__':
    main()
