n = int(input())
for i in range(1,n+1):
    print(" " * (n-i) + "* "*i + " " * (n-i))
for i in range(n-1,0,-1):
    print(" " * (n-i) + "* "*i + " " * (n-i))

        # n = int(input())
        # for i in range(1, n + 1):
        #     print(" " * (n - i) + ' '.join(["*" for k in range(i)]))
        # for i in range(n - 1, 0, -1):
        #     print(" " * (n - i) + ' '.join(["*" for k in range(i)]))