def accum(s):
    answer = []
    count = 0
    for index,char in enumerate(s):
        if index == count:
            if index > 0:
                answer.append("-")
            answer.append(char.upper())
            if index > 0:
                for demon in range(index):
                    answer.append(char)
            count += 1
    return ''.join(answer)

if __name__ == '__main__':
    print(accum("hello"))
