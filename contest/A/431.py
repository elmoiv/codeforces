# https://codeforces.com/contest/431/submission/71462337

import sys

data = sys.stdin.readlines()
calories = list(map(int, data[0].split()))

print(sum(map(lambda i: calories[int(i) - 1], data[1][:-1])))