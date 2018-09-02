def d(dna):
    answer = []
    for index,char in enumerate(dna):
        if char == 'A':
            answer.append("T")
        elif char == 'C':
                answer.append("G") # replace ';' in odd indices with "!"
        elif char == 'T':
            answer.append('A')
        elif char == 'G':
            answer.append('C')
        else:
            answer.append(char)
    return ''.join(answer)

if __name__ == '__main__':
    print(d("AAAB"))
