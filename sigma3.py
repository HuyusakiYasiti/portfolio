#自然数の和を求める

def summa(end):

    n = 0

    for i in range(1, end + 1):

        n = n + i

    return n




#等差数列の和を求める

def sigma(sta, end):

    a = summa(end)

    s = summa(sta - 1)

    return a - s




#デモ

def main():


    import time


    s = time.perf_counter()

    n = sigma(1, 100)

    e = time.perf_counter()


    print(n, e - s)




if __name__ == "__main__":

    main()

    