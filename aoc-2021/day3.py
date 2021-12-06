import sys
from collections import Counter


def p1(inp):
  tm = list(zip(*inp))
  gm = ['1' if tm[i].count('1') > len(inp) // 2 else '0' for i in range(len(inp[0]))]
  em = ['1' if v == '0' else '0' for v in gm]
  return int(''.join(gm), 2) * int(''.join(em), 2)


def p2(inp):
  oxyra, co2ra = rating(inp, True), rating(inp, False)
  return int(oxyra, 2) * int(co2ra, 2)


def rating(ra, oxy):
  ind = 0
  while len(ra) > 1:
    ones = list(zip(*ra))[ind].count('1')
    most = '1' if ones >= len(ra) / 2 else '0'
    least = '1' if ones < len(ra) / 2 else '0'
    ra = list(filter(lambda w: w[ind] == most if oxy else w[ind] == least, ra))
    ind += 1
  return ra[0]


if __name__ == '__main__':
  inp = sys.stdin.read().splitlines()
  # 4191876 3414905
  print(p1(inp), p2(inp))
