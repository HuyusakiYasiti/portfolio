#連続する整数を足し合わせる関数

def summa(end, str=1):

    n = 0

    for i in range(str, end + 1):

        n = n + i

    return n




#デモ

def main():

    import time


    s = time.perf_counter()

    n = summa(100)

    e = time.perf_counter()


    print(n, e - s)




if __name__ == "__main__":

    main()

    