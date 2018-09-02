def accum(s):
    answer = []
    for index,char in enumerate(s):
        if index > 0:
            answer.append("-")
        answer.append(char.upper())
        if index > 0:
            for demon in range(index):
                answer.append(char.lower())
    return ''.join(answer)

if __name__ == '__main__':
    print(accum("ZpglnRxqenU"))
