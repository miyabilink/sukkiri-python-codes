#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('さあ、寝ようかしら')
count = 0 # ひつじの数
count += 1
print('ひつじが{}匹'.format(count))
count += 1
print('ひつじが{}匹'.format(count))
count += 1
print('ひつじが{}匹'.format(count))
print('おやすみなさい…')


# In[ ]:


count = 0
while count < 3:
    count += 1
    print('ひつじが{}匹'.format(count))
print('おやすみなさい…')


# In[ ]:


count = 0
while count < 3:
    print('ひつじが{}匹'.format(count))
print('スヤスヤ…zzz')


# In[ ]:


is_awake = True
count = 0
while is_awake == True:
    count += 1
    print('ひつじが{}匹…'.format(count))
    key = input('もう眠りそうですか?(y/n) >>')
    if key == 'y':
        is_awake = False
print('おやすみなさい…')


# In[ ]:


count = 0                                  # カウンタ変数
student_num = int(input('学生の数を入力 >>')) # 学生の数
score_list = list()                        # 得点リスト
while count < student_num:
    count += 1
    score = int(input('{}人目の試験の得点を入力 >>'.format(count)))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print('平均点は{}点です'.format(total / student_num))


# In[ ]:


scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1


# In[ ]:


scores = [80, 20, 75, 60]
for data in scores:
    if data >= 60:
        print('合格')
    else:
        print('不合格')


# In[ ]:


for num in range(3):
    print('Pythonは楽しい')


# In[ ]:


ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5          # 目標の抽出数
samples = list() # サンプルデータを格納するリスト
for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)


# In[ ]:


ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5          # 目標の抽出数
samples = list() # サンプルデータを格納するリスト
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)


# In[ ]:


ages = [28, 50, 'ひみつ', 20, 78, 25, 22, 10, '無回答', 33]
samples = list() # サンプルデータを格納するリスト
for data in ages:
    if not isinstance(data, int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)

