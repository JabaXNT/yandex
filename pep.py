import argparse

lest = []
count = 0

parser = argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("--sort", action='store_const', const=True)
parser.add_argument("--count", action='store_const', const=True)
parser.add_argument("--num", action='store_const', const=True)
args = parser.parse_args()
try:
    with open(args.text) as f:
        for line in f:
            lest.append(line.strip())
            count += 1
except FileNotFoundError:
    print('ERROR')
    exit()

if args.sort:
    lest.sort()
if args.num:
    for i in range(len(lest)):
        lest[i] = str(i) + ' ' + lest[i]
for i in lest:
    print(i, sep='')
if args.count:
    print('rows count:', count)