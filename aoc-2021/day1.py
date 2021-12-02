import sys

def s():
  inp = list(map(int, sys.stdin.read().splitlines()))
  p1 = sum([inp[i] > inp[i-1] for i in range(1, len(inp))])
  p2 = sum([inp[i] + inp[i-1] + inp[i-2] > inp[i-1] + inp[i-2] + inp[i-3] for i in range(3, len(inp))])
  return p1, p2

if __name__ == '__main__':
  print(s())
