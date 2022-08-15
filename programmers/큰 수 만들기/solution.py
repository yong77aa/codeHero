from itertools import combinations

if __name__ == "__main__":
    number = "1231234"
    k = 3

    arr = [i for i in number]
    com = combinations(arr, k)

    com_arr = list(com)
    com_arr = sorted(com_arr, reverse=True)

    answer = ''
    for i in com_arr[0]:
        answer += i

    print(answer)
