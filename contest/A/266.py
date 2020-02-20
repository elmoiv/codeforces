# https://codeforces.com/contest/266/submission/71480697

import sys

line, line_new = [sys.stdin.readlines()[1][:-1]] * 2

for i in line:
    line_new = line_new.replace(i * 2, i)

print(len(line) - len(line_new))