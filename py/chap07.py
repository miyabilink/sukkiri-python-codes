#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = input('何を記録しますか? >>')
file = open('diary.txt', 'a')
file.write(text + '\n')
file.close()


# In[ ]:


text = input('今日は何をした? >>')
with open('diary.txt', 'a') as file:
    file.write(text + '\n')


# In[ ]:


import math
print('円周率は{}です'.format(math.pi))
print('小数点以下を切り捨てれば{}です'.format(math.floor(math.pi)))
print('小数点以下を切り上げれば{}です'.format(math.ceil(math.pi)))


# In[ ]:


import math as m
print('円周率は{}です'.format(m.pi))
print('小数点以下を切り捨てれば{}です'.format(m.floor(m.pi)))
print('小数点以下を切り上げれば{}です'.format(m.ceil(m.pi)))


# In[ ]:


from math import pi
from math import floor
print('円周率は{}'.format(pi))
print('小数点以下を切り捨てれば{}です'.format(floor(pi)))


# In[ ]:


from math import log
def log(msg):
    print('{}を記録します'.format(msg))
log(10)


# In[ ]:


from math import pi as ensyuritsu
from math import floor as kirisute
print('円周率は{}'.format(ensyuritsu))
print('小数点以下を切り捨てれば{}です' .format(kirisute(ensyuritsu)))


# In[ ]:


from math import *
print('円周率は{}です'.format(pi))
print('小数点以下を切り捨てれば{}です'.format(floor(pi)))
print('小数点以下を切り上げれば{}です'.format(ceil(pi)))


# In[ ]:


import http.client
conn = http.client.HTTPConnection('www.python.org')
# ：


# In[ ]:


from http import client
conn = client.HTTPConnection('www.python.org')
# ：


# In[ ]:


from http.client import HTTPConnection
conn = HTTPConnection('www.python.org')
# ：


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
weight = [68.4, 68.0, 69.5, 68.4, 68.6, 70.2, 71.4, 70.8, 68.5, 68.6, 68.3, 68.4]
plt.plot(weight)


# In[ ]:


import requests
response = requests.get('https://www.python.org/downloads/')
text = response.text
print(text)


# In[ ]:


import http.client
conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
text = response.read().decode('UTF-8')
print(text)
conn.close()

