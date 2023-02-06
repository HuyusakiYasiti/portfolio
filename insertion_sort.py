import random


tem = [random.randint(0, 9) for x in range(10)]#ソートするリスト

print(tem)




res = []#ソート済みの要素


#挿入位置の検索

for i in tem:

    for j in res:

        if i <= j:

            res.insert(res.index(j), i)

            break


    #末尾の要素の添加

    if len(res) == tem.index(i):

        res.append(i)




print(res)       


