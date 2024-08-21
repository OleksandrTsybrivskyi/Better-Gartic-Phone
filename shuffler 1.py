import random

def func(n):
    mas = [[0]*n for i in range(n)]
    was = [[False]*n for i in range(n)]
    # for i in range(n):
    #     was[i][i]=True
    shu=[i for i in range(n)]
    for g in range(n):
        ind =True
        while ind:
            random.shuffle(shu)
            ind=False
            for i in range(n):
                if was[shu[i]][i]:
                    ind=True
        for i in range(n):
            was[shu[i]][i]=True
            mas[g][i]=shu[i]
    return mas

n=int(input())
mas=func(n) #Введи кількість гравців
for i in range(n):
    print(mas[i])
        



