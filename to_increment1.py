import time




#入力とその監視

while True:

    n = input("Please input number.: ")


    try:

        n = int(n)


    except ValueError:

        print("Please type using half-width characters and enter an integer.")

        continue


    break




#出力

for i in range(n):

    i = i + 1

    time.sleep(1)

    print(i)


