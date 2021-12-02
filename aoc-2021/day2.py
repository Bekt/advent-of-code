import sys
from collections import Counter

def p1(inp):
  c = Counter([i for row in inp for i in [row[0]] * row[1]])
  return c['forward'] * (c['down'] - c['up'])

def p2(inp):
  h, aim, depth = 0, 0, 0
  for li in inp:
    dir, c = li
    h += c if dir == 'forward' else 0
    depth += aim * c if dir == 'forward' else 0
    aim += c if dir == 'down' else -c if dir == 'up' else 0
  return h * depth

if __name__ == '__main__':
  inp = [( li.split(' ')[0], int(li.split(' ')[1]) ) for li in sys.stdin.read().splitlines()]
  # p1, p2 2102357 2101031224
  print(p1(inp), p2(inp))
