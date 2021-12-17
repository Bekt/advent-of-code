import sys
from collections import Counter

def solve(inp, diagonal = False):
  c = Counter()
  for (x, y) in inp:
    for i in range(min(x[1], y[1]), max(x[1], y[1]) + 1, 1 if x[0] == y[0] else -1):
      c[(x[0], i)] += 1
    for i in range(min(x[0], y[0]), max(x[0], y[0]) + 1, 1 if x[1] == y[1] else -1):
      c[(i, x[1])] += 1
    if diagonal and abs(x[0] - y[0]) == abs(x[1] - y[1]):
      start, end = (x, y) if x[0] < y[0] else (y, x)
      j = start[1]
      m = int((y[1] - x[1]) / (y[0] - x[0]))
      for i in range(start[0], end[0] + 1):
        c[(i, j)] += 1
        j += m
  return sum(True for i, v in c.items() if v >= 2)

if __name__ == '__main__':
  inp = [[ tuple(map(int, item[0].split(','))), tuple(map(int, item[2].split(','))) ]
           for item in [li.split() for li in sys.stdin.read().splitlines()] ]
  # 8111 22088
  print(solve(inp, False), solve(inp, True))
