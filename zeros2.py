import os


#書き込むデータ

l = list()

t = list("0" * 10)

l.append(",".join(t))

l *= 10


path = "zeros.csv" #生成するファイル


#書き込み

f = open(path, mode="w")

f.write("\n".join(l))

f.close()


#読み込み

f = open(path, mode="r")

print(f.read())

f.close()


#削除とその確認

os.remove(path)

print("There are" if os.path.isfile(path) else "No", f"{path}.")

