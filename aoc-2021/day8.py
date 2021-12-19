import sys
from collections import Counter

def p1(inp):
  return sum(len(list(filter(lambda w: (len(w) in [2, 3, 4, 7]), ov))) for (sig, ov) in inp)

def p2(sig, ov):
  clock = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
  known = {2: 1, 3: 7, 4: 4, 7: 8}
  nums = {known[len(w)]: set(w) for w in sig if len(w) in known}
  c = Counter([ch for w in sig for ch in w])
  c = {k: [v for v in c if c[v] == k] for k in dict(c).values()}
  m = {'b': c[6][0], 'e': c[4][0], 'f': c[9][0]}
  m['a'] = list(nums[7] - nums[1])[0]
  m['c'] = c[8][1] if c[8][0] == m['a'] else c[8][0]
  m['d'] = c[7][0] if c[7][0] in nums[4] else c[7][1]
  m['g'] = c[7][1] if m['d'] == c[7][0] else c[7][0]
  m = {m[k]: k for k in m}
  digit = [str(clock.index(''.join(sorted([m[ch] for ch in d])))) for d in ov]
  return int(''.join(digit))


if __name__ == '__main__':
  inp = [[p.split() for p in li.split('|')] for li in sys.stdin.read().splitlines()]
  # 349 1070957
  print(p1(inp))
  print(sum(p2(sig, ov) for sig, ov in inp))
