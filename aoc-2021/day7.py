import sys

def solve(inp, costly = False):
  return min(sum( (abs(i-j) * (abs(i-j)+1) // 2) if costly else abs(i-j) for j in inp)
         for i in range(0, max(inp) // 2))

if __name__ == '__main__':
  inp = list(map(int, sys.stdin.read().split(',')))
  # 355521 100148777
  print(solve(inp), solve(inp, True))
