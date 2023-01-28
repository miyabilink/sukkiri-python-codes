price = input('料金を入力 >>')  # キーボード入力結果はstr型
price = int(price)
number = input('人数を入力 >>') # キーボード入力結果はstr型
number = int(number)
payment = price / number      # 割り算の結果はfloat型
payment = int(payment)
print('お支払いは' + payment + '円です')