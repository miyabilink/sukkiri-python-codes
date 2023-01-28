#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(1)
print(10)


# In[ ]:


print(1 + 1)
print(10 - 2)


# In[ ]:


print('1' + '1')


# In[ ]:


print('Python' + 'の世界へようこそ')
print('Pythonは' + 'とっても' * 3 + '楽しいですよ' )


# In[ ]:


print('はじめまして松田です身体を動かすのが好きです')
print('はじめまして\n松田です\n身体を動かすのが好きです')
print('引用符には、\'と\"があります')


# In[ ]:


print('半径が3cmの円の直径は、')
print(3 * 2)
print('その円の円周の長さは、直径×円周率で求まるため、')
print(3 * 2 * 3.14)


# In[ ]:


name = '松田'
age = 22
print(name)
print(age)


# In[ ]:


print('半径が3cmの円の直径は、')
dia = 3 * 2 # diaはdiameter(直径)の略
print(dia)
print('その円の円周の長さは、')
print(dia * 3.14)


# In[ ]:


age = 20
print('浅木の年齢は')
print(age)
age = 24
print('うそ。本当は')
print(age)


# In[ ]:


name, age = '浅木', 24


# In[ ]:


age = 24
print('浅木先輩の今年の年齢は…')
print(age)
age + 1
print('来年は…')
print(age)
age + 1
print('再来年は…')
print(age)


# In[ ]:


age = 24
print('浅木先輩の今年の年齢は…')
print(age)
age = age + 1
print('来年は…')
print(age)
age = age + 1
print('再来年は…')
print(age)


# In[ ]:


age += 1
price *= 1.5


# In[ ]:


name = input('あなたの名前を入力してください >>')
print('おお' + name + 'よ、そなたがくるのを待っておったぞ!')


# In[ ]:


price = input('料金を入力 >>')
number = input('人数を入力 >>')
payment = price / number
print('お支払いは' + payment + '円です')


# In[ ]:


x = '松田' # 名前
print(x)
x = 23    # 年齢
print(x)
x = 175.6 # 身長
print(x)


# In[ ]:


x = 10
print(type(x))


# In[ ]:


price = input('料金を入力 >>')
print(type(price))


# In[ ]:


x = 3.14
y = int(x)
print(y)       # 変換結果を表示
print(type(y)) # 変換後のデータ型を表示
z = str(x)
print(z)       # 変換結果を表示
print(type(z)) # 変換後のデータ型を表示
print(z * 2)


# In[ ]:


price = input('料金を入力 >>')  # キーボード入力結果はstr型
price = int(price)
number = input('人数を入力 >>') # キーボード入力結果はstr型
number = int(number)
payment = price / number      # 割り算の結果はfloat型
payment = int(payment)
print('お支払いは' + payment + '円です')


# In[ ]:


name = '松田光太'
age = 23
height =175.6
print('私の名前は' + name + 'で、年齢は' + str(age) +
      '歳で、身長は' + str(height) + 'cmです')


# In[ ]:


name = '松田光太'
age = 23
height = 175.6
print('私の名前は{}で、年齢は{}歳で、身長は{}cmです'
      .format(name, age, height))


# In[ ]:


price = int(input('料金を入力 >>'))
number = int(input('人数を入力 >>'))
payment = int(price / number)
print('お支払いは{}円です'.format(payment))

