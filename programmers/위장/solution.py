if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = 1

    clothes_dict = {}
    for i in clothes:
        if i[1] not in clothes_dict:
            clothes_dict[i[1]] = [i[0]]
        else:
            clothes_dict[i[1]].append(i[0])

    for i in clothes_dict.values():
        answer *= len(i) + 1

    print(answer-1)