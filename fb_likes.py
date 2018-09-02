def likes(names):
    num = len(names)
    if names == []:
        return "no one likes this"
    elif num == 1:
        return( str(names[0])+" likes this")
    elif num == 2:
        return(str(names[0]+" and "+names[1])+" like this")
    elif num == 3:
        return(str(names[0])+", "+str(names[1])+" and "+str(names[2])+" likes this")
    else:
        return(str(names[0])+", "+str(names[1])+" and "+ str(num -2)+" others like this")



if __name__ == '__main__':
    print(likes(['james','kashish','nikita','hello']))
