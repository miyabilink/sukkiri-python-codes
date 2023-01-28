try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print('1人あたり{}円です'.format(price / number))
except:
    print('料金と人数に適切な整数を入力してください')
print('プログラムを終了します')