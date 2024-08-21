import random

def func(n,m):
    mas = [[0]*n for i in range(m)]

    shu=[i for i in range(n)]
    for g in range(m):
        ind =True
        while ind:
            random.shuffle(shu)
            ind=False
            if g!=0:
                for i in range(n):
                    if mas[g-1][i]==shu[i]:
                        ind=True
        for i in range(n):
            mas[g][i]=shu[i]
    return mas

n,m=map(int,input().split())


mas=func(n,m)#введи кількість гравців n і кілSькість раундів m
for i in range(m):
    print(mas[i])

        



