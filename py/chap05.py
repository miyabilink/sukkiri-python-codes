#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student_list = ['浅木', '松田']
count = 0
for student in student_list:
    print('{}さんの試験結果を入力してください'.format(student))
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    if student == '浅木':
        asagi_scores = [network, database, security]
        asagi_avg = sum(asagi_scores) / len(asagi_scores)
    else:
        matsuda_scores = [network, database, security]
        matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
print('浅木さんの平均点は{}です'.format(asagi_avg))
print('松田さんの平均点は{}です'.format(matsuda_avg))


# In[ ]:


# 得点を入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')
# 平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
# 結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)


# In[ ]:


def hello():
    print('こんにちは。工藤です。')


# In[ ]:


hello()


# In[ ]:


def input_scores():
    name = ''
    print('{}の試験結果を入力してください'.format(name))


# In[ ]:


name = '浅木'
input_scores()
name = '松田'
input_scores()


# In[ ]:


def hello(name):
    print('こんにちは。{}です。'.format(name))


# In[ ]:


hello('浅木')
hello('松田')


# In[ ]:


def profile(name, age, hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}歳です。'.format(age))
    print('趣味は{}です。'.format(hobby))


# In[ ]:


profile('浅木', 24, 'カフェ巡り')


# In[ ]:


def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}です'.format(avg))


# In[ ]:


def input_scores(name):
    print('{}さんの試験結果を入力してください'.format(name))
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]
def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}です'.format(avg))


# In[ ]:


input_scores('浅木')
calc_average(scores)


# In[ ]:


def plus(x, y):
    answer = x + y
    return answer


# In[ ]:


answer = plus(100, 50)
print('足し算の答えは{}です'.format(answer))    


# In[ ]:


def input_scores(name):
    print('{}さんの試験結果を入力してください'.format(name))
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]
    return scores
 
def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print('{}さんの平均点は{}です'.format(name, avg))


# In[ ]:


# 浅木と松田の得点入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')
# 平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
# 結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)


# In[ ]:


def plus_and_minus(a, b):
    return a + b, a - b

next, prev = plus_and_minus(1978, 1)


# In[ ]:


def plus_and_minus(a, b):
    return (a + b, a - b)

(next, prev) = plus_and_minus(1978, 1)


# In[ ]:


def eat(breakfast, lunch, dinner):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))


# In[ ]:


print('8月1日')
eat('トースト', 'おにぎり', 'カレー')
print('8月2日')
eat('納豆ごはん', 'ラーメン', 'カレー')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当', 'カレー')


# In[ ]:


def eat(breakfast, lunch, dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))


# In[ ]:


print('8月1日')
eat('トースト', 'おにぎり')
print('8月2日')
eat('納豆ごはん', 'ラーメン')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドウィッチ', 'しゅうまい弁当')


# In[ ]:


def eat(breakfast, lunch='ラーメン', dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))


# In[ ]:


eat('納豆ごはん', 'ラーメン', 'カレーうどん')


# In[ ]:


eat(breakfast='納豆ごはん', dinner='カレーうどん') # 1
eat(dinner='カレーうどん', breakfast='納豆ごはん') # 2
eat('納豆ごはん', dinner='カレーうどん')           # 3


# In[ ]:


def eat(breakfast, lunch, dinner='カレー', desserts=()):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました'.format(d))


# In[ ]:


eat('トースト', 'パスタ', 'カレー', ('アイス', 'チョコ', 'パフェ'))


# In[ ]:


def eat(breakfast, lunch, dinner='カレー', *desserts):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました'.format(d))


# In[ ]:


eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')


# In[ ]:


name = '松田'
def hello():
    print('こんにちは' + name + 'さん')


# In[ ]:


hello()


# In[ ]:


name = '松田'
def change_name():
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')


# In[ ]:


change_name()
hello()


# In[ ]:


name = '松田'
def change_name():
    global name
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')

