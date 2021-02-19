import time

def ev1(i, x1, x2, y1, y2, a, b):
        q = a // b
        r = a % b
        print("i=",i,"x",i,"=",x2," y",i,"=",y2,"a=",a,"b=",b," r=",r," q=",q)
        if b == 0 or r == 0:
            return
        ev1(i + 1, x2, x1 - q * x2, y2, y1 - q * y2, b, r)



def ev2(a, b):
    while a % 2 == 0 and b % 2 == 0:
        a, b = a >> 1, b >> 1
    u, v, A, B, C, D, i = a, b, 1, 0, 0, 1, 1

    while u != 0:
        print("i=", i, "\n", "x = ", C, "\n", "y = ", D, "\n", "r = ", v, "\n")
        i += 1
        while u % 2 == 0:
            u = u >> 1
            if A % 2 == 0 and B%2 == 0:
                A, B = A >> 1, B >> 1
            else:
                A, B = (A + b) >> 1, (B - a) >> 1
        while v % 2 == 0:
            v = v >> 1
            if C % 2 == 0 and D%2 == 0:
                C, D = C >> 1, D >> 1
            else:
                C, D = (C + b) >> 1, (D - a) >> 1
        if u >= v:
            u, A, B = u - v, A - C, B - D
        else:
            v, C, D = v - u, C - A, D - B
    print("x = ", C, "\n", "y = ", D, "\n", "answ = ", v, "\n")
    print("value: ",  a*C + b*D)


def ev3(a, b):
    x1, y2, x2, y1, i = 1, 1, 0, 0, 0
    olya=20
    print("HALILUYA")
    bufa, bufb = a, b
    while b != 0:
        i+=1
        q = a // b
        b, a, r = a % b, b, b
        x2, x1 = x1 - x2 * q, x2
        y2, y1 = y1 - y2 * q, y2

        if b > r // 2:
            b = r - b
            x2, y2 = x1 - x2, y1 - y2
        print("i=", i, "\n", "x = ", x1, "\n", "y = ", y1, "\n", "r = ", r, "\n")
    print(" x = ", x1, "\n", "y = ", y1, "\n", "ANS = ", a, "\n")
    print("Final answ: ", bufa * x1 + bufb * y1)


i=0
a=[24,41654654445214971353, 199631117672973429856593683352454245013, 29119878183171490691953211834919337704617987225259240969011807046991506834704477]
b=[93,35015221631971064149, 857168951341389280011633162524466021001, 29119878183171490691953211834919337704617987225259240969011807046991506834704477]
t = time.time()
ev1(0, 1, 0, 0, 1, a[i], b[i])
print("FIRST algorithm time:", (time.time() - t)/1000)

t = time.time()
ev2(a[i], b[i])
#ev2(9,27)
print("SECOND algorithm time:", (time.time() - t)/1000)

t = time.time()
ev3(a[i], b[i])
print("THIRD algorithm time:", (time.time() - t)/1000)

#ev3(1234, 3)








