import math, time




def main(num):

    #入力の監視と変換

    try:

        num = int(num)


    except ValueError:

        return False




    if num == 0:

        return False


    if num == 1:

        return False


    if num == 2:

        return True




    #素数列の生成

    lis = [x for x in range(2, num)]

    lim = math.floor(math.sqrt(num))


    c = 0

    while True:

        t = lis[c]


        for i in lis[c + 1: ]:

            if i % t == 0:

                lis.remove(i)


        if t < lim:

            c = c + 1

            continue


        break





    #合成数の検出

    r = True


    for i in lis:

        if num % i == 0:

            r = False


            break




    return r








if __name__ == "__main__":

    n = input()


    str = time.perf_counter()


    res = main(n)

    print("!") if res == True else print("......")


    end = time.perf_counter()


    print(end - str)
