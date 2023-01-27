# 以下には小問(1)〜(3)のコードを掲載しています。
# 実行したい小問のコード以外はコメントアウトするか削除してから実行してください。

# (1)
isError = False
n = 99
if isError == False and n < 100:
    print('正解です')

# (2)
number = int(input('数値を入力してください >>'))
if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')

# (3)
greeting = input('挨拶をどうぞ >>')
if greeting == 'こんにちは':
    print('ようこそ!')
elif greeting == '景気は?':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で!')
else:
    print('どうしました?')