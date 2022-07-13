# 백준알고리즘 피보나치 수5
# https://www.acmicpc.net/problem/10870


def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    n = int(input())
    print(fibo(n))

