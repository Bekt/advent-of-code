import re
import sys

RE = re.compile('^(\d+)-(\d+) (.+): (.+)')

def solve(t):
    m = RE.match(t)
    c = m.group(4).count(m.group(3))
    return int(m.group(1)) <= c <= int(m.group(2))

def part2(t):
    m = RE.match(t)
    p1, p2, s, str = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    return ((str[p1-1] == s) + (str[p2-1] == s)) == 1

if __name__ == '__main__':
    # part1 = sum([solve(line) for line in sys.stdin.readlines()])
    # print(part1)
    part2 = sum([part2(line) for line in sys.stdin.readlines()])
    print(part2)
