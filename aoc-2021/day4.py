import sys

def solve(draws, boards):
  lookup = [{ b[r][c]: (r, c) for r in range(5) for c in range(5)} for b in boards]
  counter = [([0] * 5, [0] * 5) for _ in boards]
  playing = set([i for i, _ in enumerate(boards)])
  first = None
  for d in draws:
    for ind, lo in enumerate(lookup):
      if d not in lo:
        continue
      counter[ind][0][lo[d][0]] += 1
      counter[ind][1][lo[d][1]] += 1
      if counter[ind][0][lo[d][0]] == 5 or counter[ind][1][lo[d][1]] == 5:
        picks = set(draws[:draws.index(d)+1])
        s = sum([int(n) for n in lo if n not in picks])
        r = int(d) * s
        if not first:
          first = r
        playing.discard(ind)
        if not playing:
          return first, r

if __name__ == '__main__':
  inp = sys.stdin.read().splitlines()
  draws = inp[0].split(',')
  boards = [[inp[i+j].split() for j in range(5)] for i in range(2, len(inp), 6)]
  # (39902, 26936)
  print(solve(draws, boards))
