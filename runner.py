import argparse
from pathlib import Path


def read_file(file_path):
    target_file = Path(file_path)
    if not target_file.exists():
        print("The target input file doesn't exist")
        raise SystemExit(1)
    return target_file.read_text()


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="input file")
args = parser.parse_args()


data = read_file(args.input)
