MAXIMUM_LENGTH = 4

temporaryList = list(range(MAXIMUM_LENGTH))

indexsList = list()


print(temporaryList)




#注文を受け付ける

while len(temporaryList) != 0:

    n = temporaryList.pop(0)


    #指定可能な添字の一覧

    possibleNumbers = list()

    choice = str()


    for number in range(MAXIMUM_LENGTH):

        if number not in indexsList:

            possibleNumbers.append(number)


    for suitable in possibleNumbers:

        choice = choice + "{}, ".format(suitable)


    choice = choice.rstrip(", ")




    #入力と入力の監視


    while True:

        print("What is the index of '{}'?".format(n))

        answer = input("Choose from {}.: ".format(choice))


        try:

            answer = int(answer)

        except ValueError:

            print("please input positive integer value.")

            continue


        if answer not in possibleNumbers:

            print("'{}' is invalid number.".format(answer))

            continue


        break


    indexsList.append(answer)




#リクエストの通りに並び替える

orderedGoods=list(0 for x in range(MAXIMUM_LENGTH))


for i, order in enumerate(indexsList):

    orderedGoods[order] = i





#元に戻す

orderedGoods.sort()

print(orderedGoods)

