is_awake = True
count = 0
while is_awake == True:
    count += 1
    print('ひつじが{}匹…'.format(count))
    key = input('もう眠りそうですか?(y/n) >>')
    if key == 'y':
        is_awake = False
print('おやすみなさい...')