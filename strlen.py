def s(num):
    offset = len(num)%2==0
    return num[len(num)//2-offset:round(len(num)/2)+offset]
    

if __name__ == '__main__':
    print(s("hello"))
