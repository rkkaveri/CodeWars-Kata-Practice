def denmon(num):
    z = []
    i = 0
    while i < len(num):
        if int(num[i])%2 == 0:
            z.append(num[i])

        i += 2

    #num.split()
    print(int(num[0]))
    return num

if __name__ == '__main__':
    #z = denmon("2 4 7 8 10")
    #z +=1
    denmon("1 2 4 5")
    #list = [1,2,3,4]
    #print(list)
