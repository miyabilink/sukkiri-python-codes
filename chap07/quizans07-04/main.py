# 以下には小問(1)〜(2)のコードを掲載しています。
# 実行したい小問のコード以外はコメントアウトするか削除してから実行してください。

# (1)
nums = list()
for n in range(3):
    data = int(input('{}個目の整数を入力してください >>'.format(n + 1)))
    nums.append(data)
print(max(nums))

# (2)
pi = 3.141519
print(round(pi))
for n in range(4):
    print(round(pi, n + 1))