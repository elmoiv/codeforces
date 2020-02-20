# https://codeforces.com/problemset/submission/707/71462605

import sys

print(['#Black&White', '#Color'][any(i in 'CMY' for i in str(sys.stdin.readlines()))])