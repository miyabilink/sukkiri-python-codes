h = int(input('身長(cm)は? >>')) / 100
w = float(input('体重(kg)は? >>'))
bmi = w / h / h
print('BMIは{}です'.format(bmi))

# （別解）アンパック代入とf-stringの応用構文を用いた例
h, w = int(input('身長(cm)は? >>')) / 100, \
float(input('体重(kg)は? >>'))
print(f'BMIは{ w / h ** 2 }です')