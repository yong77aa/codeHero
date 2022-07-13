# 백준알고리즘 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

import math

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(math.gcd(a, b))
    print(math.lcm(a, b))