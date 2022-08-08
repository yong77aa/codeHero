if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    answer = []

    # [장르, 재생횟수, 고유번호] 리스트 생성
    song_list = [[genres[i], plays[i], i] for i in range(len(genres))]
    # 장르, 재생횟수 역순, 고유번호 순으로 정렬
    song_list.sort(key=lambda x: (x[0], -x[1], x[2]))

    # 많이 재생된 장르
    genre_plays = {}
    for info in song_list:
        if info[0] not in genre_plays:
            genre_plays[info[0]] = info[1]
        else:
            genre_plays[info[0]] += info[1]

    # 많이 재생된 순으로 정렬
    sorted_song = sorted(genre_plays.items(), key=lambda x: -x[1])

    for i in sorted_song:
        count = 0
        for j in song_list:
            if i[0] == j[0]:
                count += 1
                # 최대 2곡
                if count > 2:
                    break
                else:
                    answer.append(j[2])

    print(answer)