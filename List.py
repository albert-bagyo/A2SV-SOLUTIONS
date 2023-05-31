if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        exp = input().split(" ")
        args = map(int, exp[1:])
        if exp[0] != 'print':
            exec("l." + exp[0] + "(*args)")
        else:
            print(l)
