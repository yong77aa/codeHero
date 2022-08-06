if __name__ == "__main__":
    str = input().split(",")
    data_type = str[0].split(" ")[0]

    for i in range(len(str)):
        if i != 0:
            # 데이터 타입을 붙임
            str[i] = data_type + str[i]

        temp_data_type, temp_data_name = str[i].split(" ")  # 변수 타입과 변수명 분리
        temp_data_name = temp_data_name.replace(";", "")  # 기존 세미콜론 제거

        # 변수명 역순으로 반복
        for j in reversed(temp_data_name):
            # 변수명이 아닌 경우
            if not j.isalpha():
                temp_data_type += j  # 변수 타입에 누적
                temp_data_name = temp_data_name.replace(j, "")  # 이후 변수명에서 해당 데이터 타입 삭제
                print(temp_data_name)

        str[i] = temp_data_type + " " + temp_data_name + ";"  # 각 변수 끝에 세미콜론 추가

    # 역순으로 넣어서 대괄호가 반대인 경우
    for i, val in enumerate(str):
        str[i] = val.replace("][", "[]")

    for i in str:
        print(i)

    # str = input().split(" ")
    # data_type = str[0]
    # del str[0]
    #
    # for i in str:
    #     i = i.replace(",", "").replace(";", "")  # 세미콜론, 쉼표 제거
    #
    #     print(data_type, end="")  # 변수 타입 출력
    #
    #     # 변수명에서 역순으로
    #     for j in reversed(i):
    #         # 알파벳이 아닌 경우
    #         if not j.isalpha():
    #             if j == "[":
    #                 print("]", end="")
    #             elif j == "]":
    #                 print("[", end="")
    #             else:
    #                 print(j, end="")
    #
    #     # 한 칸
    #     print(" ", end="")
    #
    #     # 변수명 출력
    #     for j in i:
    #         if j.isalpha():
    #             print(j, end="")
    #
    #     print(";")
