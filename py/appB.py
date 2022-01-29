#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def funcA(z):
    ans = z * a
    print(ans)


# In[ ]:


def funcB(x, y):
    z=x+ y
    funcA(z)


# In[ ]:


x = 10
y = 20
funcB(10, 20)


# In[ ]:


price = int(input('料金を入力 >>'))
number = int(input('人数を入力 >>'))
print('1人あたり{}円です'.format(price / number))
print('プログラムを終了します')


# In[ ]:


try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print('1人あたり{}円です'.format(price / number))
except ValueError:
    print('料金または人数は整数を入力してください')
print('プログラムを終了します')


# In[ ]:


try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print('1人あたり{}円です'.format(price / number))
except ValueError:
    print('料金または人数は整数を入力してください')
except ZeroDivisionError:
    print('人数に0は入力しないでください')
print('プログラムを終了します')


# In[ ]:


try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print('1人あたり{}円です'.format(price / number))
except:
    print('料金と人数に適切な整数を入力してください')
print('プログラムを終了します')

