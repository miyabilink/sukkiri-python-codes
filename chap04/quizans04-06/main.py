# 以下には小問(1)〜(3)のコードを掲載しています。
# 実行したい小問のコード以外はコメントアウトするか削除してから実行してください。

# (1)
numbers = [1, 1]
data = sum(numbers)
count = 2
while data <= 1000:
    numbers.append(data)
    data = data + numbers[count-1]
    count += 1
print(numbers)

# (2)
ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratios.append(numbers[count+1] / numbers[count])
print(ratios)

# (3)
for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)