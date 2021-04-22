import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', type=str)

args = parser.parse_args()

for filename in os.listdir(args.dir):
    new_filename = filename[:-10] + '.png'
    os.rename(f'{args.dir}/{filename}', f'{args.dir}/{new_filename}')
