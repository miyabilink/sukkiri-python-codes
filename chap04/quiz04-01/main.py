# 以下には小問(1)〜(8)のコードを掲載しています。
# 実行したい小問のコード以外はコメントアウトするか削除してから実行してください。

# (1)
count = 0
while count < 5:
    count += 1

# (2)
count = 1
while count <= 5:
    count += 1

# (3)
data = [88, 21, 65, 160, 57]
count = 0
while count < len(data):
    count += 1

# (4)
for num in range(5):
    print(num)

# (5)
for item in [88, 21, 65, 160, 57]:
    print(item)

# (6)
data = [88, 21, 65, 160, 57]
for item in data:
    print(item)

# (7)
for item in [88, 21, 65, 160, 57]:
    if item >= 100:
        break
    print(item)

# (8)
for item in [88, 21, 65, 160, 57]:
    if item >= 100:
        continue
    print(item)