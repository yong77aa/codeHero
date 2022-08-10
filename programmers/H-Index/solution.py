if __name__ == "__main__":
    answer = 0
    citations = [3, 0, 6, 1, 5]
    sort_citations = sorted(citations)
    total = len(sort_citations)

    for i in range(total):
        if citations[i] >= total - i:
            answer = total - i
            break

    print(answer)

