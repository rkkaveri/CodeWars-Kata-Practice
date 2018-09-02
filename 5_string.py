def steam(txt):
    #return [word for word in txt if len(word) < 5]
    return(' '.join(w[::-1] for w in txt.split()))

if __name__ == '__main__':
    print(steam("hello the"))
