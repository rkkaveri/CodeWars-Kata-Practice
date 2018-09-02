def isprime(num):
    i = 2
    count = 0
    if num == 0 or num ==1 or num < 1:
        return False
    else:
        while i < num:
             if num%i == 0:
                 count +=1
                 i += 1
             else:
                 i+=1
    if count != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    print(isprime(4))
