def tower_builder(n):
    a = []
    for i in range(n):
        a.append(" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1))
    return a




if __name__ == '__main__':
    print(tower_builder(3))
